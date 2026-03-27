import json

studentdata = {}

def save():
    with open("student.json", "w") as file:
        json.dump(studentdata, file)

def load():
    global studentdata
    try:
        with open("student.json", "r") as file:
            studentdata = json.load(file)
    except FileNotFoundError:
        studentdata = {}

class Person:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def detailsdisplay(self):
        print("Name:", self.name)
        print("PhoneNumber:", self.number)
        print("Email:", self.email)

load()

while True:
    p1 = Person(
        input("Enter name: "),
        input("Enter phone number: "),
        input("Enter email: ")
    )
    studentdata[p1.name] = {
        "number": p1.number,
        "email": p1.email
    }

    p1.detailsdisplay()

    userchoice = input("Enter another person details(Y/N): ")
    if userchoice == "N":
        break


save()

print("Contacts saved successfully!")