# Implementation notes
- Raw CSVs are immutable source snapshots for this demo.
- The pipeline uses explicit validation rules and writes an exception register.
- Records with blocking exceptions are quarantined from the validated output.
- Before production deployment, agree source-specific business rules, acceptable tolerances, PII access controls, retention, refresh cadence, and issue ownership.
- Power BI Desktop is required to create the final PBIX report using the included model and design guide.
