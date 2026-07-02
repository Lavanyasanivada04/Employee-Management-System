print("Employee Management System")

employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        employees.append(name)
        print("Employee Added Successfully!")

    elif choice == "2":
        print("\nEmployees:")
        for employee in employees:
            print(employee)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
