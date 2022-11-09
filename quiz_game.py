print("Welcome to quiz game! by Tadas Stravinskas 2022.10.08")

playing = input("Do you want to play? - ")

if playing.lower() != "yes":
    print("But why :(")
    quit()

print("Okey! Let's play! There're 5 questions about auto/moto engineering")
score = 0

answer = input("What ECU stands for? - ")
if answer.lower() == "electronic control unit" or answer == "engine control unit":
    print("Correct! Either way, both of \"Electronic Control Unit\" and \"Engine Control Unit\" are correct answers!")
    score += 1
else:
    print("Incorrect!")

answer = input("What MAF stands for? - ")
if answer.lower() == "mass air flow":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input("How many wheels motocyces do usually have? - ")
if answer == "2":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What DI stands for? - ")
if answer.lower() == "direct injection":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Does stock Subaru WRX has a turbo? - ")
if answer.lower() == "yes":
    print("Correct! Both WRX and WRX STI have turbo")
    score += 1
else:
    print("Incorrect! Both WRX and WRX STI have turbo")

print("Quiz game is finished!")
print("You got " + str(score) + " of 5 questions right!")
print("That's " + str((score / 5) * 100) + "%")