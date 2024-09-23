import random

print(" !!! GUESS THE NUMEBER !!!")

EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_diff(level_chosen):

    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen== 'hard':
        return HARD_LEVEL_ATTEMPTS
    
def checked_answer(guessed , answer , attempts):

    if guessed < answer :
        print("your guess is too low")
        return attempts-1
    elif guessed > answer:
        print("your guess is too high")

        return attempts-1
    else:
        print(f"your guess is right the answer was {answer}")
def game():

    chosen=random.randint(1,50)
    print("Let me think a number between 1 to 50")
    level=input("choose level of difficulty... Type 'easy' or 'hard' ").lower()

    attempts = set_diff(level)

    guess = 0

    while (guess !=chosen):

        print(f"you have {attempts} remaining to guess the number")
        guess = int(input("guess a number"))

        attempts=checked_answer(guess , chosen , attempts)
        
        if attempts==0:
            print("you are out of guesses... You Lose!")
            return
        elif guess!=chosen:
            print("guess again")
game()
            
