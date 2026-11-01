import unittest, pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class QualityTests(unittest.TestCase):
 def test_master_ids_unique(self):
  d=pd.read_csv(ROOT/'data/raw/employee_master.csv'); self.assertTrue(d.employee_id.is_unique)
 def test_source_has_demo_exceptions(self):
  d=pd.read_csv(ROOT/'data/raw/source_records.csv')
  self.assertTrue((d.metric_value<0).any())
  self.assertTrue(d.record_date.isna().any())
  self.assertTrue(d.record_id.duplicated().any())
 def test_reference_ids(self):
  e=pd.read_csv(ROOT/'data/raw/employee_master.csv'); d=pd.read_csv(ROOT/'data/raw/source_records.csv')
  self.assertTrue((~d.employee_id.isin(e.employee_id)).any())
if __name__=='__main__': unittest.main()
