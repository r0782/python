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
                print("Answer:",Number1+Number2)
            elif UserChoice =="2":
                print("Answer:",Number1-Number2)
            elif UserChoice =="3":
                print("Answer:",Number1/Number2)
            elif UserChoice =="4":
                print("Answer:",Number1*Number2)
        except:
            print("Invalid Input!, Please check the given input")
    else:
        print("Invalid choice.Please select from the range of 1 to 5")

