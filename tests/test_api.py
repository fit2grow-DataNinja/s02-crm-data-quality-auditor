import unittest
try:
    from fastapi.testclient import TestClient
    from s02.api import app
except ImportError:
    TestClient = None

@unittest.skipUnless(TestClient, 'Install requirements-api.txt to run API tests')
class ApiTests(unittest.TestCase):
    def test_upload_and_audit(self):
        with TestClient(app) as client:
            response = client.post('/audit', files={
                'contacts':('contacts.csv',b'Record ID,Email\n1,a@example.com\n','text/csv'),
                'deals':('deals.csv',b'Record ID,Deal Name,Deal Stage,Amount,Deal owner\n2,Example,Negotiation,100,Owner\n','text/csv'),
            })
            self.assertEqual(response.status_code,200,response.text)
            import zipfile,io,json
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                summary=json.loads(z.read('summary.json'))
                self.assertEqual(summary['issues_total'],0)
    def test_reject_wrong_schema(self):
        with TestClient(app) as client:
            response = client.post('/audit', files={
                'contacts':('contacts.csv',b'Email\na@example.com\n','text/csv'),
                'deals':('deals.csv',b'Record ID,Deal Name,Deal Stage,Amount\n2,X,Qualified,1\n','text/csv'),
            })
            self.assertEqual(response.status_code,422)
