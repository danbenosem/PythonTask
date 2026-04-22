







for number in range(-1  ,10):
        if number==-1:
            print(" ",end=" ")
    
        elif number==0:
            print("  ",end="")
           
            print(f"_____ ",end="")
            print("_____",end="")
        elif number==1:
            print()
            print(number,end=" ")
            print(f"| ",end="\t")
        else:
            
            print(number,end=" ")
            print(f"| ",end="\t")
    
        for number2 in range (1,10):
            if number==-1:
                print(" ",end=" ")
                print(" ",end=" ")
                print(" ",end=" ")
                print(number2,end=" ")
                
                    
            elif number*number2==0:
                    
                    print("________",end=" ")
                    
               
            else:
            
                print(f"{number*number2}",end="\t")
            
            
            
            
        
        print( )
   
