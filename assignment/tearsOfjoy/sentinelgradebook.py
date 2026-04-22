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
    
