'''''

define failure counter
define pass counter 


collect grade from the teacher

set a while loop condition to continue running if the condition is true

if pass increment counter

if fail increment counter for failure


print the counter






'''


fail_count=0
pass_count=0
print("to end the program press 0")
user_input=0
while user_input!=-1:
    user_input = int(input("Enter the value integer:"))
    if user_input==0:
        user_input=-1
    elif user_input==1:
        pass_count+=1
    elif user_input==2:
        fail_count+=2
    else:
         user_input = int(input("Enter the value integer:"))

print(f"the number of pass rate is {pass_count}, the number of failure rate is {fail_count}")
