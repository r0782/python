def palindrom(x):
    if x[:]==x[::-1]:
        return("It is a palindrom")
UserInput=input("Enter a word:")
result=palindrom(UserInput)
print(result)