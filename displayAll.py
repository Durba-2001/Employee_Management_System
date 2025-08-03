import json
from load_employee import load_employee
def display(fp):
    emp,_=load_employee(fp)
    for e in emp:
        print(json.dumps(e,indent=4))
#display("employees.json")