"""
collect input from the user
set a container
multiply each number through that container, then decrement

continue until the condition is mer

"""

number= int(input("Enter the number"))


factorial=1
while number>1:
    factorial= factorial * number
    number-=1

print(factorial)
