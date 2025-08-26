import json
from load_employee import load_employee
from validity import email_valid,dob_valid,name_valid
from loguru import logger
def update_employee(fp,emp_id,update_data):
    employees=load_employee(fp)
    try:
        for emp in employees:
            if emp["emp_id"] == emp_id:
                logger.info(f"Attempting to update employee details with ID{emp_id}")
                if "8" in update_data.keys():
                    logger.info(f"Update cancel with employee ID {emp_id}")
                    return 1
                for key,value in update_data.items():
                    if key=="name":
                        emp["name"] = value
                        if not name_valid(emp["name"]):
                            logger.error(f"Invalid name format entered during update for for employee ID {emp_id}:{emp["name"]}")
                            return 1
                        logger.info(f"Updated name for employee ID {emp_id}")
                    if key=="email":
                        emp["email"] =value          
                        if not email_valid(emp["email"]):
                            logger.error(f"Invalid email format entered during update for employee ID {emp_id}: {emp['email']}")
                            
                            return 1
                        logger.info(f"Updated email for employee ID {emp_id}")
                    if key=="salary":
                        emp["salary"] = float(value)
                        if emp["salary"] < 0:
                            logger.error(f"Negative salary entered during update for employee ID {emp_id}: {emp['salary']}")
                         
                            return 1
                        logger.info(f"Updated salary for employee ID {emp_id}")
                    if key=="address":
                        emp["address"] = value
                        logger.info(f"Updated address for employee ID {emp_id}")
                    if key=="dob":
                        emp["dob"] = value
                        if not dob_valid(emp["dob"]):
                            logger.error(f"Invalid DOB format entered during update for employee ID {emp_id}: {emp['dob']}")
                            return 1
                        logger.info(f"Updated dob for employee ID {emp_id}")
                    if key=="department":
                        emp["department"] = value
                        logger.info(f"Updated department for employee ID {emp_id}")
                    
                
                with open(fp, "w") as f:
                    json.dump(employees, f, indent=4)
                logger.success(f"Successfully updated the details of employee with ID{emp_id}")
                return 0
        logger.error(f"Employee with ID {emp_id} not found during updating operation.")
        return -1
    except ValueError:
        logger.error("Invalid input while reading operation.")
        