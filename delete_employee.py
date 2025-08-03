import json
from load_employee import load_employee
def delete_employee(fp):
    employees,file=load_employee(fp)
    try:
        emp_id=int(input("Enter the Employee ID to delete:: "))
        for emp in employees:
            if emp["emp_id"]==emp_id:
                print("Employee Details:: ")
                print(json.dumps(emp,indent=4))
                confirm=input("Are you sure you want to delete this employee?(Y/N) ")
                if confirm.upper()=="Y":
                    employees.remove(emp)
                    with open(file,"w") as f:
                        json.dump(employees,f,indent=4)
                    print("Employee deleted successfully!!")
                    return
                else:
                    print("Deletion cancelled.")
                    return
        print("Employee with ID",emp_id,"not found.")
    except ValueError:
        print("Invalid input. Please enter the correct values.")
#delete_employee()