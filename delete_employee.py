
from loguru import logger
async def delete_employee(db,emp_id):
  try:
   
    collections=db["employee"] 
    emp = await collections.find_one({"emp_id":emp_id})
    if emp:
      logger.info(f"Attempting to delete employee with id{emp_id}")
      await collections.delete_one({"emp_id":emp_id})
      logger.success(f"Employee with id {emp_id} deleted successfully")
      return True
    
    else:
      logger.error(f"Employee with id {emp_id} not found")
      return False
    
  except Exception as e:
    logger.error(f"Error deleting employee: {e}")
    return False