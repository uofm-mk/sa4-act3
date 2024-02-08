number = 10
print("I'm thinking of a number...")
remaining_guesses = 5

while remaining_guesses > 0:
    guess = input(f"What number am I thinking of? You have {remaining_guesses} guesses remaining. Type 'q' to quit. ")
    
    if guess == 'q':
        print(f"The number was {number}.")
        break
    
    guess = int(guess)
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Sorry! Your guess is too low.")
    else:
        print("Sorry! Your guess is too high.")
    
    remaining_guesses -= 1

if remaining_guesses == 0:
    print(f"Sorry, you've run out of guesses. The number was {number}.")