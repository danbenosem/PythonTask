

"""
define a varible digit

set a container that will collect the digit from back

find a way to collect last digit and collect from a container

continue

till it gets zero


"""
number=12345

new_digit=0
while number>0:
    new_digit= (new_digit*10)+ (number%10)
    number//=10

print(new_digit)
    

    
