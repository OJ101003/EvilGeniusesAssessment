import ProcessGameState as pgs
import pandas as pd
import matplotlib.pyplot as plt

gameState = pgs.ProcessGameState("data/game_state_frame_data.parquet") # Creates a game state object using the parquet file path

df = gameState.getDF() # Creates a Dataframe variable that contains all the parquet file data

team2Players = df.loc[(df["team"] == "Team2")]["player"].unique().tolist()

# All the methods are pretty much the same as they were from last time
def getCoordsRound(player, round, team):
    xcoordsPlayer = df.loc[(df["team"] == team) & (df["round_num"] == round) & (df["player"] == player) & (df["area_name"] == "BombsiteB")]["x"].tolist()
    ycoordsPlayer = df.loc[(df["team"] == team) & (df["round_num"] == round) & (df["player"] == player) & (df["area_name"] == "BombsiteB")]["y"].tolist()
    return xcoordsPlayer, ycoordsPlayer

def getRoundNums(team, side, area, player): 
    round_times = df.loc[(df["team"] == team) & (df["side"]==side) & (df["area_name"] == area) & (df["player"] == player)]
    roundNumbersOnSite = round_times["round_num"].unique()
    round_nums_passed = []
    for i in roundNumbersOnSite:
        round_nums_passed.append(i)
    return round_nums_passed

def playerTimesMethod(): 
    playerTimes = {}
    for i in team2Players:
        playerTimes[i] = getRoundNums("Team2", "CT", "BombsiteB", i)

    return playerTimes

playerRoundsOnB = (playerTimesMethod())

totalCoordinatesX = []
totalCoordinatesY = []
for player, roundnums in playerRoundsOnB.items(): # Players and round nums where they were on B site
    for i in roundnums: # For each round a player was on b site
        x, y = getCoordsRound(player, i, "Team2") # Gets the coordinates of a player during that round
        totalCoordinatesX += x # Adds all the coordinates to a list
        totalCoordinatesY += y

coordData = pd.DataFrame({'X': totalCoordinatesX, 'Y': totalCoordinatesY})


# Set the number of bins
bins = 75  # Adjust the number of bins as desired. More bins means smaller squares but more detailed

# Create a 2D histogram
fig, ax = plt.subplots()
hist = ax.hist2d(coordData['X'], coordData['Y'], bins=bins, cmap='gist_earth')

# Add colorbar
plt.colorbar(hist[3], label='Frequency')

# Set labels and title
plt.xlabel('X coordinates')
plt.ylabel('Y coordinates')
plt.title('2D Histogram of Coordinates')

# Show the plot
plt.show()
