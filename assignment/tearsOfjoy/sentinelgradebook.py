""""
two sentinel loops means one outer and one inner'

outer will ask for name but stop when blank


inner will ask for score but will stop when -1

add upp all scores and calculate average

print



"""


while True:

    student_name= input("Enter your name:")


        if name=="":
            break

    total=0
    count=0
    score=0
    while score!=-1:
        score= int(input("Enter score:"))

        if score==-1:
            break

        total+=score
        count+=1

        average= total/count
        print(f"{name}, {average}")
    
