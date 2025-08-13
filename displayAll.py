
from loguru import logger
async def displayAll(db):
  
  collections=db["employee"]
  employees = []
  logger.info("Displaying all employees")
  async for emp in collections.find():  
     employees.append(emp)
  return employees
