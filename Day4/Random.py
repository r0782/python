import random
Number=int(input("Enter a end range number:"))
r=random.randrange(1,Number+1)
while True:
    userinput=int(input("Guess the number:"))
    if userinput<r:
        print("False(Your guess is lower than number Try again)")
    elif userinput>r:
        print("False(Your guess is higher than number Try again)")
    elif userinput == r:
        print("Congrats.You guessed the number")
        break
