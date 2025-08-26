import json
from update_employee import update_employee

def set_upfile(temp_path):
  initial_data=[
      {"emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"}
  ]
  file=temp_path/"emp.json"
  file.write_text(json.dumps(initial_data))
  return file

def test_update_name(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"name":"Alicia"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["name"]=="Alicia"

def test_update_email(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"email":"alicia@gmail.com"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["email"]=="alicia@gmail.com"

def test_update_salary(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"salary":70050}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["salary"]==70050

def test_update_address(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"address":"xyz street"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["address"]=="xyz street"

def test_update_dob(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"dob":"17-08-2000"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["dob"]=="17-08-2000"

def test_update_department(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"department":"HR"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["department"]=="HR"

def test_update_namesalary(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"name":"Alicia",
    "salary":70050}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["name"]=="Alicia"
  assert updated[0]["salary"]==70050

def test_update_emailsalary(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"email":"alicia@gmail.com",
    "salary":70050}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["email"]=="alicia@gmail.com"
  assert updated[0]["salary"]==70050

def test_update_dobsalary(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"dob":"17-08-2000",
    "salary":70050}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["dob"]=="17-08-2000"
  assert updated[0]["salary"]==70050

def test_update_deptsalary(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"department":"HR",
    "salary":70050}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["department"]=="HR"
  assert updated[0]["salary"]==70050

def test_update_Addresssalary(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"address":"xyz street",
    "salary":70050}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["address"]=="xyz street"
    assert updated[0]["salary"]==70050

def test_update_nameemail(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"name":"Alicia",
    "email":"alicia@gmail.com"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["name"]=="Alicia"
    assert updated[0]["email"]=="alicia@gmail.com"

def test_update_namedob(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"name":"Alicia",
    "dob":"17-06-1999"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["name"]=="Alicia"
    assert updated[0]["dob"]=="17-06-1999"

def test_update_namedept(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"name":"Alicia",
    "department":"IT"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["name"]=="Alicia"
    assert updated[0]["department"]=="IT"

def test_update_nameaddress(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"name":"Alicia",
    "address":"abc colony"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["name"]=="Alicia"
    assert updated[0]["address"]=="abc colony"

def test_update_emaildob(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"email":"alicia@gmail.com",
    "dob":"17-08-2000"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["email"]=="alicia@gmail.com"
  assert updated[0]["dob"]=="17-08-2000"

def test_update_emaildept(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"email":"alicia@gmail.com",
    "department":"HR"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["email"]=="alicia@gmail.com"
  assert updated[0]["department"]=="HR"

def test_update_emailaddress(tmp_path):
  file=set_upfile(tmp_path)
  emp_id=1
  update_data={"email":"alicia@gmail.com",
    "address":"abc street"}
  res=update_employee(str(file),emp_id,update_data)
  updated=json.loads(file.read_text())
  assert res==0
  assert updated[0]["email"]=="alicia@gmail.com"
  assert updated[0]["address"]=="abc street"

def test_update_Addressdob(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"address":"xyz street",
    "dob":"17-08-2000"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["address"]=="xyz street"
    assert updated[0]["dob"]=="17-08-2000"

def test_update_Addressdept(tmp_path):
    file=set_upfile(tmp_path)
    emp_id=1
    update_data={"address":"xyz street",
    "department":"HR"}
    res=update_employee(str(file),emp_id,update_data)
    updated=json.loads(file.read_text())
    assert res==0
    assert updated[0]["address"]=="xyz street"
    assert updated[0]["department"]=="HR"

def test_update_dobdept(tmp_path):
   file=set_upfile(tmp_path)
   emp_id=1
   update_data={"dob":"20-04-1996", "department": "IT"}
   res=update_employee(str(file),emp_id,update_data)
   updated=json.loads(file.read_text())
   assert res==0
   assert updated[0]["dob"]=="20-04-1996"
   assert updated[0]["department"]=="IT"

def test_wrong_id(tmp_path):
    file = set_upfile(tmp_path)
    emp_id = 3  # Not in file
    update_data = {"name": "unknown"}
    res = update_employee(str(file), emp_id, update_data)
    assert res == -1

def test_update_all(tmp_path):
   file=set_upfile(tmp_path)
   emp_id=1
   update_data={ "name":"Alicia",
      "email":"alicia@gmail.com",
      "salary":70050,
      "address":"xyz street",
      "dob":"20-04-1996", 
      "department": "IT"
   }
   res=update_employee(str(file),emp_id,update_data)
   updated=json.loads(file.read_text())
   assert res==0
   assert updated[0]["name"]=="Alicia"
   assert updated[0]["email"]=="alicia@gmail.com"
   assert updated[0]["salary"]==70050
   assert updated[0]["address"]=="xyz street"
   assert updated[0]["dob"]=="20-04-1996"
   assert updated[0]["department"]=="IT"

def test_update_namesalarydept(tmp_path):
   file=set_upfile(tmp_path)
   emp_id=1
   update_data={
      "name":"Alicia",
      "salary":70050,
      "department": "IT"
   }
   res=update_employee(str(file),emp_id,update_data)
   updated=json.loads(file.read_text())
   assert res==0
   assert updated[0]["name"]=="Alicia"
   assert updated[0]["salary"]==70050
   assert updated[0]["department"]=="IT"

def test_wrong_name(tmp_path):
    file = set_upfile(tmp_path)
    emp_id = 1 
    update_data = {"name": "Alicia123"}
    res = update_employee(str(file), emp_id, update_data)
    assert res == 1

def test_wrong_email(tmp_path):
    file = set_upfile(tmp_path)
    emp_id = 1 
    update_data = {"name": "Alicia","email":"alicia@example"}
    res = update_employee(str(file), emp_id, update_data)
    assert res == 1
    updated=json.loads(file.read_text())

    assert updated[0]["name"] != "Alicia"

def test_wrong_dob(tmp_path):
    file = set_upfile(tmp_path)
    emp_id = 1 
    update_data = {"name": "Alicia","dob":"2000-04-17"}
    res = update_employee(str(file), emp_id, update_data)
    assert res == 1
    updated=json.loads(file.read_text())

    assert updated[0]["name"] != "Alicia"

def test_update_namesalarydeptdob(tmp_path):
   file=set_upfile(tmp_path)
   emp_id=1
   update_data={
      "name":"Alicia",
      "salary":70050,
      "department": "IT",
      "dob":"18-09-2000"
   }
   res=update_employee(str(file),emp_id,update_data)
   updated=json.loads(file.read_text())
   assert res==0
   assert updated[0]["name"]=="Alicia"
   assert updated[0]["salary"]==70050
   assert updated[0]["department"]=="IT"
   assert updated[0]["dob"]=="18-09-2000"