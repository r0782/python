import json
students=[]
def save():
    with open("Student.json","w") as file:
        json.dump(students,file,indent=4)
def load():
    global students
    try:
        with open("Student.json","r") as file:
            students=json.load(file)
    except FileNotFoundError:
        students = []
class Student:
    def __init__(self, name, age, roll_no, section, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.section = section
        self.marks = marks
class System:
    def add_student(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        roll_no = input("Enter roll number: ")
        section = input("Enter section: ")
        n = int(input("Enter number of subjects: "))
        marks = []
        for i in range(n):
            m = int(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)
        student = Student(name, age, roll_no, section, marks)
        students.append(student.__dict__)
    def update_student(self):
        roll_no = input("Enter roll number of student to update: ")
        for s in students:
            if s["roll_no"] == roll_no:
                print("Student found. Enter new details.")
                s["name"] = input("Enter student name: ")
                s["age"] = int(input("Enter student age: "))
                s["section"] = input("Enter section: ")
                n = int(input("Enter number of subjects: "))
                marks = []
                for i in range(n):
                    m = int(input(f"Enter marks for subject {i+1}: "))
                    marks.append(m)
                s["marks"] = marks
                print("Student updated successfully.")
                return
        print("Student not found.")
    def delete_student(self):
        roll_no = input("Enter roll number of student to delete: ")
        for s in students:
            if s["roll_no"] == roll_no:
                students.remove(s)
                print("Student deleted successfully.")
                return
        print("Student not found.")
    def display_students(self):
        if not students:
            print("No students found.")
            return
        for s in students:
            print(f"Name: {s['name']}, Age: {s['age']}, Roll No: {s['roll_no']}, Section: {s['section']}, Marks: {s['marks']}")
load()
system = System()
while True:
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        system.add_student()
        save()
    elif choice == "2":
        system.update_student()
        save()
    elif choice == "3":
        system.delete_student()
        save()
    elif choice == "4":
        system.display_students()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
save()