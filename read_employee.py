from load_employee import load_employee
import json
from loguru import logger

def read_employee(fp,emp_id=-1):
    emp=load_employee(fp)
    try:
        if emp_id==-1:
            logger.info("Reading all employee records.")
            return emp
        else:   
            for c in emp:  
                if c["emp_id"]==emp_id:
                    logger.info(f"Reading employee record with ID: {emp_id}")
                    return c
           
            logger.error(f"Employee with ID {emp_id} not found during reading operation.")
            return None
                
    except ValueError:
        logger.error("Invalid input while reading operation.")