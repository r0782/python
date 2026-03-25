def addition(x,y):
    a=x+y
    return a
def subtraction(x,y):
    b=x-y
    return b
def multipilaction(x,y):
    c=x*y
    return c
def division(x,y):
    d=x/y
    return d
while True:
    print(" Calculator Menu ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4.Multiply")
    print("5. Exit")
    UserChoice=input("Enter the number from 1-5 to do the operation:")
    if UserChoice=="5":
        print("Stoping the process")
        break
    if UserChoice in ["1","2","3","4"]:
        try:
            Number1=float(input("Enter the number: "))
            Number2=float(input("Enter the another number:"))
            if UserChoice=="1":
                result=addition(Number1,Number2)
                print("Answer:",result)
            elif UserChoice =="2":
                result=subtraction(Number1-Number2)
                print("Answer:",result)
            elif UserChoice =="3":
                result=division(Number1,Number2)
                print("Answer:",result)
            elif UserChoice =="4":
                result=multipilaction(Number1,Number2)
                print("Answer:",result)
        except:
            print("Invalid Input!, Please check the given input")
    else:
        print("Invalid choice.Please select from the range of 1 to 5")