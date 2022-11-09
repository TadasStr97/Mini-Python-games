import random
print("Welcome to NUMBER GUESS game! by Tadas Stravinskas 2022.10.08")

top_of_range = input("Enter the range of number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if int(top_of_range) <= 0:
        print("Please enter a greater number!")
        quit()
else:  
    print("Please enter a number!")
    quit()
    
random_number = random.randint(0, top_of_range)

guess = 0
while True:
    guess += 1
    user_guess = input("Guess your number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number!")
        continue

    if user_guess == random_number:
        print("You got it!")
        print("You got it right in", guess, "guesses!")
        break
    elif user_guess < random_number:
        print("You are below the number")
    else:
        print("You are above the number")