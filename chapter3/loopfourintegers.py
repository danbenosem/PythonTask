
sum=0
count=0
largest=0
average=0
product=1
smallest=0
for number in range(4):
        user= int(input("Enter the integer"))
        
        count+=1

        sum+=user
        average= sum/count
        product*=user

        if user>largest:
            largest=user

        if user<smallest:
            smallest=user








print(f"the sum is {sum}")
print(f"the average is {average}")
print(f"the product is {product}")
print(f"the largest is {largest}")
print(f"the smallest is {smallest}")
            
            
            
                        



