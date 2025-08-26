def take_input():
    emp_id = int(input("Enter the Employee Id:: "))
    emp_name = input("Enter Employee Name:: ")
    email = input("Enter Employee email:: ")
    salary = float(input("Enter Employee Salary:: "))
    address = input("Enter Employee address:: ")
    dob = input("Enter employee date of birth:: ")
    department = input("Enter employee department:: ")
    new_emp = {
        "emp_id": emp_id,
        "name": emp_name,
        "email": email,
        "salary": salary,
        "address": address,
        "dob": dob,
        "department": department
    }
    return new_emp