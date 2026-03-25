def grade(x):
    if x>=90:
        return("A")
    elif x>=75:
        return("B")
    elif x>=50:
        return("C")
    else:
        return "Fail"
while True:
    print("------Enter the student details------")
    Name=input("Enter the name of the student:")
    RollNo=int(input("Enter the rollno:"))
    marks=[]
    Subjects=int(input("Enter no of subjects:"))
    for i in range(Subjects):
        m=int(input(f"Enter marks for subject{i+1}:"))
        marks.append(m)
    total=sum(marks)
    avg=total/Subjects
    Grade=grade(avg)
    print(marks)
    print(f"The Grade of student containing roll no of {RollNo} is {Grade}" )
    UserChoice=input("Close the programe (Y/N): ")
    if UserChoice=="Y":
        break
