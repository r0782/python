def EvenOrOdd(x):
    if x%2==0:
        return("Even")
    else:
        return("Odd")
UserInput=int(input("Enter a number:"))
result=EvenOrOdd(UserInput)
print("Given number is a",result,"number")