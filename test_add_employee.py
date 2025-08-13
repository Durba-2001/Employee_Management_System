from pymongo import AsyncMongoClient
import os
from add_employee import create_employee
from dotenv import load_dotenv,find_dotenv
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
    initial_data={
        
        "emp_id": 1,
        "emp_name": "Alice",
        "emp_email": "alice@example.com",
        "emp_salary": 50000,
        "emp_address": "123 A St",
        "emp_dob": "01-01-1990",
        "emp_department": "IT"
    }
    
    await db.employee.insert_one(initial_data)

@pytest.mark.asyncio
async def test_add_employee():
    db,client= await get_test_db()
    
    await set_up_collections(db)
    
    valid_emp = {
        "emp_id": 2, 
        "emp_name": "Bob", 
        "emp_email": "bob@example.com", 
        "emp_salary": 60000,
        "emp_address": "456 B Ave", 
        "emp_dob": "02-02-1982", 
        "emp_department": "HR"
    }
    result_valid = await create_employee(db, valid_emp)
    assert result_valid is True
    added = await db.employee.find_one({"emp_email": "bob@example.com"})
    
    assert added is not None
    
    assert added["emp_name"]=="Bob"
    assert added["emp_email"]=="bob@example.com"
    assert added["emp_salary"]==60000
    assert added["emp_address"]=="456 B Ave"
    assert added["emp_dob"]=="02-02-1982"
    assert added["emp_department"]=="HR"
    await client.drop_database("test_employee_db")

@pytest.mark.asyncio

async def test_invalid_name():
    db,client= await get_test_db()
    await set_up_collections(db)
    
    invalid_emp = {
          "emp_name": "john123", "emp_email": "john@example.com", "emp_salary": 70000,
         "emp_address": "789 C Rd", "emp_dob": "03-03-1985", "emp_department": "Finance"
     }
    
    result_invalid = await create_employee(db,invalid_emp)
    assert result_invalid is False
    
    assert await db.employee.count_documents({}) == 1
    await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_invalid_email():
    db,client= await get_test_db()
    await set_up_collections(db)
    
    invalid_emp = {
          "emp_name": "john", "emp_email": "john@example", "emp_salary": 70000,
         "emp_address": "789 C Rd", "emp_dob": "03-03-1985", "emp_department": "Finance"
     }
    
    result_invalid = await create_employee(db,invalid_emp)
    assert result_invalid is False
    
    assert await db.employee.count_documents({}) == 1
    await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_negative_salary():
    db,client= await get_test_db()
    await set_up_collections(db)
    
    invalid_emp = {
          "emp_name": "john", "emp_email": "john@example.com", "emp_salary": -70000,
         "emp_address": "789 C Rd", "emp_dob": "03-03-1985", "emp_department": "Finance"
     }
    
    result_invalid = await create_employee(db,invalid_emp)
    assert result_invalid is False
    
    assert await db.employee.count_documents({}) == 1
    await client.drop_database("test_employee_db")

@pytest.mark.asyncio
async def test_invalid_dob():
    db,client= await get_test_db()
    await set_up_collections(db)
    
    invalid_emp = {
          "emp_name": "john", "emp_email": "john@example.com", "emp_salary": 70000,
         "emp_address": "789 C Rd", "emp_dob": "1985-08-20", "emp_department": "Finance"
     }
    
    result_invalid = await create_employee(db,invalid_emp)
    assert result_invalid is False
    
    assert await db.employee.count_documents({}) == 1
    await client.drop_database("test_employee_db")