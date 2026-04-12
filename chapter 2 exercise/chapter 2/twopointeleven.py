number = int(input('Enter a five-digit integer: '))


digit_one = number // 10000



digit_two = (number % 10000)//1000
 


digit_three=  ((number % 10000)%1000)//100 


digit_four = (((number % 10000)%1000)%100) // 10 


digit_five = (((number % 10000)%1000)%100) % 10 


print(digit_one,"\t", digit_two, "\t",  digit_three,"\t",  digit_four, "\t",   digit_five)
