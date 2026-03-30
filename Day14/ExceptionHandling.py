import json
Data=[]
while True:
    Name=input("Enter name of the person : ")
    Email=input("Enter the email : ")
    while True:
        try:
            MobileNum=int(input("Enter the mobile Number : "))
            break
        except:
            print("Enter the digits")
        finally:
            print("Data Saved")
    person={
        "Name":Name,
        "Email":Email,
        "Mobile Number":MobileNum}
    
    Data.append(person)
    userChoice=input("Want to enter another person data(Y/N):")
    if userChoice=="N":
        break
with open("Data.jason","w") as file:
    json.dump(Data,file)
for d in Data:
    print(d)



