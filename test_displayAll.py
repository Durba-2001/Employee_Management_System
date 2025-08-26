import json
from displayAll import display

def set_upfile(temp_path):
  initial_data = [{
    "emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"      
  },
  {
      "emp_id": 2, "name": "John", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
  },
  {
      "emp_id": 3, "name": "Bob", "email": "bob@example.com", "salary": 60000,
        "address": "467 C st", "dob": "05-06-1985", "department": "HR"
  }]
  file=temp_path/"emp.json"
  file.write_text(json.dumps(initial_data))
  return file

def test_display(tmp_path):
  file=set_upfile(tmp_path)
  res=display(str(file))
  assert len(res)==3
  assert res[0]["name"]=="Alice"
  assert res[1]["name"]=="John"
  assert res[2]["name"]=="Bob"
  assert res[0]["department"]=="IT"
  assert res[1]["department"]=="Finance"
  assert res[2]["department"]=="HR"
