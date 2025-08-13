import re
async def name_valid(name):
    pattern=r"^[a-zA-Z ]+$"
    n=re.match(pattern,name)
    return n
async def email_valid(email):
    pattern=r"^\w+@\w+\.\w+$"
    e=re.match(pattern,email)
    return e

async def dob_valid(dob):
    pattern=r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    d=re.match(pattern,dob)
    return d
