from add_employee import add_employee
from read_employee import read_employee
from update_employee import update_employee
from delete_employee import delete_employee
from displayAll import display
from print_separator import print_separator
from menu2 import menu2
def main():
    file=input("Enter the file_path:: ")
    print("-"*50)
    print("\U0001F4CD Welcome to Employee Management System")	
    print("-"*50)
    while True:
        ch=menu2()
        match ch:
            case 1:
                print_separator("Add Employee")
                add_employee(file)
                #read_employee(file)
                
            case 2:
                
                print_separator("Read Employee")
                read_employee(file)
                
            case 3:
                print_separator("Update Employee")
                update_employee(file)
                
            case 4:
                print_separator("Delete Employee")
                delete_employee(file)
                
            case 5:
                print_separator("Display All Employees")
                display(file)
            case 6:
                print("Exiting....")
                exit()
            case _:
                print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__=="__main__":
    main()