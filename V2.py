import random
print("Welcome")
stop = 0
score = 0
round = 0

while stop == 0:
    if round == 0:
        print("You Played",round,"Round")
    elif round == 1:
        print("You played",round,"Round")
    else:
        print("You played",round,"Rounds")
    choicehuman = input("Choose Rock Paper or Scissors or Quit ").lower()

    
    if choicehuman == "quit":
        stop = 1
        print("You won", score, "Out Of", round, "rounds")
    
    else: 
        choiceai = random.randint(1, 3)

        if choiceai == 1:
            round = (round + 1 )
            if choicehuman == "rock":
                print("Rock Vs Rock")
                print("Draw")
            elif choicehuman == "paper":
                print("Paper vs Rock")
                print("You Win")
                score = (score + 1)
            elif choicehuman == "scissors":
                print("Scissors vs Rock")
                print("You Lose")

        elif choiceai == 2:
            round = (round + 1 )
            if choicehuman == "rock":
                print("Rock Vs Paper")
                print("You Lose")
            elif choicehuman == "paper":
                print("Paper vs Paper")
                print("Draw")
            elif choicehuman == "scissors":
                print("Scissors vs Paper")
                print("You Win")
                score = (score+1)

        elif choiceai == 3:
            round = (round + 1 )
            if choicehuman == "rock":
                print("Rock Vs Scissors")
                print("You Win")
                score = (score+1)
            elif choicehuman == "paper":
                print("Paper vs Scissors")
                print("You Lose")
            elif choicehuman == "scissors":
                print("Scissors vs Scissors")
                print("Draw")

        else:
            print("Error, try again")
