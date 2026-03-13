# Function to calculate grade
def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


# Function to add a single student
def add_student(students_list):
    print("--------------------------------")
    name = input("Enter name: ")
    department = input("Enter department: ")
    regno = input("Enter registration number: ")
    level = int(input("Enter level: "))

    while True:
        score = int(input("Enter score: "))
        if 0 <= score <= 100:
            break
        print("Invalid score! Enter between 0 and 100.")

    grade = calculate_grade(score)

    student = {
        "Name": name,
        "Department": department,
        "Registration Number": regno,
        "Level": level,
        "Score": score,
        "Grade": grade
    }

    students_list.append(student)
    print(f"Student {name} added successfully!\n")


# Function to display all students
def display_students(students_list):
    if not students_list:
        print("No students to display!\n")
        return

    print("\n------ STUDENT RECORDS ------")
    for student in students_list:
        print("---------------------------")
        for key, value in student.items():
            print(f"{key}: {value}")


# Function to search a student by registration number
def search_student(students_list):
    regno_search = input("Enter registration number to search: ")
    found = False
    for student in students_list:
        if student["Registration Number"] == regno_search:
            print("\n--- Student Found ---")
            for key, value in student.items():
                print(f"{key}: {value}")
            found = True
            break
    if not found:
        print("Student not found!\n")


# Function to show statistics
def show_statistics(students_list):
    if not students_list:
        print("No students to calculate statistics!\n")
        return

    highest = students_list[0]["Score"]
    lowest = students_list[0]["Score"]
    total = 0

    for student in students_list:
        score = student["Score"]
        total += score
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score

    average = total / len(students_list)

    print("\n------ STATISTICS ------")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")
    print(f"Class Average: {average:.2f}")


# Main Program
def main():
    students_list = []

    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Registration Number")
        print("4. Show Statistics")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(students_list)
        elif choice == "2":
            display_students(students_list)
        elif choice == "3":
            search_student(students_list)
        elif choice == "4":
            show_statistics(students_list)
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


# Run the program
main()