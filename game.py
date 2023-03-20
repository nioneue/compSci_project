import random
import csv

def playGame():
    global high_score
    high_score = 0
    print("rock paper scissors!")
    options = ("rock", "paper", "scissors")
    repeatOptions = ("y", "n")
    running = True
    name = input("Please enter your name: ")

    while running:

        player = None
        computer = random.choice(options)

        player = input("Enter a choice (rock, paper, scissors): ")
        while player not in options:
            print("your choice was not an option")
            player = input("Enter a choice (rock, paper, scissors): ")

        print(f"{name}: {player}")
        print(f"computer: {computer}")

        if player == computer:
            print("Tie!!!")

        elif player == "rock" and computer == "scissors":
            print("you win!!")
            high_score += 1
            print(f"Your score is {high_score}")

        elif player == "paper" and computer == "rock":
            print("you win!!!")
            high_score += 1
            print(f"your score is {high_score}")

        elif player == "scissors" and computer == "paper":
            print("you win!!")
            high_score += 1
            print(f"your score is {high_score}")

        else:
            print("you lose!")
            print(f"your score was {high_score}")
            fieldnames = ['Score','Name']
            with open('HighScore.csv', 'a') as writeFile:
                writer = csv.writer(writeFile)
                writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
                writer.writerow({'Score': high_score, 'Name':name})


            high_score = 0
            
            playAgain = input("Would you like to play again? (y/n): ")
            playAgain = playAgain.lower()
            
            while playAgain not in repeatOptions:
                print("your choice was not an option")
                playAgain = input("Would you like to play again? (y/n): ")
                
            if playAgain == "y":
                    running = True
            else:
                print("Thanks for playing")
                running = False