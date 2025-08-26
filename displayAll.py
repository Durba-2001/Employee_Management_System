import json
from load_employee import load_employee
from loguru import logger
def display(fp):
    emp=load_employee(fp)
    logger.info("Displaying all employee records.")
    return emp
