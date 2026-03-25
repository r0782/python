def ListOperations():
    ListA=[]
    for i in range(5):
       x=input("Enter the elements to the list: ")
       ListA.append(x)
    print(ListA)
    while True:
        print("\n--- MENU ---")
        print("1. Add number")
        print("2. Remove number")
        print("3. Display list")
        print("4. Sort list")
        print("5. Search number")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            num = int(input("Enter number: "))
            ListA.append(num)
            print("Added!")
        elif choice == "2":
          num = int(input("Enter number to remove: "))
          if num in ListA:
            ListA.remove(num)
            print("Removed!")
          else:
            print("Not found!")

        elif choice == "3":
           print("List:", ListA)

        elif choice == "4":
           ListA.sort()
           print("Sorted List:", ListA)

        elif choice == "5":
            num = int(input("Enter number to search: "))
            if num in ListA:
                print("Found at index:", ListA.index(num))
            else:
               print("Not found")
        elif choice == "6":
            print("Program ended")
            break

def TupleOperations():
    temp_list = []

    for i in range(5):
        x = int(input("Enter element: "))
        temp_list.append(x)

    TA = tuple(temp_list)

    while True:
        print("\n--- MENU ---")
        print("1. Add number")
        print("2. Remove number")
        print("3. Display tuple")
        print("4. Sort tuple")
        print("5. Search number")
        print("6. Exit")

        choice = input("Enter choice: ")

        temp_list = list(TA)  # convert to list for operations

        if choice == "1":
            num = int(input("Enter number: "))
            temp_list.append(num)

        elif choice == "2":
            num = int(input("Enter number to remove: "))
            if num in temp_list:
                temp_list.remove(num)
            else:
                print("Not found!")

        elif choice == "3":
            print("Tuple:", TA)

        elif choice == "4":
            temp_list.sort()
            print("Sorted Tuple:", tuple(temp_list))

        elif choice == "5":
            num = int(input("Enter number to search: "))
            if num in TA:
                print("Found at index:", TA.index(num))
            else:
                print("Not found")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

        TA = tuple(temp_list)  # convert back
while True:
    print("On which Collection you want to perfrom Operations:")
    print("1.List")
    print("2.Tupel")
    SelectChoice=input("Enter the choice:")
    if SelectChoice=="1":
        Output=ListOperations()
        print(Output)
    elif SelectChoice=="2":
        Output=TupleOperations()
        print(Output)
       



