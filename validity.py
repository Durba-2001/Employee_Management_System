import re
def email_valid(email):
    pattern=r"^\w+@\w.+\.com$"
    e=re.match(pattern,email)
    return e

def dob_valid(dob):
    pattern=r"^\d{2}-\d{2}-\d{4}$"
    d=re.match(pattern,dob)
    return d