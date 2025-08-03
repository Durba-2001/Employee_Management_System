from load_employee import load_employee
import json

def read_employee(fp):
    emp,_=load_employee(fp)
    try:  
        ch=input("Do you want all employees record?(y/n):: ")
        if ch.lower()=="y":
            for e in emp:
              print(json.dumps(e,indent=4))
        else:
            flag=0 
            emp_id=int(input("Enter Employee Id:: "))  
            for c in emp:
                
                if c["emp_id"]==emp_id:
                    print("\nEmployee Details:: ")
                    print(json.dumps(c,indent=4))
                    flag=1
                    break
            if(flag==0):
                print("Employee Details not found!!!")
    except ValueError:
        print("Invalid input.Please Enter the correct value...")
#read_employee(emp_id)