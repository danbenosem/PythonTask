"""
DECLARE VARIBLE

collect price from the user

IF price matches the PRICE RANGE.
CALCULATE DISCOUNT

PRINT DISCOUNT


END




"""


user_input= int(input("Enter the price:"))

if user_input>1000 and user_input<10000:
    print("you have 5% discount")
    discount_price= 0.05 * user_input
    final_discount= user_input- discount_price
    print (f"discount price  is {final_discount}")

elif user_input>10000 and user_input<50000:
    print("you have 10% discount")
    discount= 0.10 * user_input
    final_discount= user_input- discount_price
    print (f"discount price  is {final_discount}")

elif user_input>50000:
     print("you have 20% discount")
     discount= 0.20 * user_input
     final_discount= user_input- discount_price
     print (f"discount price  is {final_discount}")













