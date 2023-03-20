from getpass import getpass as inp

def twoPlayer():
    print("rock paper scissors!")
    options = ("rock", "paper", "scissors")
    repeatOptions = ("y", "n")
    running = True

    print("look away player 2")
    player_name = input("Player 1 please enter your name: ")
    print("\nlook away player 1")
    player2_name = input("Player 2 please enter your name: ")


    while running:

        player = None
        player2 = None

        player = inp(f"\n{player_name} please enter a choice (rock, paper, scissors): ")
        while player not in options:
            print("your choice was not an option")
            player = inp(f"{player_name} please enter a choice (rock, paper, scissors): ")
        
        player2 = inp(f"{player2_name} pleas enter a choice (rock, paper, scissors): ")
        while player2 not in options:
            print("your choice was not an option")
            player2 = inp(f"{player2_name} please enter a choice (rock, paper, scissors): ")

        print(f"\n{player_name}: {player}")
        print(f"{player2_name}: {player2}")

        if player == player2:
            print("\nTie!!!")
        elif player == "rock" and player2 == "scissors":
            print(f"\n{player_name} wins!!")
        elif player == "paper" and player2 == "rock":
            print(f"\n{player_name} wins!!")
        elif player == "scissors" and player2 == "paper":
            print(f"\n{player_name} wins!!")
        else:
            print(f"\n{player2_name} wins!!")
        
        playAgain = input("\nWould you like to play again? (y/n): ")
        playAgain = playAgain.lower()

        while playAgain not in repeatOptions:
            print("your choice was not an option")
            playAgain = input("Would you like to play again? (y/n): ")
        
        if playAgain == "y":
            running = True
        else:
            print("Thanks for playing")
            running = False