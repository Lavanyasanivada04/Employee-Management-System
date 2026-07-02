print("===== Employee Management System =====")

employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        employees.append(name)
        print("✅ Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            print("\nEmployee List:")
            for employee in employees:
                print("-", employee)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
