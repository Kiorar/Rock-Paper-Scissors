import random
print("Welcome")
stop = 0

while stop == 0:
    choicehuman = input("Choose Rock Paper or Scissors or Quit ").lower()

    if choicehuman == "quit":
        stop = 1
    else: 
        choiceai = random.randint(1, 3)

        if choiceai == 1:
            if choicehuman == "rock":
                print("Rock Vs Rock")
                print("Draw")
            elif choicehuman == "paper":
                print("Paper vs Rock")
                print("You Win")
            elif choicehuman == "scissors":
                print("Scissors vs Rock")
                print("You Lose")

        elif choiceai == 2:
            if choicehuman == "rock":
                print("Rock Vs Paper")
                print("You Lose")
            elif choicehuman == "paper":
                print("Paper vs Paper")
                print("Draw")
            elif choicehuman == "scissors":
                print("Scissors vs Paper")
                print("You Win")

        elif choiceai == 3:
            if choicehuman == "rock":
                print("Rock Vs Scissors")
                print("You Win")
            elif choicehuman == "paper":
                print("Paper vs Scissors")
                print("You Lose")
            elif choicehuman == "scissors":
                print("Scissors vs Scissors")
                print("Draw")

        else:
            print("Error, try again")
