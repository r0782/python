Number=int(input("Enter a number:"))
gap=1
for i in range(1,Number+1):
    if i==1:
        print(" "*(Number-i)+"*")
    elif i==Number:
        print("* "*Number)
    else:
        print(" "*(Number-i)+"*"+" "*gap+"*")
        gap=gap+2