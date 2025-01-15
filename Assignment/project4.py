secret = 'beach'
count = 0
i = ""
print("Welcome to the word guessing game")
print ("Your hint is:  ", end="")

for i in range(len(secret)):
    print ("_ " , end = "")
         
guess= input("\nWhat is your guess? ")
print("Your hint is:")

for i in range (len(guess)):
    if guess[i].lower == secret[i].lower():
        print(guess[i].upper(), end="") 
    elif guess[i].lower() in secret.lower():
        print(guess[i].lower(), end="")      
    else:
        print ("_ ", end="")  
count +=1
print()
while guess != secret:
    guess= input("\nWhat is your guess? ")
    print("Your hint is:")

for i in range(len(secret)):
    print ("_ " , end = "")
    
for i in range (len(guess)):
    if guess[i].lower() in secret.lower():
        print(guess[i].lower(), end="")
    else:
        print ("_ ", end="")     
count += 1
if guess == secret:           
    count += 1
    print(f"Congratulations! You guessed the correct word in {count} times!")