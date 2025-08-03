import json 
from load_employee import load_employee
from validity import email_valid,dob_valid


def add_employee(fp):
    employees,file=load_employee(fp)
    try:
        emp_id=int(input("Enter the Employee Id:: "))
        for e in employees:
            if e["emp_id"]==emp_id:
                print("Employee Already Exists")
                return
        name=input("Enter Employee Name:: ")
        email=input("Enter Employee email:: ")
        if not email_valid(email):
            print("Invalid email Format!!")
            return
        salary=float(input("Enter Employee Salary:: "))
        if salary<0:
            print("Salary must be non negative")
            return
        address=input("Enter Employee address:: ")
        dob= input("Enter employee date of birth:: ")
        if not dob_valid(dob):
            print("Invalid DOB Format!!")
            return
        department =input("Enter employee department:: ")
        new_emp={
            "emp_id":emp_id,
            "name":name,
            "email":email,
            "salary":salary,
            "address":address,
            "dob":dob,
            "department":department 
        }
        employees.append(new_emp)
        with open(file,"w") as f:
            json.dump(employees,f,indent=4)
        print("New Employee added successfully!!")
        return emp_id
    except ValueError:
        print("Invalid input. Please enter the correct values.")
#add_employee()