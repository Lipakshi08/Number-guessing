import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, guess again....Too small")
        elif guess > random_num:
            print("sorry, guess again.....Too large")   
    print(f"Yay, congrats. You guessed it correctly. The number is {random_num}")

guess(10)

#Next Game
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low     
        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1 
        if feedback == "l":
            low = guess + 1    
    print("Oh no! computer guessed your number", guess, "correctly")

computer_guess(10)           