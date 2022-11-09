import random
print("Hello and welcome to \"ROCK, PAPER & SCISSORS\" game! by Tadas Stravinskas 2022.10.08 \n")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Choose Rock/Paper/Scissors or type \"Q\" to quit, - ").lower()
    if user_pick == "q":
        break
    else:
        if user_pick not in options:
            print("You choosed invalid pick")
            continue

    computer_pick = options[random.randint(0, 2)]
    # 0: rock, 1: paper, 2: scissors
    print("Computer pick:", computer_pick)

    if user_pick == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_pick == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    
    elif user_pick == " scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_pick == computer_pick:
        print("It's a draw!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times!")
print("Computer won", computer_wins, "times!")

if user_wins > computer_wins:
    print("You are the WINNER!")
elif user_wins < computer_wins:
    print("You are the LOOSER!")
else:
    print("You both played well. GG!")

print("Goodbye!")