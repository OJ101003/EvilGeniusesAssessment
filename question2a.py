import ProcessGameState as pgs

gameState = pgs.ProcessGameState("data/game_state_frame_data.parquet") # Creates a game state object using the parquet file path

df = gameState.getDF() # Creates a Dataframe variable that contains all the parquet file data

# Creates a list containing all the players in team 2
team2Players = df.loc[(df["team"] == "Team2")]["player"].unique().tolist()

# These are the coordinates that make up the light blue area.
# Coords are stored in tuples and then are stored in a list
coord1 = (-1735,250)
coord2 = (-2024,398)
coord3 = (-2806, 724)
coord4 = (-2472, 1233)
coord5 = (-1565, 580)
coordinateList = [coord1, coord2, coord3, coord4, coord5]

# This gets the coordinates of where players where for each tick of a round, given the player, round, and team
# Returns 2 lists with x and y coordinates
def getCoordsRound(player, round, team):
    xcoordsPlayer = df.loc[(df["team"] == team) & (df["round_num"] == round) & (df["player"] == player)]["x"].tolist()
    ycoordsPlayer = df.loc[(df["team"] == team) & (df["round_num"] == round) & (df["player"] == player)]["y"].tolist()
    return xcoordsPlayer, ycoordsPlayer

# Gets the round numbers where a player went to a certain area, given the team, side, area, and player
# Returns a list with the round numbers
def getRoundNums(team, side, area, player): 
    roundTimes = df.loc[(df["team"] == team) & (df["side"]==side) & (df["area_name"] == area) & (df["player"] == player)]
    roundNumbersOnSite = roundTimes["round_num"].unique().tolist() # The .unique() method gets all unique values given the column name
    return roundNumbersOnSite

# Hardcoded to use the method above and create a dictionary where the keys are all the players on Team2 while
# they are on T side and were on BombsiteB
# Returns a dictionary
def teamRoundsOnBsite():
    playerTimes = {}
    for i in team2Players: # i is each player as a str from the list created in the beginning
        playerTimes[i] = getRoundNums("Team2", "T", "BombsiteB", i)

    return playerTimes

teamOnBSite = (teamRoundsOnBsite())


numTimesPassThruZone = 0 # number of times a zone is passed through

for player, roundnums in teamOnBSite.items(): # Players and round nums where they were on B site
    for i in roundnums: # For each round a player was on b site
        x, y = getCoordsRound(player, i, "Team2") # Gets the coordinates of a player during that round
        for j in range(len(x)): # For loop with the length of the x coordinate lists
            coordPoint = (x[j], y[j]) # Makes a tuple with each coordinate of x and y
            boolVal = gameState.withinBoundary(coordPoint, coordinateList) # returns boolean of whether coordinate val is within the set shape 
            if boolVal: # If the coordinates are within the chokepoint then it is assumed they have entered B site that round through the chokepoint Increments the time when they pass through that zone 
                numTimesPassThruZone += 1 
                print(f"Player: {player} passed through the chokepoint on round number: {i}")
                break

print(f"\nNumber of times the chokepoint was passed through to get to B: {numTimesPassThruZone}")