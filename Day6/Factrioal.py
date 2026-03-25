def factorial(x):
    product=1
    count=1
    for i in range(x):
        product=product*count
        count=count+1
    return product
Number=int(input("Enter a number:"))
result=factorial(Number)
print("factorial of the given number is:",result)
