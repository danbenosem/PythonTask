def product(*numbers):
   
    total = 1 
    
    for num in numbers:
        total = total * num
        
    return total


print("Product of 2 and 3 is:", product(2, 3))
print("Product of 2, 3, and 4 is:", product(2, 3, 4))
print("Product of 5, 2, 10, and 2 is:", product(5, 2, 10, 2))
