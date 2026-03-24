a=int(input("Entre a range: ")) #-------------------> Here The user must enter the number of numbers he wants to determine the average for
sum=0 #-------------------->Empty Varabile for calucating the sum
for i in range(1,a+1): #----------------------> For loop to print the user determined range
    x=int(input(f"Enter your {i}'st number:"))
    sum=sum+x #-------------------> Caluclating the Sum
print("Average of the given numbers",sum/a) #-------------> Caluclating the Average