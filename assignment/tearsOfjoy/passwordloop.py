''''
  
set the value of password inside a variable

set the value of count

if count is 3 it breaks







'''


count=0

password= "python123"




while count<4:
    user=input("enter the password")
    if user==password:
        print("Access granted")
        break
    elif user!=password:
        print("Wrong")
        count+=1
        if count==3:
            break
    
