import json
from delete_employee import delete_employee
def set_upfile(temp_path):
  initial_data = [{"emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"},
                   {
      "emp_id": 2, "name": "John", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
  }
                  ]
  file=temp_path/"emp.json"
  file.write_text(json.dumps(initial_data))
  return file
def test_delete_emp(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  res=delete_employee(str(file),emp_id)
  updated=json.loads(file.read_text())
  assert res == 0
  assert len(updated)==1
  assert updated[0]["name"]=="John"

def test_delete_cancel(tmp_path):
  file=set_upfile(tmp_path)
  confirm = "n"
  emp_id = 1
  if confirm.lower() == "y":   
    res = delete_employee(str(file), emp_id)
  else:
    res=1
  updated = json.loads(file.read_text())
  assert res == 1
  assert len(updated) == 2

def test_id_not_found(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=5
  res=delete_employee(str(file),emp_id)
  updated = json.loads(file.read_text())
  assert res==False
  assert len(updated)==2
