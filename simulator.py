import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style




def simulation():
    timesRan = int(input("How many times would you like the simulator to run: "))
    options = ("rock", "paper", "scissors")
    rock = 0
    paper = 0
    scissors = 0
    ties = 0

    computer1 = random.choice(options)
    computer2 = random.choice(options)

    runs = 0
    while runs != timesRan:
        
        computer1 = random.choice(options)
        computer2 = random.choice(options)

        # count how many times there was a tie
        if computer1 == computer2:
            ties += 1
        
        # count how many times rock won
        elif computer1 == "rock" and computer2 == "scissors":
            rock += 1
        elif computer2 == "rock" and computer1 == "scissors":
            rock += 1
        
        # count how many times paper won
        elif computer1 == "paper" and computer2 == "rock":
            paper += 1
        elif computer2 == "paper" and computer1 == "rock":
            paper += 1
        
        # count how many times scissors won
        elif computer1 == "scissors" and computer2 == "paper":
            scissors += 1
        elif computer2 == "scissors" and computer1 == "paper":
            scissors += 1
        
        runs += 1

    print(f"\nrock won {rock} times")
    print(f"paper won {paper} times")
    print(f"scissors won {scissors} times")
    print(f"There were {ties} amount of ties")

    # getting percentage
    rockPercent = ((rock/timesRan) * 100)
    paperPercent = ((paper/timesRan) * 100)
    scissorsPercent = ((scissors/timesRan) * 100)
    tiePercent = ((ties/timesRan) * 100)

    # rounding the percent to 2 decimal places
    rockPercent = round(rockPercent, 2)
    paperPercent = round(paperPercent, 2)
    scissorsPercent = round(scissorsPercent, 2)
    tiePercent = round(tiePercent, 2)

    print(f"\nrock won {rockPercent}% of the games")
    print(f"\npaper won {paperPercent}% of the games")
    print(f"\nscissors won {scissorsPercent}% of the games\n")
    print(f"{tiePercent}% of the games were a draw\n")

    input("type enter to continue ")
    
    # grapghing data
    winning_data = {'rock':rockPercent, 'paper':paperPercent, 'scissors':scissorsPercent, 'ties':tiePercent}
    choice_game = list(winning_data.keys())
    winning_percent = list(winning_data.values())

    style.use('bmh')
    plt.figure(figsize=(5,5))
    color = ['royalblue', 'red', 'purple', 'yellow']
    plt.bar(choice_game, winning_percent, color=color, width=0.5)
    plt.xlabel('options')
    plt.ylabel('percentage')
    plt.title(f"percentage of wins and ties out of {timesRan} go's")
    plt.show()

