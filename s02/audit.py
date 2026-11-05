"""S02 deterministic, read-only CRM CSV audit. Python standard library only."""
import csv, json, re
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path

STAGES = ['Lead Identified','Qualified','Needs Analysis','Proposal Sent','Negotiation','Closed Won','Closed Lost']
LATE_STAGES = {'Proposal Sent','Negotiation','Closed Won','Closed Lost'}
EMAIL = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]+$')

def load_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames: raise ValueError(f'No CSV header: {path}')
        return list(reader), reader.fieldnames

def audit(contacts_path, deals_path, associations_path=None, *, run_time=None):
    contacts, ch = load_csv(contacts_path)
    deals, dh = load_csv(deals_path)
    if not {'Record ID','Email'}.issubset(ch): raise ValueError('Contacts export requires Record ID and Email columns')
    if not {'Record ID','Deal Name','Deal Stage','Amount'}.issubset(dh): raise ValueError('Deals export requires Record ID, Deal Name, Deal Stage, Amount')
    issues=[]
    def flag(rule,severity,obj,record,field,observed,explanation):
        issues.append(dict(rule_id=rule,severity=severity,object=obj,record_id=record,field=field,observed=str(observed),explanation=explanation))
    def rid(r): return r.get('Record ID','').strip()
    for obj, rows in [('contact',contacts),('deal',deals)]:
        ids=Counter(rid(r) for r in rows if rid(r))
        for r in rows:
            key=rid(r)
            if not key: flag('CRM-RECORD-ID-MISSING','high',obj,'', 'Record ID','', 'Missing source record identifier')
            elif ids[key]>1: flag('CRM-RECORD-ID-DUPLICATE','high',obj,key,'Record ID',key,'Duplicate record identifier in export')
    emails=Counter(r.get('Email','').strip().casefold() for r in contacts if r.get('Email','').strip())
    for r in contacts:
        key=rid(r); email=r.get('Email','').strip()
        if not email: flag('CRM-EMAIL-MISSING','medium','contact',key,'Email','', 'Contact has no email; may be allowed by policy')
        elif not EMAIL.fullmatch(email): flag('CRM-EMAIL-INVALID','medium','contact',key,'Email',email,'Email syntax is invalid')
        if email and emails[email.casefold()]>1: flag('CRM-EMAIL-DUPLICATE','high','contact',key,'Email',email,'Email occurs more than once in export')
    names=Counter(r.get('Deal Name','').strip().casefold() for r in deals if r.get('Deal Name','').strip())
    for r in deals:
        key=rid(r); stage=r.get('Deal Stage','').strip(); name=r.get('Deal Name','').strip(); amount=r.get('Amount','').strip()
        if not name: flag('CRM-DEAL-NAME-MISSING','high','deal',key,'Deal Name','', 'Deal name is missing')
        elif names[name.casefold()]>1: flag('CRM-DEAL-NAME-DUPLICATE','medium','deal',key,'Deal Name',name,'Duplicate deal name (review, not proof of duplicate deal)')
        if stage not in STAGES: flag('CRM-STAGE-UNKNOWN','high','deal',key,'Deal Stage',stage,'Stage is not in pilot stage catalogue')
        if not amount:
            if stage=='Negotiation': flag('CRM-NEGOTIATION-AMOUNT-MISSING','high','deal',key,'Amount','', 'Negotiation deal has no amount')
        else:
            try:
                value=Decimal(amount.replace(',',''))
                if not value.is_finite() or value<0: flag('CRM-AMOUNT-INVALID','high','deal',key,'Amount',amount,'Deal amount must be finite and nonnegative')
            except InvalidOperation: flag('CRM-AMOUNT-INVALID','high','deal',key,'Amount',amount,'Deal amount is not numeric')
        if stage in STAGES[1:] and not r.get('Deal owner','').strip():
            flag('CRM-DEAL-OWNER-MISSING','medium','deal',key,'Deal owner','', 'Deal at Qualified or later has no owner (pilot policy hypothesis)')
    checks={'contact_associations':'not_evaluated_no_association_export','close_date_source_reconciliation':'not_evaluated_no_original_value_in_export','freshness':'not_evaluated_no_extract_timestamp'}
    if associations_path:
        assocs, ah=load_csv(associations_path)
        if not {'Deal Record ID','Contact Record ID'}.issubset(ah): raise ValueError('Association file requires Deal Record ID and Contact Record ID')
        deal_ids={rid(r) for r in deals}; contact_ids={rid(r) for r in contacts}
        linked=set()
        for a in assocs:
            d=a['Deal Record ID'].strip(); c=a['Contact Record ID'].strip()
            if d not in deal_ids: flag('CRM-ASSOCIATION-DEAL-UNKNOWN','high','association',d,'Deal Record ID',d,'Association references deal absent from export')
            if c not in contact_ids: flag('CRM-ASSOCIATION-CONTACT-UNKNOWN','high','association',d,'Contact Record ID',c,'Association references contact absent from export')
            if d in deal_ids and c in contact_ids: linked.add(d)
        # Association import/reference file is a subset, not a full CRM export.
        checks['contact_associations']='partial_reference_only_no_missing_association_inference'
        checks['known_associations_in_file']=len(linked)
    summary={'contacts_checked':len(contacts),'deals_checked':len(deals),'issues_total':len(issues),'by_severity':dict(Counter(i['severity'] for i in issues)),'by_rule':dict(sorted(Counter(i['rule_id'] for i in issues).items())),'coverage':checks,'run_time_utc':run_time or datetime.now(timezone.utc).isoformat()}
    return summary, issues

def write_results(summary,issues,output):
    out=Path(output); out.mkdir(parents=True,exist_ok=True)
    (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    fields=['rule_id','severity','object','record_id','field','observed','explanation']
    with (out/'issues.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(issues)
    lines=['# S02 CRM Data Quality Audit','',f"Contacts checked: **{summary['contacts_checked']}**; deals checked: **{summary['deals_checked']}**; findings: **{summary['issues_total']}**.",'','## Findings by rule','']
    for rule,count in summary['by_rule'].items():lines.append(f'- {rule}: {count}')
    if not summary['by_rule']:lines.append('- No rule violations detected in evaluated checks.')
    lines+=['','## Checks not fully evaluated','']
    for k,v in summary['coverage'].items():lines.append(f'- {k}: {v}')
    lines+=['','## Interpretation','','Findings reflect provisional pilot rules, not universal HubSpot requirements. Missing owners may be intentional. No external AI was used. Source records were not modified.','', '## Recommended review','','Confirm owner-assignment policy; obtain a complete deal-contact association export before enforcing missing-association rules; reconcile close dates against source imports only with a documented transformation policy.']
    (out/'report.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
