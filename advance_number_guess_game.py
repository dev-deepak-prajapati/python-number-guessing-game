
import random

def difficulty_level():
    print("""======= SELECT DIFFICULTY ======
1. Easy
2. Medium
3. Hard

""")
    
    choice = input("Enter your choice: ")
    match choice:
        
        case "1":
            return 50, 10
        case "2":
            return 100, 7
        case "3":
            return 500, 10
        case _:
            print("Invalid choice")
            return None ,None
        
def play_game():
    maximum , max_attempt = difficulty_level()
    if maximum is None :
        return
    secret_number = random.randint(1, maximum)
    attemps = 0
    print("Guess a nimber between 1 and",maximum)
    print("You hava",max_attempt,"attempts.")
    
    while attemps < max_attempt:
        try:
            guess = int(input("Enter your guess: "))
            attemps += 1
            if guess == secret_number:
                score = (max_attempt - attemps + 1) * 10
                print("congratulations!")
                print("Correct number :",secret_number)
                print("Attempts:",attemps)
                print("Score:",score)
                return
            elif guess > secret_number:
                print("Too High!")
            else:
                print("Too Low !")
        except ValueError:
            print("Please enter a valid number.")
        
    print("Game Over")
    print("The correct number was:",secret_number)
    
play_game()
            
                        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        