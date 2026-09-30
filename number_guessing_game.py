#---------------NUMBER GUESSING GAME-------------------

import random

maximum = 100
secret_number = random.randint(1,maximum)

attempt = 0

print("============================")
print("    NUMBER GUESSING GAME    ")
print("============================")

print("Enter a number between 1 to",maximum,".")

while True:
    try:
        print()
        guess = int(input("enter youe guess: "))
        attempt += 1
        
        if guess == secret_number:
            print("You guessed in",attempt,"attempts.")
            break
        elif guess > secret_number:
            print("Too High ")
                    
        else:
            print("Too Low ")
    
    except ValueError:
        print("Please enter correct value.")
        
