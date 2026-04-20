
print("welcome to the menu section\n")
print("1.  Phone book")
print("2.  Messages")
print("3.  Chat")
print("4.  Call register")
print("5.  Tones")
print("6.  Settings")
print("7.  Call divert")
print("8.  Games")
print("9.  Calculator")
print("10. Remainders")
print("11. Clock")	
print("12. Profiles")
print("13. SIM services")

print("\n")

number=int(input("enter the number for the menu: "))


match number:
    case 1: 
            
            
                print("\nwelcome to the phonebook section\n")
                print("1.  Search")
                print("2.  Service nos")
                print("3.  Add name")
                print("4.  Erase")
                print("5.  Edit")
                print("6.  Assign tone")
                print("7.  Send b card")
                print("8.  Options")
                print("9.  Speed dials")
                print("10. Voice tags \n")
                print("11. to end press 0")
                print("\n")

              
                
                number_one=int(input("Enter the number:"))
                
                if number_one==8:
                    
                        print("\nwelcome to options\n ")
                        
                        print("1. Type of view")
                        print("2. Memory status")
                       
                        print("\n")


            
    case 2:     
                print("\nWELCOME TO THE MESSAGES SECTION\n")

                print("1.  write messages")
                print("2.  inbox")
                print("3.  outbox")
                print("4.  picture messages")
                print("5.  Template")
                print("6.  Smileys")
                print("7.  Message settings")
               

                number_two=int(input("enter the number for the menu :  "))
               
                

               
                if number_two==7:
                    
                        print("welcome to message settings:\n")
                        print("1. Set 1")
                        print("2. Common\n")
                       

                        subnumber_one=int(input("Enter a value:"))
                       
                        if subnumber_one==1:
                           
                                print("Welcome to set options\n")
                                print("1. Message centre number")
                                print("2. Message sent as")
                                print("3. Message validity")
                               
                        elif subnumber_one==2:
                         
                                print("Welcome Common options")
                                print("1. Delivery report")
                                print("2. Reply via same centre")
                                print("3. Character support")
                                print("4. info service")
                                print("5. voice mailbox number")
                                print("6. Service command editor")
                               

    case 3: print("chat")

    case 4:
          
                print("WELCOME TO THE CALL REGISTER SECTION\n")

                print("1.  Missed calls")
                print("2.  Received calls")
                print("3.  Dialled numbers")
                print("4.  Erase recent call list")
                print("5.  Show call duration")
                print("6.  Show call costs")
                print("7.  Call cost settings")
                print("8.  prepaid credit")

                               
                

               
                

                number_four=int(input("Enter either number 5 or 6 or 7 0r 0:"))
               

                if number_four==5:
                  
                        print("\nWelcome to  show call duration\n")
                        print("1. Last call duration")
                        print("2. All calls’ duration")
                        print("3. Received calls’ duration")
                        print("4. Dialled calls’ duration")
                        print("5. Clear timers")
                       

                elif number_four==6:
                  
                        print("\nwelcome to  show call cost\n")
                        print("1. Last call cost")
                        print("2. All calls’ cost")
                        print("3. Clear counters")
                      
                elif number_four==7:
                 
                        print("\nwelcome to call cost settings\n")
                        print("1. Call cost limit")
                        print("2. Show costs in")
                      

    case 5:  
            
          
                print("WELCOME TO THE PHONE TONES SECTION\n")

                print("1.  Ringing tone")
                print("2.  Ringing volume")
                print("3.  Incoming call alert")
                print("4.  Composer")
                print("5.  Message alert tone")
                print("6.  Keypad tone")
                print("7.  Warning and game tones")
                print("8.  Vibrating alert")
                print("9.  Screen saver")
               
               

             
                



    case 6 :

                print("     SETTINGS\n")

                print("1.  Call settings")
                print("2.  Phone settings")
                print("3.  Security settings")
                print("4.  Restore factory settings")
                print("5. to end press 0")
                print("\n")

                number_six=int(input("enter the number:  "))
             
                
               


                
                if number_six==1:
                   
                    
                        print("Welcome to  call settings\n")
                        print("1. Automatic redial")
                        print("2. Speed dialling")
                        print("3. Call waiting options")
                        print("4. Own number sending")
                        print("5. Phone line in use")
                        print("6. Automatic answer 1")
                        print("7. to end press 0")
                        print("\n")

                        subnumber_six=int(input("enter the number:  "))
                      

                if number_six == 2:
                   
                        print("Welcome to phone settings\n")
                        print("1. Language")
                        print("2. Cell info display")
                        print("3. Welcome note")
                        print("4. Network selection")
                        print("5. Lights")
                        print("6. Confirm SIM service actions")
                    
                elif number_six == 3:
                 
                        print("Welcome to security settings\n")

                        
                        print("1. PIN code request")
                        print("2. Call barring service")
                        print("3. Fixed dialling")
                        print("4. Closed user group")
                        print("5. Phone security")
                        print("6. Change access codes")
                      



    case 7: print("call divert")

    case 8: print("Games")

    case 9: print ("Calulator")

    case 10: print ("Reminders")



    case 11:
          

                print("     CLOCK\n")

                print("1.  Alarm settings")
                print("2.  Clock settings")
                print("3.  Date settings")
                print("4.  Stopwatch")
                print("5.  Countdown timer")
                print("6.  Auto update of date and time")
              
                



    case 12 :print("Profiles")

    case 13: print("SIM services")

            


















