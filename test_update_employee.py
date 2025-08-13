import os
from pymongo import AsyncMongoClient
from dotenv import find_dotenv,load_dotenv
from update_employee import update_employee
import pytest

async def get_test_db():
    load_dotenv(find_dotenv())
    password=os.environ.get("MongoDB_password")
    connection_string=f"mongodb+srv://durba028:{password}@tuitorial.s0vgcnr.mongodb.net/"
    client=AsyncMongoClient(connection_string)
    db=client["test_employee_db"]
    return db,client

async def set_up_collections(db):
  db.employee.delete_many({})
  initial_data = [{
    "emp_id": 1, "name": "Alice", "email": "alice@example.com", "salary": 50000,
         "address": "123 A St", "dob": "01-01-1990", "department": "IT"      
  },
  {
      "emp_id": 2, "name": "John", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"
  }
                  ]
  await db.employee.insert_many(initial_data)

@pytest.mark.asyncio
async def test_update_name():
  db,client= await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_email():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_email":"alicia@gmail.com"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_email"]=="alicia@gmail.com"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_salary():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_address():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_address":"xyz street"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_address"]=="xyz street"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_dob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_dob":"17-08-2000"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_dob"]=="17-08-2000"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_department():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_department":"HR"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_department"]=="HR"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_namesalary():
  db,client= await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia",
    "emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_emailsalary():
  db,client= await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_email":"alicia@gmail.com",
    "emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_email"]=="alicia@gmail.com"
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_dobsalary():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_dob":"17-08-2000",
    "emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_dob"]=="17-08-2000"
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_deptsalary():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_department":"HR",
    "emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_department"]=="HR"
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_Addresssalary():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_address":"xyz street",
    "emp_salary":70050}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_address"]=="xyz street"
  assert updated["emp_salary"]==70050
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_nameemail():
  db,client= await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia",
    "emp_email":"alicia@gmail.com"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_email"]=="alicia@gmail.com"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_namedob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia",
    "emp_dob":"17-06-1999"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_dob"]=="17-06-1999"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_namedept():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia",
    "emp_department":"IT"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_department"]=="IT"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_nameaddress():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_name":"Alicia",
    "emp_address":"abc colony"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_address"]=="abc colony"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_emaildob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_email":"alicia@gmail.com",
    "emp_dob":"17-08-2000"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_email"]=="alicia@gmail.com"
  assert updated["emp_dob"]=="17-08-2000"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_emaildept():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_email":"alicia@gmail.com",
    "emp_department":"HR"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_email"]=="alicia@gmail.com"
  assert updated["emp_department"]=="HR"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_emailaddress():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_email":"alicia@gmail.com",
    "emp_address":"abc street"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_email"]=="alicia@gmail.com"
  assert updated["emp_address"]=="abc street"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_Addressdob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_address":"xyz street",
 "emp_dob":"17-08-2000"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_address"]=="xyz street"
  assert updated["emp_dob"]=="17-08-2000"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_Addressdept():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_address":"xyz street",
    "emp_department":"HR"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_address"]=="xyz street"
  assert updated["emp_department"]=="HR"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_dobdept():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={"emp_dob":"20-04-1996", "emp_department": "IT"}
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_dob"]=="20-04-1996"
  assert updated["emp_department"]=="IT"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_wrong_id():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id = 3  
  update_data = {"emp_name": "unknown"}
  res = await update_employee(db, emp_id, update_data)
  assert res is False
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_all():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={ "emp_name":"Alicia",
       "emp_email":"alicia@gmail.com",
       "emp_salary":70050,
       "emp_address":"xyz street",
       "emp_dob":"20-04-1996", 
       "emp_department": "IT"
    }
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_email"]=="alicia@gmail.com"
  assert updated["emp_salary"]==70050
  assert updated["emp_address"]=="xyz street"
  assert updated["emp_dob"]=="20-04-1996"
  assert updated["emp_department"]=="IT"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_namesalarydept():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={
       "emp_name":"Alicia",
       "emp_salary":70050,
       "emp_department": "IT"
    }
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_salary"]==70050
  assert updated["emp_department"]=="IT"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_wrong_name():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id = 1 
  update_data = {"emp_name": "Alicia123"}
  res = await update_employee(db, emp_id, update_data)
  assert res is False
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_wrong_email():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id = 1 
  update_data = {"emp_email":"alicia@example"}
  res = await update_employee(db, emp_id, update_data)
  assert res is False
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_wrong_dob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id = 1 
  update_data = {"emp_name": "Alicia","emp_dob":"2000-04-17"}
  res = await update_employee(db, emp_id, update_data)
  assert res is False
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert updated["name"] != "Alicia"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_update_namesalarydeptdob():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  update_data={
      "emp_name":"Alicia",
       "emp_salary":70050,
       "emp_department": "IT",
       "emp_dob":"18-09-2000"
    }
  res=await update_employee(db,emp_id,update_data)
  updated=await db.employee.find_one({"emp_id":emp_id})
  assert res is True
  assert updated["emp_name"]=="Alicia"
  assert updated["emp_salary"]==70050
  assert updated["emp_department"]=="IT"
  assert updated["emp_dob"]=="18-09-2000"
  await client.drop_database("test_employee_db")