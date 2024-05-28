import random

def play():
    die = [1,2,3,4,5,6]
    number = random.choice(die)
    print("Your number is ", number)
    return number

def find_winners(score_list, max_score):
    winners = []
    for i, item in enumerate(score_list):
        if item == max_score:
            winners.append(i+1)
    return winners

def game():
    print("Welcome to the Pig Game!")
    print()

    print("The rules are,\
          \n\t1) Each player rolls a single die until either a one is rolled, or they decide to hold.\
          \n\t2) Their score is the sum of all the numbers rolled.\
          \n\t3) If they roll a one in which case their score is zero.")
    print()

    players = int(input("Please enter the number of players : "))
    print()

    score_list = []

    for i in range (players):
        print("Player ", i+1)
        score = 0
        roll = 0
        preference = input("Roll? (y/n) : ")

        while (preference != "n" and roll != 1):
            if (preference == "y"):
                roll = play()

            if (preference == "y" and roll == 1):
                score = 0
                print("Final Score = ", score)
                print("Game over!")
                print()
            elif (preference == "y" and roll != 1):
                score = score + roll
                print("Score = ", score)
                preference = input("Roll? (y/n) : ")
            else:
                roll = 0
                print("Invalid input, try again")
                preference = input("Roll? (y/n) : ")
        
        if (preference == "n"):
            print("Final Score = ", score)
            print()

        score_list.append(score)
    
    max_score = max(score_list)
    winners = find_winners(score_list, max_score)

    for i in range (players):
        print("Player ", i+1, " score = ",score_list[i])

    print()

    if (len(winners) == 1):
        print("The winner is Player", winners[0], "!")
    else:
        print("The winners are Player ", winners, "!")

    print()

again = "y"
while (again != "n"):
    if (again == "y"):
        game()
        again = input("Play again? (y/n) : ")
    else:
        print("Invalid input")
        again = input("Play again? (y/n) : ")