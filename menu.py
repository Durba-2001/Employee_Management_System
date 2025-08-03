from print_separator import print_separator
def menu():
  print_separator("Which field you want to update?")
  print("1.Name")
  print("2.Email")
  print("3.Salary")
  print("4.Address")
  print("5.DOB")
  print("6.Department")
  print("7.All Fields")
  print("8.cancel")
  ch = input("Enter your choice(s) (comma-separated for multiple):: ")
  return ch