-- Source volume by system
SELECT source_system, COUNT(*) record_count FROM reporting_records GROUP BY source_system ORDER BY record_count DESC;

-- Reconciliation by department and system
SELECT e.department, r.source_system, COUNT(*) records,
       COUNT(DISTINCT r.employee_id) employees, ROUND(SUM(r.metric_value),2) metric_total
FROM reporting_records r JOIN employee_master e USING(employee_id)
GROUP BY e.department,r.source_system;

-- Data quality exception counts (run against exceptions export)
-- Python ETL creates typed exception register with issue_code and record_id.

-- Daily reporting trend
SELECT record_date, COUNT(*) records, ROUND(SUM(metric_value),2) metric_total
FROM reporting_records GROUP BY record_date ORDER BY record_date;

-- Records requiring review
SELECT * FROM reporting_records
WHERE status IN ('Pending','Open') ORDER BY updated_at;
