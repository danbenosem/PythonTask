"""
START
USER ENTER THE PASSWORD
IF password length using the len funtion matches the first condition which is less than 8 
PRINT very weak

ELSE IF password length using the len funtion matches the second condition which is greater than 8 and less than eqaul to 16 
PRINT strong

ELSE IF password length using the len funtion matches the third condition which is greater than 16 
PRINT strong 




"""







password = input("Enter the password:")

if len(password) <8:
    print("very weak")
elif len(password)==8:
    print("weak")

elif  len(password) >=8 and <=16:
    print("strong ")

elif  len(password) >16:
    print(" very strong ")

