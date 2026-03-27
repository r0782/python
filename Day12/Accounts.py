import json
import random
data={}
def save():
    with open("data.json","w") as file:
        json.dump(data,file)
def load():
    global data
    try:
        with open("data.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        data={}
class Accounts:
    def __init__(self,accountnumber,accountHolderName):
        self.accountnumber=accountnumber
        self.accountHolderName=accountHolderName
class Customerdata(Accounts):
    def displaymethod(self):
        balance=random.randint(1000,90000)
        print("Account Number :", self.accountnumber)
        print("Name Of Account Holder:",self.accountHolderName)
        print("Balance In Account:",balance)
class currentAccount(Customerdata):
    def datadisplay(self):
        balance=random.randint(10000,1000000)
        print("Account Number :", self.accountnumber)
        print("Balance:",balance)
load()
while True:
    A=Customerdata(input("Enter Account Number: "),
              input("Enter Name of the Account Holder: ")
              )
    data[A.accountnumber]={
        "accountnumber":A.accountnumber,
        "accountholder":A.accountHolderName
    }
    A.displaymethod()
    userchoice = input("Enter another person details(Y/N): ")
    if userchoice == "N":
        break


save()

