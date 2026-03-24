import random
attempts=0
max_attempts=5
score=50
Number=int(input("Enter a end range number:"))
r=random.randrange(1,Number+1)
while True:
     userinput=int(input("Guess the number:"))
     if attempts<max_attempts:
        if userinput<r:
            print("False(Your guess is lower than number Try again)")
            attempts=attempts+1
            score=score-10
        elif userinput>r:
            print("False(Your guess is higher than number Try again)")
            attempts=attempts+1
            score=score-10
        elif userinput == r:
            print("Congrats.You guessed the number")
            print("Attempts taken to guess the number",attempts)
            print("Player score:",score)
            break
           