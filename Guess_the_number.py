import random 

print("The lower bound of this guessing game will be 0\n")
max_number = input("Give an upper bound range: \n")

# Validating the input 
# If user input is not a number or less than zero quit the game
if max_number.isdigit():
    max_number = int(max_number)

    if max_number <= 0:
        print("Error: Number is less than 0")
        quit()
else:
    print("Please type a number next time")
    quit()



# generating a random number
random_number = random.randint(0, max_number)

#guess count
guess_count = 0

#main loop of the game
while True:
    guess_count += 1
    user_guess = input("Make a guess: ")

    # Validating the user input guess
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Type a number!")

    # If user has guess the number, end loop
    # else provide a hint and tell the user to guess lower or higher depending on their guess
    if user_guess == random_number:
        print("You have guessed the number!\n")
        break
    else:
        print("You are wrong!")
        
        if user_guess < random_number:
            print("Hint: Guess Higher!\n")
        else:
            print("Hint: Guess lower!\n")

print("You got it in " , guess_count, " guesses")




