from pymongo import AsyncMongoClient
from loguru import logger
import os
from dotenv import load_dotenv,find_dotenv
from delete_employee import delete_employee
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
    initial_data=[{
       "emp_id" :1,
        "name": "Alice",
        "email": "alice@example.com",
        "salary": 50000,
        "address": "123 A St",
        "dob": "01-01-1990",
        "department": "IT"
    },{"emp_id":2,"name": "John", "email": "john@example.com", "salary": 70000,
        "address": "789 C Rd", "dob": "03-03-1985", "department": "Finance"}]
    
    await db.employee.insert_many(initial_data)

@pytest.mark.asyncio
async def test_delete_emp():
  db,client=await get_test_db()
    
  await set_up_collections(db)
  emp_id=1
  res= await delete_employee(db,emp_id)
  
  assert res is True
  assert await db.employee.count_documents({}) == 1
  await client.drop_database("test_employee_db")
 
@pytest.mark.asyncio
async def test_delete_cancel():
  db,client=await get_test_db()
    
  await set_up_collections(db)
  confirm = "n"
  emp_id = 1
  if confirm.lower() == "y":   
    res = await delete_employee(db, emp_id)
  else:
    res=False
    logger.error(f"Deletion cancel with employee ID: {emp_id}")
  
  assert res is False
  assert await db.employee.count_documents({}) == 2
  await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_id_not_found():
  db,client=await get_test_db()
    
  await set_up_collections(db)
  emp_id=5
  res=await delete_employee(db,emp_id)
  assert res is False
  assert await db.employee.count_documents({}) == 2
  await client.drop_database("test_employee_db")
