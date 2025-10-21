# Student Management System
# Simple Python project using lists and functions

students = []

def add_student(name, roll_no, marks):
    student = {"name": name, "roll_no": roll_no, "marks": marks}
    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
    else:
        for student in students:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")
        print()

def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            print(f"Found: {student['name']} - Marks: {student['marks']}\n")
            return
    print("Student not found!\n")

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll_no = input("Enter roll number: ")
            marks = input("Enter marks: ")
            add_student(name, roll_no, marks)
        elif choice == "2":
            view_students()
        elif choice == "3":
            roll_no = input("Enter roll number to search: ")
            search_student(roll_no)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
