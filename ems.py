employees = {}

def Add_Employee(emp_id, name, age, department, salary):
    if emp_id in employees:
        print("Employee Already Exists! Please use a different Employee ID.")
        return 
    else:
        employees[emp_id] = {
            "Name": name,
            "Age": age,
            "Department": department,
            "Salary": salary
        }
        print("Employee Added Successfully!")


def display_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)

    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['Name']}\t{details['Age']}\t"
              f"{details['Department']}\t\t{details['Salary']}")

def search_employees(emp_id):
    if emp_id in  employees:
        print (f"Employee ID is : {emp_id}")
        print (f"Name of Employee is : {employees[emp_id]['Name']}")
        print (f"Age of Employee is : {employees[emp_id]['Age']}")
        print (f"Department of Employee is : {employees[emp_id]['Department']}")
        print (f"Salary of Employee is : {employees[emp_id]['Salary']}")
    else:
        print("Employee Not Found!")

def main_menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            department = input("Enter Employee Department: ")
            salary = float(input("Enter Employee Salary: "))
            Add_Employee(emp_id,name,age,department,salary)
            
        elif choice == '2':
            display_employees()
            
        elif choice == '3':
            emp_id = int (input("Enter Employee ID to Search the Employee: "))
            search_employees(emp_id)
            
        elif choice == '4':
            print("Exiting....")
            break
        else:
            print("Invalid choice! Please select between 1 to 4.")
main_menu()
