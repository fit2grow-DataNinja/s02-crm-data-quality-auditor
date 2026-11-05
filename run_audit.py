import argparse
from s02.audit import audit,write_results

def main():
    p=argparse.ArgumentParser(description='S02 read-only HubSpot CSV data quality auditor')
    p.add_argument('--contacts',required=True);p.add_argument('--deals',required=True)
    p.add_argument('--associations',help='Optional PARTIAL association reference; never used to infer missing associations')
    p.add_argument('--out',default='audit_output')
    args=p.parse_args()
    summary,issues=audit(args.contacts,args.deals,args.associations)
    write_results(summary,issues,args.out)
    print(f"Audited {summary['contacts_checked']} contacts, {summary['deals_checked']} deals; {len(issues)} findings. Output: {args.out}")
if __name__=='__main__':main()
