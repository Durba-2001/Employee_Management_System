import json
from load_employee import load_employee
from validity import email_valid,dob_valid
from menu import menu
def update_employee(fp):
    employees,file=load_employee(fp)
    try:
        emp_id=int(input("Enter Employee ID to update:: "))
        for emp in employees:
            if emp["emp_id"]==emp_id:
                print("Current Employee Details:: ")
                print(json.dumps(emp,indent=4))
                ch=menu()
                if ch == "8":
                    print("Update cancelled.")
                    return

                choices = ch.split(",")

                for i in choices:
                    if i == "1" or i=="7":
                        emp["name"] = input("Enter new name:: ")
                    if i == "2" or i=="7":
                        emp["email"] = input("Enter new email:: ")
                        if not email_valid(emp["email"]):
                            print("Invalid email Format!!")
                            return
                    if i == "3" or i=="7":
                        emp["salary"] = float(input("Enter new salary:: "))
                        if emp["salary"] < 0:
                            print("Salary must be non negative")
                            return
                    if i == "4" or i=="7":
                        emp["address"] = input("Enter new address:: ")
                    if i == "5" or i=="7":
                        emp["dob"] = input("Enter new DOB:: ")
                        if not dob_valid(emp["dob"]):
                            print("Invalid DOB Format!!")
                            return
                    if i == "6" or i=="7":
                        emp["department"] = input("Enter new department:: ")
                    if i<"1" or i>"8":
                        print("Invalid choice:", i)
                        return
                print("After updating Employee Details:: ")
                print(json.dumps(emp,indent=4))
                with open(file, "w") as f:
                    json.dump(employees, f, indent=4)
                print("Employee details updated successfully!!")
                return

        print("Employee with ID", emp_id, "not found.")

    except ValueError:
        print("Invalid input. Please enter the correct values.")
#update_employee()