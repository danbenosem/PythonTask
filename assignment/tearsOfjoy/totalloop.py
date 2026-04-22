
""'''


declare varible for largest set to zero

do a loop to keep asking the user for numbers

use if statement for that stop

then typecast the user input if it is numbers

them compare to largest



""'''

largest=0
while True:
    user_input =input("Enter a number or type stop:")
    if user_input=="stop":
         break
        
        
       
    number= int(user_input)
    if number > largest:
        largest=number
    
    

print(largest)

    
