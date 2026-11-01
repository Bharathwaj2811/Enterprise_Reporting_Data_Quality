![Uploading image.png…]()
# Enterprise Reporting Automation & Data Quality Monitoring System

**Portfolio project | Python + SQL + Power BI + PowerPoint**

A synthetic enterprise reporting pipeline demonstrating multi-source consolidation, data validation, reconciliation, exception management, operational reporting, and stakeholder-ready analytics. It is designed around the responsibilities of a Reporting & Analytics Support analyst.

> Independent portfolio work. All data is synthetic; it is not affiliated with Any Company and contains no real employee or client information.

## Business scenario
A global organization receives recurring structured extracts from HRIS, LMS, Finance, Procurement, and CRM. The reporting team needs reliable consolidated outputs, clear validation rules, traceable exceptions, and management reporting.

## Included
- 600 synthetic employee master records and 5,000+ source records.
- Deliberate demo defects: duplicate IDs, unknown employee references, missing dates, negative metrics, unknown source systems.
- Python ETL and exception register.
- SQLite database and analytical SQL.
- Power BI DAX measures, model and dashboard build guide.
- PowerPoint executive reporting pack.
- Unit tests and sample output files.

## Folder structure
`data/raw` source extracts; `data/processed` validated data, exception log, SQLite DB and quality summary; `src` Python pipeline; `sql` schema and queries; `powerbi` DAX and build guide; `powerpoint` stakeholder deck; `tests` automated checks.

## Run
Python 3.10+ recommended.
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/quality_pipeline.py
python -m unittest discover -s tests -v
```
Outputs:
- `data/processed/validated_reporting_records.csv`
- `data/processed/data_quality_exceptions.csv`
- `data/processed/quality_summary.json`
- `data/processed/reporting_quality.db`

## SQL
Open the SQLite database with DB Browser for SQLite. Queries in `sql/analytics_queries.sql` provide source volume, department/source reconciliation, daily trends, and pending review records.

## Power BI
Follow `powerbi/POWER_BI_BUILD_GUIDE.md`. Import validated records and exception log; create date table and measures from the DAX files. `.pbix` is not included because native report authoring requires Power BI Desktop.

## Controls and KPI definitions
- Quality pass rate = validated rows / (validated rows + exception rows). This is a portfolio-level proxy; in production define row-level vs issue-level denominator carefully.
- Exception rows = distinct exception-register records after deduplication.
- Reconciliation = compare source-level row counts and metric totals against validated warehouse outputs.
- Blocking defects are quarantined for remediation, not silently deleted.

## Interview positioning
Explain the pipeline as a controlled reporting workflow: ingest -> standardize -> validate -> quarantine -> load -> visualize -> reconcile -> communicate. Describe why you preserve raw inputs, document rules, and escalate ambiguous data definitions.
