from simulator import simulation
from game import playGame
from multiplayer import twoPlayer
from read_highScore import highscore

choice = ("simulation", "playGame", "twoPlayer", "highscore")
playerChoice = input("what would you like to do (simulation, playGame, twoPlayer or highscore): ")
while playerChoice not in choice:
    print("mispell!")
    playerChoice = input("what would you like to do (simulation, playGame, twoPlayer or highscore): ")

if playerChoice == "simulation":
    simulation()
elif playerChoice == "playGame":
    playGame()
elif playerChoice == "twoPlayer":
    twoPlayer()
else:
    highscore()
