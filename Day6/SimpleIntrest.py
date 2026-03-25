def intrest(P,R,T):
    return((P*R*T)/100)
Principal=float(input("Enter the principal amount:"))
RateOfIntrest=float(input("Enter the rate of intrest:"))
Time=float(input("Entre no of years:"))
SimpleIntrest=intrest(Principal,RateOfIntrest,Time)
print(SimpleIntrest)