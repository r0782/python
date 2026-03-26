import json #-----------------> importing json(javaScript object Notation)
Contacts={} #------------------> Dictionary
def save(): #-------------------> save function
    with open("contacts.json","w") as file:#-----------> Here it opens that "Contacts.json file" if it exists it overwrite that old one ,if it don't exist it create a new one with that name 
        #---> "w" is for write mode for that file
        #---> "with open() it is a saftey method to handle the file operations.It acts as "context manager{Context manager is an object which provides a neat way to automatically set up and clean up resources}".
        #---> In a short form when we open a file by using "with open()" it ensure proper release even if errors occur.
        json.dump(Contacts,file)  #---->Here "json.dump()" is json method which converts python objects into json string.
def load():#----->Load function
    global Contacts #----> making "Contancts" global inside the function.
    #WHY GLOBAL?----->when we make it global it changes the original varabile.{python by default creates a local varabile and when we run those the local varabile will be updated not the original one}
    try:#-----------------------------------------
        with open("contacts.json","r") as file: #|---------- "r" read mode and it is used to open files for reading 
            Contacts=json.load(file)            #|------------"json.load(file) this method converts the json string to python dictionary" 
    except FileNotFoundError: #-------------------------------try-except is used for  error handling{when their is a crash instead of prgm crashing we handle error saftely}
        Contacts={}
def contactCreation():#--------contact creating function
    name=input("Enter Name: ")#------- input
    phnNum=input("Enter the phone number: ")
    Contacts[name]=phnNum
    print("Contact added successfully")
def viewingContacts():
    if not Contacts:
        print("Contact doesn't exist")
    else:
        for name,phnNum in Contacts.items():
            print(name,":",phnNum)
def updateContact():
    name=input("Enter the name:")
    if name in Contacts:
        newNumber=input("Enter new mobile number: ")
        Contacts[name]=newNumber
        print("Contact number updated successfully")
    else:
        print("contact doesn't exist")
def deletecontact():
    name=input("Enter the name: ")
    if name in Contacts:
        del Contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact doesn't exist")
def contactSearch():
    search=input("Enter a name: ")
    if search in Contacts:
        print(search, ":" ,Contacts[search])
    else:
        print("Contact doesn't exist")
load()#------------ is used to get back the saved data from the file into this program
while True:
    print("  Menu   ")
    print("Choose a operation to perfome: ")
    print("1.Create a  New Contact")
    print("2.View existing contacts")
    print("3.update a contact")
    print("4.Delete a contact")
    print("5.Search the contact")
    print("6.Exit")
    Userchoice=input("Enter a choice to perfome operation:")
    if Userchoice=="1":
        contactCreation()
    elif Userchoice=="2":
        viewingContacts()
    elif Userchoice=="3":
        updateContact()
    elif Userchoice=="4":
        deletecontact()
    elif Userchoice=="5":
        contactSearch()
    elif Userchoice=="6":
        break


