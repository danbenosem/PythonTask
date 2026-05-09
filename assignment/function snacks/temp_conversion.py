# receive the value with the unit beside it and the treshold
#
# in my head i am like we have to distingiush between farhenhit and celsius
#
# so we loop through the string in order to get the unit either C or F
#
# then find a way to get the digits
#
# convert them to integer 
#
# compare with the treshold
#
# return the output after comparison
#








def temperature_conversion(temp,treshold):

    digit=""
    unit=""

    for index in  range (len(temp)):
        char=temp[index].upper()
        if char=='C':
            unit='C'
            digit= temp[:index]
            break;
        elif char=='F':
            unit='F'
            digit= temp[:index]
            break;

    new_value= int(digit)
    if unit=='C':
        converted_temp =(new_value-32)*(5/9)
        
      
    elif unit=='F':
         converted_temp=(new_value*5/9) + 32


    if converted_temp < treshold:
        return "Cold advisory"

    elif converted_temp >= treshold:
        return "Heat alert"


    
