import random

top_of_range = input("type maximum number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number that greater than zero!")
        quit()
else:
    print("The number that you entered must be an integer!")
    
random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1
    
    user_guess = input("Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    
    if user_guess == random_number:
        print("You win!!!")
        break
    elif user_guess < random_number:
        print("Your guess is below, try again.")
    else:
        print("Your guess is above, try again.")


