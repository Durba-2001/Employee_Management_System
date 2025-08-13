from print_separator import print_separator
def menu2():
 
   print_separator("Employee Management System")
   print("1.Add Employee")
   print("2.Read Employee")
   print("3.Update Employee")
   print("4.Delete Employee")
   print("5.Display All Employees")
   print("6.View logs")
   print("7.Exit")
   ch=int(input("Enter your choice:: "))
   return ch
#menu2()