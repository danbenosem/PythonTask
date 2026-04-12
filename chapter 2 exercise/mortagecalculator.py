principal = int(input("enter the principal amount:"))

annual_rate = int(input("enter the annual interest rate:"))

years = int(input("enter the duration in years :"))

rate = (annual_rate/100)/12

duration= years*12


monthly=principal * (rate*((1+rate)**duration)) /   ((1+rate)**duration -1) 


print("Your monthly payment is:$",round(monthly,2))
