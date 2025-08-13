from validity import *
from loguru import logger
async def update_employee(db,emp_id,update_data):
  try:
    
    collections=db["employee"]
    emp=await collections.find_one({"emp_id":emp_id})
    if emp:
      logger.info(f"Attempting to update employee with id {emp_id}")
      for key,value in update_data.items():
        if key=="emp_name":
          if not name_valid(value):
            logger.error(f"Invalid Name with Id {emp_id}")
            return False
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_name":value}})
          logger.success(f"Updating name for employee with id {emp_id}")
        if key=="emp_email":
          if not email_valid(value):
            logger.error(f"Invalid Email with Id {emp_id}")
            return False
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_email":value}})
          logger.success(f"Updating email for employee with id {emp_id}")
        if key=="emp_salary":
          salary=float(value)
          if salary<0:
            logger.error(f"Negative Salary entered during update for employee with Id {emp_id}")
            return False
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_salary":salary}})
          logger.success(f"Updating salary for employee with id {emp_id}")
        if key=="emp_address":
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_address":value}})
          logger.success(f"Updating address for employee with id {emp_id}")
        if key=="emp_dob":
          if not dob_valid(value):
            logger.error(f"Invalid DOB with Id {emp_id}")
            return False
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_dob":value}})
          logger.success(f"Updating dob for employee with id {emp_id}")
        if key=="emp_department":
          await collections.update_one({"emp_id":emp_id},{"$set":{"emp_department":value}})
          logger.success(f"Updating department for employee with id {emp_id}")
      logger.success(f"Employee with id {emp_id} updated successfully")
      return True
    logger.error(f"Employee with id {emp_id} not found")
    return False
  except Exception as e:
    logger.error(f"Error updating employee: {e}")
    return False