from loguru import logger


async def read_employee(db,emp_id=-1):
  try:    
    collections=db["employee"]
    if emp_id==-1:
      logger.info("Reading all employees")
      employees = []
      async for emp in collections.find():
        employees.append(emp)
      return employees
      
    else:
      emp=await collections.find_one({"emp_id":emp_id})
      if emp:
        logger.info(f"Reading employee with id {emp_id}")
        return emp
      else:
        logger.error(f"Employee with id {emp_id} not found")
        return None
  except Exception as e:
    logger.error(f"Error reading employee: {e}")
