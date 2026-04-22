

''''

collect the input of the user
set the count to 1 as that is where factorial will stop

also set a variable that will store the values for factorial by multiplying through it

the loop will run as long as the number is greater than or equal to count

then decrement it

print result



set the while condition to be less than or equal to 1


'''''


user_input=int(input("enter the number:"))

count=1
factorial=1

while user_input>=count:
   
    factorial*=user_input
    
    user_input-=1

print(f"Fcatorial:{factorial}")



