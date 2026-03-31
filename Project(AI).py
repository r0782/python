import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)

def add_student():
    students = load_students()
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    student = {"name": name, "roll": roll}
    students.append(student)
    save_students(students)
    print("Student added.")

def view_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for idx, s in enumerate(students, 1):
        print(f"{idx}. Name: {s['name']}, Roll: {s['roll']}")

def update_student():
    students = load_students()
    view_students()
    idx = int(input("Enter student number to update: ")) - 1
    if 0 <= idx < len(students):
        name = input("Enter new name: ")
        roll = input("Enter new roll number: ")
        students[idx] = {"name": name, "roll": roll}
        save_students(students)
        print("Student updated.")
    else:
        print("Invalid student number.")

def delete_student():
    students = load_students()
    view_students()
    idx = int(input("Enter student number to delete: ")) - 1
    if 0 <= idx < len(students):
        students.pop(idx)
        save_students(students)
        print("Student deleted.")
    else:
        print("Invalid student number.")

def main():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()