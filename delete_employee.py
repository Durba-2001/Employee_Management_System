import json
from load_employee import load_employee
from loguru import logger
def delete_employee(fp,emp_id):
    employees=load_employee(fp)
    try:
        
        for emp in employees:
            if emp["emp_id"]==emp_id:
                logger.info(f"Attempting to delete employee with ID:: {emp_id}")
                employees.remove(emp)
                with open(fp,"w") as f:
                     json.dump(employees,f,indent=4)
                logger.success(f"Employee with ID {emp_id} deleted succesfully")   
                return 0
        logger.error(f"Employee with ID{emp_id} not found during deleting operation.")
        return False
    except ValueError:
        logger.error("Invalid input while reading operation.")
        