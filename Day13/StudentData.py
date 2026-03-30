import json
students = []
def load():
    global students
    try:
        with open("Student.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []

def save():
    with open("Student.json", "w") as file:
        json.dump(students, file, indent=4)

load()

while True:
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    section = input("Enter section: ")

    n = int(input("Enter number of subjects: "))
    marks = []

    for i in range(n):
        m = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(m)

    student = {
        "name": name,
        "roll": roll,
        "section": section,
        "marks": marks
    }

    students.append(student)

    choice = input("Add another? (Y/N): ")
    if choice.upper() == "N":
        break

save()

print("\nStored Students Data:")
for s in students:
    print(s)
'''''
def save():
    with open("Student.json","w") as file:
        json.dump(Student,file)
def load():
    global Student
    try:
        with open("Student.json","r") as file:
            Student=json.load(file)
    except FileNotFoundError:
        Student={}
class Student:
    def __init__(self,Name,RollNo,Section):
        self.Name=Name
        self.RollNo=RollNo
        self.Section=Section
class Marks(Student):
    def display(self):
        Marks=random.randint(0,100)
        print("Name of the Student : ",self.Name)
        print("Roll No :",self.RollNo)
        print("Section : ",self.Section)
        NoOfSubjects=int(input("Enter no of subjects student enrolled :"))
        for i in range(1,NoOfSubjects+1):
            x=input(f"Enter marks of Subject{i} : ")
load()
while True:
    S=Marks(input("Enter the name of the student : "),
            input("Enter the roll no : "),
            input("Enter section :"))
    Student[S.Name]={"Student Name ": S.Name,"Student Roll No": S.RollNo,"Student Section ":S.Section}
    S.display()
    userchoice = input("Enter another student details(Y/N): ")
    if userchoice == "N":
        break
'''
save()

            
