from pymongo import AsyncMongoClient
import os
from dotenv import load_dotenv,find_dotenv
from displayAll import displayAll
import pytest
async def get_test_db():
    load_dotenv(find_dotenv())
    password=os.environ.get("MongoDB_password")
    connection_string=f"mongodb+srv://durba028:{password}@tuitorial.s0vgcnr.mongodb.net/"
    client=AsyncMongoClient(connection_string)
    db=client["test_employee_db"]
    return db,client

async def set_up_collections(db):
    await db.employee.delete_many({})
    initial_data=initial_data = [{
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
    
    await db.employee.insert_many(initial_data)

@pytest.mark.asyncio
async def test_display():
  db,client=await get_test_db()
    
  await set_up_collections(db)
  res=await displayAll(db)
  assert await db.employee.count_documents({})==3
  assert res[0]["name"]=="Alice"
  assert res[1]["name"]=="John"
  assert res[2]["name"]=="Bob"
  assert res[0]["department"]=="IT"
  assert res[1]["department"]=="Finance"
  assert res[2]["department"]=="HR"
  await client.drop_database("test_employee_db")
