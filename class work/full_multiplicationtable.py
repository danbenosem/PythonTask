







for number in range(0  ,10):
    
        if number==0:
            print("  ",end="")
            print(f"| ",end="\t ")
        else:
 
            print(number,end=" ")
            print(f"| ",end="")
    
        for number2 in range (1,10):
            if number*number2==0:
                for number3 in range(1,10):
                    if number3==2:
                        break;
                    print(number3,end=" ")
               
            else:
            
                print(f"{number*number2}",end="\t")
            
            
            
            
        
        print( )
   
