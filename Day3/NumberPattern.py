Number=int(input("Enter a number:"))
for i in range(1,Number+1):
    if i==1:
        print(" "*(Number-i)+str(i),)
    else:
        print(" "*(Number-i),end="")
        for j in range(1,i+1):
            print(str(j)+" ",end="")
        print()

