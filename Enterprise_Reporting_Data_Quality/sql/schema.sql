PRAGMA foreign_keys=ON;
DROP TABLE IF EXISTS reporting_records;
DROP TABLE IF EXISTS employee_master;
CREATE TABLE employee_master(
 employee_id TEXT PRIMARY KEY, department TEXT, region TEXT, country TEXT,
 business_unit TEXT, hire_date DATE, active_flag INTEGER
);
CREATE TABLE reporting_records(
 record_id TEXT PRIMARY KEY, employee_id TEXT, source_system TEXT, record_date DATE,
 business_unit TEXT, metric_code TEXT, metric_value REAL, currency TEXT,
 status TEXT, updated_at DATE,
 FOREIGN KEY(employee_id) REFERENCES employee_master(employee_id)
);
