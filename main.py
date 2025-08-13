from add_employee import create_employee
from read_employee import read_employee
from update_employee import update_employee
from delete_employee import delete_employee
from displayAll import displayAll
from print_separator import print_separator
from menu2 import menu2
from loguru import logger
from menu import menu
from take_input import take_input
from load_employee import get_db
import asyncio
def display(emp):
       print("-"*40)
       print("ID         :",emp["emp_id"])
       print("Name       :",emp["emp_name"])
       print("Salary     :",emp["emp_salary"])
       print("Email      :",emp["emp_email"])
       print("Address    :",emp["emp_address"])
       print("DOB        :",emp["emp_dob"])
       print("Department :",emp["emp_department"])
       print("-"*40)

async def main(): 
    db,client=await get_db()

    logger.add("emp.log")
    print("-"*50)
    print("-"*50)
    print("\U0001F4CD Welcome to Employee Management System")	
    print("-"*50)
    while True:
        ch=menu2()
        match ch:
            case 1:
                print_separator("Add Employee")
                logger.info("Selecting Add Employee Option")
                emp=take_input()
                r= await create_employee(db,emp)
                if r:
                   e= await read_employee(db,emp["emp_id"])
                   display(e)
            case 2:
                print_separator("Read Employee")
                logger.info("Selecting Read Employee Option")
                ch=input("Do you want all employee records?(y/n) ")
                
                if ch.lower()=="y":
                    emp=await read_employee(db)
                    if emp:
                        for e in emp:
                            display(e)
                        
                else:
                    emp_id=int(input("Enter Employee Id:"))
                    emp=await read_employee(db,emp_id)
                    if emp:
                        logger.info(f"Reading employee with id {emp_id}")
                        display(emp)
            case 3:
                print_separator("Update Employee")
                logger.info("Selecting UPDATE employee option.")
                emp_id=int(input("Enter Employee ID to update:: "))
                emp=await read_employee(db,emp_id)
                display(emp)
                ch=menu()
                choices=ch.split(",")
                if "8" in choices:
                    logger.info(f"Update cancelled for employee with id {emp_id}")
                    continue
                update_data={}
                for i in choices:
                  if i=="1" or i=="7":
                    update_data["emp_name"]=input("Enter new name:")
                  if i=="2" or i=="7":
                    update_data["emp_email"]=input("Enter new email:")
                  if i=="3" or i=="7":
                    update_data["emp_salary"]=float(input("Enter new salary:"))
                  if i=="4" or i=="7":
                    update_data["emp_address"]=input("Enter new address:")
                  if i=="5" or i=="7":
                    update_data["emp_dob"]=input("Enter new dob:")
                  if i=="6" or i=="7":
                    update_data["emp_department"]=input("Enter new department:")
                  if i<"1" or i>"8":
                    logger.error("Invalid choice")
                    return False
                if update_data:
                  
                  res=await update_employee(db,emp_id,update_data)
                  if res:
                    logger.success("Employee updated successfully.")
                    emp=await read_employee(db,emp_id)
                    display(emp)
                  else:
                    logger.error(f"Update failed for Employee ID {emp_id}")

            case 4:
                print_separator("Delete Employee")
                logger.info("Selecting Delete Employee Option")
                emp_id=int(input("Enter Employee Id:"))
                emp_data=await read_employee(db,emp_id)
                if emp_data:
                     print("\nEmployee Record:")
                     display(emp_data)
                     ch=input(f"Are you sure you want to delete the employee with Id {emp_id}? ")  
                     if ch.lower()=="y":
                        res=await delete_employee(db,emp_id)
                        if res:
                         logger.success("Employee deleted successfully.")
                        else:
                            logger.error(f"Deletion failed for Employee ID {emp_id}")
                     else: 
                        logger.info(f"Deletion cancelled for Employee ID {emp_id}")
                else:
                   logger.error(f"No employee found with id{emp_id}")
                    

                
            case 5:
                print_separator("Display All Employees")
                logger.info("Selecting Display all employee option.")
                emp=await displayAll(db)
                for e in range(len(emp)):
                      display(emp[e])
            case 6:
                print_separator("Viewing logs")
                logger.info("Selecting View log option.")
                try:
                    with open("emp.log","r") as fp:
                        for line in fp.readlines():
                            print(line)
                except FileNotFoundError:
                    pass

            case 7:
                logger.info("Exiting from the application.")
                await client.close()
                logger.info("MongoDB connection closed.")
                exit()
                
            case _:
                logger.error(f"Invalid choice entered.")
           

        input("Press Enter to continue...")

if __name__=="__main__":
    asyncio.run(main())