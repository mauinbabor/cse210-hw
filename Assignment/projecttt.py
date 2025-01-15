secret = 'beach'
print("Welcome to the word guessing game")


print ("Your hint is:  ", end="")
for i in range(len(secret)):
    print ("_ " , end = "")

         
guess= input("\nWhat is your guess? ")
print("Your hint is:", guess[i])

for i in range (len(guess)):
    
    if guess[i].upper == secret[i].upper():
        print(guess[i].upper(), end="")    

    elif guess[i].lower() in secret.lower():
        print(guess[i].lower(), end="")

    else:
        print ("_ ", end="")     
    
print()
  
while guess != secret:
    guess= input("\nWhat is your guess? ")
    print("Your hint is:", guess[i])

for i in range (len(guess)):
    
    if guess[i].lower == secret[i].upper():
        print(guess[i].upper(), end="")    

    elif guess[i].lower() in secret.lower():
        print(guess[i].lower(), end="")

    else:
        print ("_ ", end="")     



if guess == secret:           
    print ("Congratulations! You guessed the correct word in ",i, "times!") 
