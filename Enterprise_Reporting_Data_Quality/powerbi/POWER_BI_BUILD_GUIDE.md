# Power BI build guide
1. Run `python src/quality_pipeline.py`.
2. Import `data/processed/validated_reporting_records.csv` and `data/processed/data_quality_exceptions.csv`.
3. Import `data/raw/employee_master.csv` as Employee dimension if preferred; for the validated file, department and region are already denormalized.
4. Add Calendar table from `calendar_table.dax`; relate Calendar[Date] to validated_reporting_records[record_date].
5. Add measures from `measures.dax` (adjust table names if renamed).
## Pages
- Executive Reporting: KPI cards for record count, metric total, distinct employees, quality pass rate; daily trend; source-system volume; department split.
- Data Quality Controls: exception count by issue, exception detail table, quality pass rate, trend by source if exception date is added.
- Source Reconciliation: source system x department matrix, metric totals, row counts, pending/open review queue.
- Operational Detail: searchable record table with source, date, employee, metric, value, status.
## Design controls
16:9 canvas, clear titles and units, consistent date filters, source labels, refresh timestamp, synthetic-data disclaimer. Test slicer interactions, totals against SQL, and drill-through.
