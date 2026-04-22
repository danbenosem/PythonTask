''''
  

import random
genrate random number

use it in a loop to compare with condition

print required result



'''


import random
number= random.randint(1,100)


while True:
    guess_num= int(input("enter guess:"))

    if guess_num < number:
        print("lower")
    elif guess_num>number:
        print("higher")

    else:
        print("correct")
