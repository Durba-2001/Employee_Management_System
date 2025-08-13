import os
from pymongo import AsyncMongoClient
from dotenv import find_dotenv,load_dotenv
from read_employee import read_employee
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
async def test_read_employee():
  db,client=await get_test_db()
  await set_up_collections(db)
  emp_id=1
  res = await read_employee(db,emp_id)
  assert res["name"]=="Alice"
  assert res["email"]=="alice@example.com"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_read_all_employees():
  db,client= await get_test_db()
  await set_up_collections(db)
  res = await read_employee(db)
  assert await db.employee.count_documents({}) == 2
  assert res[0]["name"]=="Alice"
  assert res[1]["name"]=="John"
  assert res[0]["department"]=="IT"
  assert res[1]["department"]=="Finance"
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_wrong_id():
  db,client=await get_test_db()
  emp_id=3
  res=await read_employee(db,emp_id)
  assert res==None
  await client.drop_database("test_employee_db")