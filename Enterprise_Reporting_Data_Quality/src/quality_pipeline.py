from pathlib import Path
import pandas as pd, sqlite3, json
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"data/raw"; OUT=ROOT/"data/processed"
def main():
    emp=pd.read_csv(RAW/"employee_master.csv",dtype={"employee_id":"string"})
    df=pd.read_csv(RAW/"source_records.csv",dtype={"employee_id":"string","record_id":"string"})
    for x in (emp,df):
        for c in x.select_dtypes(include="object").columns:
            x[c]=x[c].astype("string").str.strip().replace({"":pd.NA})
    issues=[]
    def add(mask,code,detail):
        for _,r in df[mask].iterrows():
            issues.append({"record_id":r.get("record_id"),"employee_id":r.get("employee_id"),
                           "source_system":r.get("source_system"),"issue_code":code,"issue_detail":detail})
    add(df["record_id"].duplicated(keep=False),"DUPLICATE_RECORD_ID","record_id is not unique")
    add(~df["employee_id"].isin(emp["employee_id"]),"UNKNOWN_EMPLOYEE","employee_id absent from master")
    add(df["record_date"].isna(),"MISSING_RECORD_DATE","record_date is blank")
    add(df["metric_value"].isna() | (df["metric_value"]<0),"INVALID_METRIC_VALUE","metric_value missing or negative")
    add(~df["source_system"].isin(["HRIS","LMS","Finance","Procurement","CRM"]),"UNKNOWN_SOURCE","source_system not in approved source list")
    exc=pd.DataFrame(issues).drop_duplicates()
    # Quarantine rows with blocking issues. Retain a separate exception log for remediation.
    bad_ids=set(exc.loc[exc.issue_code.isin(["DUPLICATE_RECORD_ID","UNKNOWN_EMPLOYEE","MISSING_RECORD_DATE","INVALID_METRIC_VALUE","UNKNOWN_SOURCE"]),"record_id"].dropna())
    clean=df[~df["record_id"].isin(bad_ids)].copy()
    clean=clean.merge(emp[["employee_id","department","region","country","active_flag"]],on="employee_id",how="left",validate="many_to_one")
    clean.to_csv(OUT/"validated_reporting_records.csv",index=False)
    exc.to_csv(OUT/"data_quality_exceptions.csv",index=False)
    summary={"source_rows":int(len(df)),"validated_rows":int(len(clean)),"exception_rows":int(len(exc)),
      "duplicate_record_ids":int(df.record_id.duplicated(keep=False).sum()),
      "unknown_employee_rows":int((~df.employee_id.isin(emp.employee_id)).sum()),
      "missing_record_date_rows":int(df.record_date.isna().sum()),
      "invalid_metric_rows":int((df.metric_value.isna()|(df.metric_value<0)).sum()),
      "unknown_source_rows":int((~df.source_system.isin(["HRIS","LMS","Finance","Procurement","CRM"])).sum()),
      "note":"Synthetic demonstration data; blocked rows are quarantined, not silently discarded."}
    (OUT/"quality_summary.json").write_text(json.dumps(summary,indent=2))
    con=sqlite3.connect(OUT/"reporting_quality.db")
    emp.to_sql("employee_master",con,index=False,if_exists="replace")
    clean.drop(columns=["department","region","country","active_flag"]).to_sql("reporting_records",con,index=False,if_exists="replace")
    exc.to_sql("data_quality_exceptions",con,index=False,if_exists="replace")
    con.close()
    print(json.dumps(summary,indent=2))
if __name__=="__main__": main()
