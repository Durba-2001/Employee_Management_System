from add_employee import add_employee
from read_employee import read_employee
from update_employee import update_employee
from delete_employee import delete_employee
from displayAll import display
from print_separator import print_separator
from menu2 import menu2
from loguru import logger
from take_input import take_input
from menu import menu
import json
def main():
    
    logger.add("emp.log")
    print("-"*50)
    file=input("Enter the file_path:: ")
    print("-"*50)
    print("-"*50)
    print("\U0001F4CD Welcome to Employee Management System")	
    print("-"*50)
    while True:
        ch=menu2()
        match ch:
            case 1:
                print_separator("Add Employee")
                logger.info("Selecting ADD employee option.")
                emp_data=take_input()
                r=add_employee(file,emp_data)
                if r==0:
                    read_employee(file,emp_data["emp_id"])
                
            case 2:  
                print_separator("Read Employee")    
                logger.info("Selecting READ employee option.")  
                ch=input("Do you want all employees record?(y/n):: ")
                if ch.lower()=="y":
                    emp=read_employee(file)
                    for e in emp:
                        print(json.dumps(e,indent=4))
                else:
                    emp_id=int(input("Enter Employee Id:: ")) 
                    e=read_employee(file,emp_id)
                    print(json.dumps(e,indent=4))
                
            case 3:
                print_separator("Update Employee")
                logger.info("Selecting UPDATE employee option.")
                emp_id=int(input("Enter Employee ID to update:: "))
                read_employee(file,emp_id)
                ch=menu()
                choices = ch.split(",")
                update_data={}
                for i in choices:
                    if i == "1" or i=="7":
                        update_data["name"] = input("Enter new name:: ")
                    if i == "2" or i=="7":
                         update_data["email"] = input("Enter new email:: ")
                    if i == "3" or i=="7":
                         update_data["salary"] = input("Enter new salary:: ")
                    if i == "4" or i=="7":
                         update_data["address"] = input("Enter new address:: ")
                    if i == "5" or i=="7":
                         update_data["dob"] = input("Enter new dob:: ")
                    if i == "6" or i=="7":
                         update_data["department"] = input("Enter new department:: ")
                    if i<"1" or i>"8":
                        logger.error(f"Invalid update choice entered for employee ID: {emp_id}")
                        
                        return 1
                if update_data:
                    r=update_employee(file,emp_id,update_data)
                    if r==0:
                        print("After updating Employee Details:: ")
                        e=read_employee(file,emp_id)
                        print(json.dumps(e,indent=4))

                
            case 4:
                print_separator("Delete Employee")
                logger.info("Selecting DELETE employee option.")
                emp_id=int(input("Enter Employee ID to delete:: "))
                print("Employee Details:: ")
                e=read_employee(file,emp_id)
                print(json.dumps(e,indent=4))
                confirm=input("Are you sure you want to delete this employee? ")
                if confirm.lower()=="y":
                    res=delete_employee(file,emp_id)
                    if res==0:
                         print("Employee deleted successfully.")
                    else:
                        logger.info(f"Deletion failed for Employee ID {emp_id}")
                else: 
                    logger.info(f"Deletion cancelled for Employee ID {emp_id}")
                
            case 5:
                print_separator("Display All Employees")
                logger.info("Selecting Display all employee option.")
                emp=display(file)
                for e in emp:
                    print(json.dumps(e,indent=4))
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
                print("Exiting....")
                exit()
            case _:
                logger.error(f"Invalid choice entered.")
                print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__=="__main__":
    main()