#Employee Information System
Name=input("Enter Employee Name: ")
print(f"Data Type: {type(Name)}")
Id=int(input("Enter Employee ID: "))
print(f"Data Type: {type(Id)}")
Salary=float(input("Enter Salary: "))
print(f"Data Type: {type(Salary)}")
Department=input("Enter Department: ")
print(f"Data Type: {type(Department)}")
Active=input("Is the employee active? (yes/no): ").lower() =="yes"
print(f"Data Type: {type(Active)}")

print("--- Employee Details ---")
print(f"Name       : {Name}")
print(f"ID         : {Id}")
print(f"Salary     : {Salary}")
print(f"Department : {Department}")
print(f"Active     : {Active}")