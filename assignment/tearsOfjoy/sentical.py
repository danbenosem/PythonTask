''''
  



declare variable for total and count and number
set sentinel value

loop through
match the conditions
calculate average and print



'''




total=0





count=0

number=0
while number !=-1:
   
    number=int(input("Enter number,to exit-1:"))
    if number == -1:
        break

    else:
        total+=number 
        count+=1


average= total/count

print(average)
