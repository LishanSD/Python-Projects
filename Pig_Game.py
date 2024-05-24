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