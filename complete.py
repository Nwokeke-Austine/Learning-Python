# Student Management System

students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nEnter Student Details")

        name = input("Student Name: ")
        matric = input("Matric Number: ")
        department = input("Department: ")
        level = input("Level: ")

        student = {
            "Name": name,
            "Matric Number": matric,
            "Department": department,
            "Level": level
        }

        students.append(student)

        print("Student record added successfully!")

    elif choice == "2":
        print("\n===== STUDENT RECORDS =====")

        if len(students) == 0:
            print("No student records available.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"\nStudent {i}")
                print("Name:", student["Name"])
                print("Matric Number:", student["Matric Number"])
                print("Department:", student["Department"])
                print("Level:", student["Level"])

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")