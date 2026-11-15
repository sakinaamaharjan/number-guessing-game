#Using docstring to explain the program 
"""
Description: 
1. The computer randomly selects a number between 1 to 100
2. The user must guess the number within limited attempts (7).
3. After each incorrect guess, a hint is provided
4. Low guess = "Too Low", High guess = "High Guess"
"""

#randint() - used to generate random numbers 

import random

attempts = 7

def display_rules():
    print("Welcome to the number guessing game!\n")
    print("You have 7 attempts to guess the correct number between 1 to 100\n")
    print("Let's Begin!!\n")

def play_game(number, attempt=1): #starting with attempt= 1 as default 
    if attempt > attempts:
        print("Game Over!\n")
        print(f"The correct number is {number}")
        return

    guess = input(f"Attempt {attempt}/7. Enter your guess: ")

#Exception Handling
    try:
        guess = int(guess)
    except ValueError: #ValueError exception is raised if the the input is not an integer
        print("Please enter a valid number!\n")
        return play_game(number, attempt)

    check_guess = lambda x, y: "correct" if x == y else (
        "low" if x < y else "high"
    )

    result = check_guess(guess, number)

    if result == "correct":
        print("Congratulations, you guessed the number!\n")
        print (f"You guessed it in {attempt} attempt(s)")
        return 

    if result == "low":
        print("The number is too low, try a higher number.\n")
    else:
        print("The number is too high, try a lower number\n")

    play_game(number, attempt + 1) #recursion

#Starting the game
display_rules()
random_number = random.randint(1, 100)
play_game(random_number)
