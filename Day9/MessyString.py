print("Want to see a magic trick!. Give me a messy string and i conevrt it into Neat one: ")
x=input("Give me a messy  String: ")
print("Select one of the secret option :")
print("1.Magic TrickNo1")
print("2.Magic TrickNo2")
print("3.Magic TrickNo3")
userchoice=input("Enter the option you want: ")
if userchoice=="1":
    NeatString=x.title()
    print(NeatString)
elif userchoice=="2":
    print(x.upper())
elif userchoice=="3":
    print(x.lower())