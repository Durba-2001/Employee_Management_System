import json 
from load_employee import load_employee
from validity import email_valid,dob_valid,name_valid
from loguru import logger


def add_employee(fp,emp_data):
    employees=load_employee(fp)
    try:  
        emp_id=emp_data["emp_id"]
        for e in employees:
            if e["emp_id"]==emp_id:
                logger.warning(f"Attempting to add existing employee with ID{emp_id}")
                return True
        name=emp_data["name"]
        if not name_valid(name):
            logger.error(f"Invalid Name format entered for employee ID{emp_id} : {name}")   
            return False
        email=emp_data["email"]
        if not email_valid(email):
            logger.error(f"Invalid email format entered for employee ID{emp_id} : {email}")   
            return False
        salary=emp_data["salary"]
        if salary<0:
            logger.error(f"Negative salary entered for employee ID{emp_id} : {salary}")
            return False
      
        dob=emp_data["dob"]
        if not dob_valid(dob):
            logger.error(f"Invalid DOB format entered for employee ID{emp_id} : {dob}")
    
            return False    
        employees.append(emp_data)
        with open(fp,"w") as f:
            json.dump(employees,f,indent=4)
        logger.success(f"Successfully added new employee with id :: {emp_id}")
        
        return True
    except ValueError:
        logger.error("Invalid input during add operation.")
        