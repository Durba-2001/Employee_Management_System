import json
import os
def load_employee(file):
    if os.path.exists(file):
        with open(file,"r") as f:
            data=json.load(f)
            return data,file
    else:
        return [],file


        

