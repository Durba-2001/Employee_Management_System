import json
from add_employee import add_employee
def set_upfile(temp_path):
   initial_data = [
        {"emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"}
    ]
   file = temp_path / "emp.json"
   file.write_text(json.dumps(initial_data))
   return file

def test_add_employee(tmp_path):
    file = set_upfile(tmp_path)
    valid_emp = {
        "emp_id": 2, "name": "Bob", "email": "bob@example.com", "salary": 60000,
        "address": "456 B Ave", "dob": "02-02-1982", "department": "HR"
    }
    result_valid = add_employee(str(file), valid_emp)

    updated = json.loads(file.read_text())
    added=updated[-1]
    print("Added employees:: ",json.dumps(added,indent=4))
    assert result_valid == True
    assert added["emp_id"]==2
    assert added["name"]=="Bob"
    assert added["email"]=="bob@example.com"
    assert added["salary"]==60000
    assert added["address"]=="456 B Ave"
    assert added["dob"]=="02-02-1982"
    assert added["department"]=="HR"
    
def test_duplicate_employee_id(tmp_path):
    file = set_upfile(tmp_path)
    valid_emp = {
        "emp_id": 2, "name": "Bob", "email": "bob@example.com", "salary": 60000,
        "address": "456 B Ave", "dob": "02-02-1982", "department": "HR"
    }
    invalid_emp = {
        "emp_id": 2, "name": "john", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
    }

    add_employee(str(file), valid_emp)

    updated = json.loads(file.read_text())
    result_invalid = add_employee(str(file), invalid_emp)
    assert result_invalid == True
    updated = json.loads(file.read_text())
    assert len(updated) == 2

def test_invalid_name(tmp_path):
    file = set_upfile(tmp_path)
    
    invalid_emp = {
        "emp_id": 3, "name": "john123", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
    }
    result_invalid = add_employee(str(file), invalid_emp)
    assert result_invalid == False
    updated = json.loads(file.read_text())
    assert len(updated) == 1

def test_invalid_email(tmp_path):
    file = set_upfile(tmp_path)
    invalid_emp = {
        "emp_id": 3, "name": "john", "email": "john@example", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
    }
    result_invalid = add_employee(str(file), invalid_emp)
    assert result_invalid == False
    updated = json.loads(file.read_text())
    assert len(updated) == 1

def test_negative_salary(tmp_path):
    file = set_upfile(tmp_path)
    invalid_emp = {
        "emp_id": 3, "name": "john", "email": "john@example.com", "salary": -70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
    }
    result_invalid = add_employee(str(file), invalid_emp)
    assert result_invalid == False
    updated = json.loads(file.read_text())
    assert len(updated) == 1

def test_invalid_dob(tmp_path):
    file = set_upfile(tmp_path)
    invalid_emp = {
        "emp_id": 3, "name": "john", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "2000-04-28", "department": "Finance"
    }
    result_invalid = add_employee(str(file), invalid_emp)
    assert result_invalid == False
    updated = json.loads(file.read_text())
    assert len(updated) == 1
