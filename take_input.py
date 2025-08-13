def take_input():
    
    emp_name = input("Enter Employee Name:: ")
    email = input("Enter Employee email:: ")
    salary = float(input("Enter Employee Salary:: "))
    address = input("Enter Employee address:: ")
    dob = input("Enter employee date of birth:: ")
    department = input("Enter employee department:: ")
    new_emp = {
    
        "emp_name": emp_name,
        "emp_email": email,
        "emp_salary": salary,
        "emp_address": address,
        "emp_dob": dob,
        "emp_department": department
    }
    return new_emp