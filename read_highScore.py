
# function to show top 5 highscores
def highscore():
    f = open('HighScore.csv', 'r')
    leaderboard = [line.replace('\n','') for line in f.readlines()]

    sortedData = sorted(leaderboard,reverse=True)
    print("Top 5 highScores")
    print("Pos: Score Name")
    for i in range(5):
        lol = str(sortedData[i])
        lol = lol.replace(",","    ")
        print(f"{i+1}:     {lol}")

highscore()
