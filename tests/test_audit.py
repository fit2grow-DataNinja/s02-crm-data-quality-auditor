import csv,tempfile,unittest
from pathlib import Path
from s02.audit import audit, write_results

def make(p,rows):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)

class AuditTests(unittest.TestCase):
    def test_rules_and_partial_associations(self):
        with tempfile.TemporaryDirectory() as t:
            c=Path(t)/'c.csv';d=Path(t)/'d.csv';a=Path(t)/'a.csv'
            make(c,[{'Record ID':'1','Email':'a@example.com'},{'Record ID':'2','Email':'a@example.com'}])
            make(d,[{'Record ID':'3','Deal Name':'Example','Deal Stage':'Negotiation','Amount':'','Deal owner':''}])
            make(a,[{'Deal Record ID':'3','Contact Record ID':'999'}])
            summary,issues=audit(c,d,a)
            rules={i['rule_id'] for i in issues}
            self.assertIn('CRM-EMAIL-DUPLICATE',rules)
            self.assertIn('CRM-NEGOTIATION-AMOUNT-MISSING',rules)
            self.assertIn('CRM-ASSOCIATION-CONTACT-UNKNOWN',rules)
            self.assertNotIn('CRM-ASSOCIATION-MISSING',rules)
            self.assertEqual(summary['coverage']['contact_associations'],'partial_reference_only_no_missing_association_inference')
    def test_missing_deal_owner_at_qualified_stage(self):
        """Qualified deals without an owner trigger the provisional owner rule."""
        with tempfile.TemporaryDirectory() as t:
            contacts = Path(t) / 'contacts.csv'
            deals = Path(t) / 'deals.csv'
            make(contacts, [{'Record ID': '1', 'Email': 'synthetic@example.com'}])
            make(deals, [{
                'Record ID': '2', 'Deal Name': 'Synthetic Deal',
                'Deal Stage': 'Qualified', 'Amount': '100', 'Deal owner': '',
            }])
            summary, issues = audit(contacts, deals)
            owner_issues = [i for i in issues if i['rule_id'] == 'CRM-DEAL-OWNER-MISSING']
            self.assertEqual(len(owner_issues), 1)
            self.assertEqual(owner_issues[0]['record_id'], '2')
            self.assertEqual(owner_issues[0]['severity'], 'medium')
            self.assertEqual(summary['by_rule']['CRM-DEAL-OWNER-MISSING'], 1)

    def test_report_lists_evaluated_checks_without_associations(self):
        with tempfile.TemporaryDirectory() as t:
            base = Path(t)
            c = base / 'contacts.csv'; d = base / 'deals.csv'
            make(c, [{'Record ID': '1', 'Email': 'synthetic@example.com'}])
            make(d, [{'Record ID': '2', 'Deal Name': 'Example', 'Deal Stage': 'Qualified', 'Amount': '100', 'Deal owner': 'Owner'}])
            summary, issues = audit(c, d)
            write_results(summary, issues, base / 'output')
            report = (base / 'output' / 'report.md').read_text()
            evaluated = report.split('## Checks evaluated')[1].split('## Checks not fully evaluated')[0]
            self.assertEqual(summary['issues_total'], 0)
            self.assertIn('CRM-EMAIL-DUPLICATE', evaluated)
            self.assertIn('CRM-DEAL-OWNER-MISSING', evaluated)
            self.assertNotIn('CRM-ASSOCIATION-DEAL-UNKNOWN', evaluated)
            self.assertIn('not_evaluated_no_association_export', report)
            self.assertIn('not_evaluated_no_extract_timestamp', report)

    def test_report_lists_association_reference_checks_only_when_supplied(self):
        with tempfile.TemporaryDirectory() as t:
            base = Path(t)
            c = base / 'contacts.csv'; d = base / 'deals.csv'; a = base / 'associations.csv'
            make(c, [{'Record ID': '1', 'Email': 'synthetic@example.com'}])
            make(d, [{'Record ID': '2', 'Deal Name': 'Example', 'Deal Stage': 'Qualified', 'Amount': '100', 'Deal owner': 'Owner'}])
            make(a, [{'Deal Record ID': '2', 'Contact Record ID': '1'}])
            summary, issues = audit(c, d, a)
            write_results(summary, issues, base / 'output')
            report = (base / 'output' / 'report.md').read_text()
            evaluated = report.split('## Checks evaluated')[1].split('## Checks not fully evaluated')[0]
            self.assertEqual(summary['issues_total'], 0)
            self.assertIn('CRM-ASSOCIATION-DEAL-UNKNOWN', evaluated)
            self.assertIn('CRM-ASSOCIATION-CONTACT-UNKNOWN', evaluated)
            self.assertIn('partial_reference_only_no_missing_association_inference', report)
            self.assertNotIn('CRM-ASSOCIATION-MISSING', evaluated)

    def test_schema_rejection(self):
        with tempfile.TemporaryDirectory() as t:
            c=Path(t)/'c.csv';d=Path(t)/'d.csv'
            make(c,[{'Email':'x@example.com'}]);make(d,[{'Record ID':'1','Deal Name':'X','Deal Stage':'Qualified','Amount':'2'}])
            with self.assertRaises(ValueError):audit(c,d)
if __name__=='__main__':unittest.main()
