

def max (number1,number2, number3):
        largest = number1
        if number2>number1:
            largest=number2
        
        elif number3>largest:
              largest=number3
       
        return largest

print(max(2,5,9))
