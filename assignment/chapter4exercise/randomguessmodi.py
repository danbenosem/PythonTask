import random	

number=random.randrange(1,1001)
count=1
input_number=int(input("enter the guess:"))
while(input_number!=number):
    count+=1
    
    if(input_number<number):
        print("lower than the guess")
  

    if(input_number>number):
        print("higher than the guess")

    input_number=int(input("enter the guess:"))



print("the number of guesses are",count)
