contacts={}
def Contacts():
    while True:
        x=input("Enter Contact Name: ")
        y=input("Enter Contact Number: ")
        contacts[x]=y
        print(contacts)
        print("Do you want to create another new contact ? (Y/N): ")
        userinput=input("enter:")
        if userinput=="N":
            break
    return contacts

while True:
    print("Enter a operation to perfome: ")
    print("1. Create Contact")
    print("2. Search Contact")
    print("3.Exit")
    userchoice=input("enter the choice: ")
    if userchoice=="1":
        Contacts()
    elif userchoice=="2":
        name=input("Enter the contact name: ")
        if name in contacts:
            print(name,contacts[name])
        else:
            print("Contact not found")
    elif userchoice=="3":
        break

