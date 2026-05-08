"""


4.3 (What’s Wrong with This Code?) What is wrong with the following cube function’s definition?
def cube(x):

Calculate the cube of x
 x ** 3
print('The cube of 2 is', cube(2))



Answer: 
The function calculates the math (x ** 3), but it is missing the 'return' 
keyword. Because it doesn't return the result, the function will just hand back 
'None' when called. 


"""
