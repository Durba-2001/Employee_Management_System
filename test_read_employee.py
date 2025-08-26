import json
from read_employee import read_employee

def set_upfile(temp_path):
  initial_data = [{
    "emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"      
  },
  {
      "emp_id": 2, "name": "John", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
  }
                  ]
  file=temp_path/"emp.json"
  file.write_text(json.dumps(initial_data))
  return file

def test_read_employee(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  res = read_employee(str(file),emp_id)
  assert res["name"]=="Alice"
  assert res["email"]=="alice@example.com"

def test_read_all_employees(tmp_path):
  file=set_upfile(tmp_path)
  res = read_employee(str(file))
  assert len(res)==2
  assert res[0]["name"]=="Alice"
  assert res[1]["name"]=="John"
  assert res[0]["department"]=="IT"
  assert res[1]["department"]=="Finance"

def test_wrong_id(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=3
  res=read_employee(str(file),emp_id)
  assert res==None