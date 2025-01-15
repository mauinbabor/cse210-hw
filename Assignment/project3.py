game=input("You are escaping from the strange people, and arrive at the cross roads, way leads to the: RIGHT or LEFT. \nWhich way do you go? ")
#first level
if game.lower() == 'right':
    game=input("You head to the right and you found two types of vehicles that you can choose to \neasily escape from the strange people. What vehicle \nyou want to choose a MOTORCYCLE or CAR? ")
if game.lower() == 'motorcycle' :    
    game=input("You choose motorcycle that can run in range of 60 to 80 km per hour. Hurry!. Do you want to add speed to it YES or NO? ")
elif game.lower() == 'car' :
    game=input("You choose car that can run in range of 700 to 800 km per hour. You are about to escape them. Keep CONTINUE or STOP? " )        
else:
    print("Invalid choice") 
#second choice   
if game.lower() ==  'yes' :
    print("You are moving faster and about to escape")
elif game.lower() == 'no' :
    print("You are moving in average speed")  
else:
    print("Invalid context")    
#third choice
if game.lower() == 'continue' :
    game=input("Congratulations! You escape from them. ")
elif game.lower() == 'stop' :
    print("Hurry! They will catch you.")    
else:
    print("Check your answer")    
#second level    
if game.lower() == "left":
    game=input("You head to the left and you saw a old lady and all of her stuff was fallen apart \nbut you are in a hurry. \nDo you want to HELP her or continue to RUN to escape? ")    
if game.lower() == 'help' :
    game=input("You choose to help the old lady. She is asking if you can stay for a while. Do you AGREE or LEAVE her ?" )       
elif game.lower() == 'run' :
    game=input("You choose to run. Do faster than you can. You found a bike along the way. Press USE or NOT" ) 
else:
    print('Look for the choices')           
#second choice      
if game.lower() == 'agree' :   
     print("Thank you! You're so kind. " ) 
elif game.lower() == 'leave' :
    print("Sorry I was in a hurry")  
else:
    print("Look for the choices")
#third choice
if game.lower() == 'use' :
    print("You are about to escape. Keep going! ")
elif game.lower() == 'not' :
    print(" Continue to run faster until you've finally escaped to them ")  
else:
    print("Invalid")   