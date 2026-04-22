		
"""
collect the number from the user

using 10000,1000,100, 10, units format

trying to get the separate digits  and compare the first and last digit to see if palindrome

"""


number = int(input("Enter a 5-digit integer: "))

digit_one = number // 10000        
digit_two = number // 1000 % 10   
digit_three= number // 100 % 10    
digit_four = number // 10 % 10     
digit_five = number % 10           

if digit_one == digit_two: 
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
