name = input("Type your name: ")
print("Welcome to \"The Adventure Game\"", str(name) + "!")
print("This game created by Tadas Stravinskas 2022.10.09 \n")

answer = input("You exit the train station. Which direction do you want to go (left/ahead/right/back)? ").lower()

if answer == "left":
    answer = input("You reached the shop and the bridge. Where do you want to go (shop/bridge)? ").lower()
  
    if answer == "shop":
        print("You have not enough money to buy and tried to steal some candies. Unfortunately, but you've been catched and you lose the game.")
        quit()
    elif answer == "bridge":
        answer = input("At the end of the bridge you reached the street. Where do you want to go (left/right)? ").lower()
       
        if answer == "left":
            print("You met some dangerous gangsters, they beated you and you lose the game.")
            quit()
        elif answer == "right":
            print("You came to the job. CONGRATULATIONS! You WON the game!")
            quit()
        else:
            print("You misspelled something. Try again")
    else:
        print("You misspelled something. Try again")

elif answer == "ahead":
    answer = input("You reached bus station. Where do you want to go by bus (center/job)? " ).lower()

    if answer == "center":
        print("You came to city center but you don't have money anymore. You lost the game")
        quit()
    elif answer == "job":
        print("CONGRATULATIONS! You WON the game!")
        quit()
    else:
        print("You misspelled something. Try again")

elif answer == "right":
    answer = input("You reached bus station and McDonalds. Where do you want to go (bus/mcdolands)? ").lower()

    if answer == "bus":
        print("You don't have enough money to buy ticket. You lost the game")
        quit()
    elif answer == "mcdonalds":
        print("You don't have enough money to buy some cheeseburgers. You lost the game")
        quit()
    else:
        print("You misspelled something. Try again")
elif answer == "back":
    print("You don't have enough money to buy ticket to home. You lose the game")
    quit()

else:
    print("You misspelled something. Try again")
    quit()