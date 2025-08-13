from validity import *
from loguru import logger
from load_employee import get_next_empId

async def create_employee(db,emp):
  try:
   
    collections=db["employee"]
    emp["emp_id"]= await get_next_empId(db)
    existing= await collections.find_one({"emp_id":emp["emp_id"]})
    if existing:
      logger.error(f"Attempting to add already exists employee id: {emp['emp_id']}")
      return False
    if not name_valid(emp["emp_name"]):
      logger.error(f"Input invalid name with id: {emp['emp_id']}")
      return False
    if not email_valid(emp["emp_email"]):
      logger.error(f"Input invalid email with id: {emp['emp_id']}")
      return False
    if not dob_valid(emp['emp_dob']):
      logger.error(f"Input invalid DOB with id: {emp['emp_id']}")
      return False
    await collections.insert_one(emp)
    logger.success("Employee Added successfully")
    return True
  except Exception as e:
    logger.error(f"Error adding employee: {e}")