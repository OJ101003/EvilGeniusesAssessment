import ProcessGameState as pgs
import math

gameState = pgs.ProcessGameState("data/game_state_frame_data.parquet") # Creates a game state object using the parquet file path

df = gameState.getDF() # Creates a Dataframe variable that contains all the parquet file data

# Creates a list containing all the players in team 2
team2Players = df.loc[(df["team"] == "Team2")]["player"].unique().tolist()

# Method that takes the team, side, area, and player as arguments
# Filters out a df with the arguments given
# Returns dictionary where the key is round num and value is time elapsed when entering given area
def getRoundSeconds(team, side, area, player):
    roundTimes = df.loc[(df["team"] == team) & (df["side"]==side) & (df["area_name"] == area) & (df["player"] == player)][["round_num", "seconds"]]
    roundNumbersOnSite = roundTimes["round_num"].unique()
    round_nums_passed = {}
    for i in roundNumbersOnSite:
        round_nums_passed[i] = roundTimes[(roundTimes["round_num"] == i)]["seconds"].head(1).item()
    return round_nums_passed # Returns dictionary with rounds the player entered B site and the time elapsed when they entered

# Hardcoded method that gets each player from team 2 and uses their names as keys in a dictionary
# The values of the dictionary are the dictionaries returned from the above method
# Ex: {(name)Player5 : {(roundNum)16: (timeElapsed)51}}
def playerTimesMethod():
    playerTimes = {}
    for i in team2Players:
        playerTimes[i] = getRoundSeconds("Team2", "T", "BombsiteB", i)

    return playerTimes # Dictionary

'''
 Get's players inventory given the player, side, and roundnum
 This is achieved by filtering out a dataframe with the filters being the side, the round num, the player, and whether they're alive or not 
 By doing this we get a dataframe containing the players inventory each tick for the whole round
 We then sift through each row, get the inventory dictionary, and then make a new dictionary that shows what weapon classes were used
 The dictionary key is the weapon class, and the value is a True boolean
 If the weapon class is in the dictionary then that means that at one point during the round the player had that weapon
 The areaBefore argument is if you want to check the inventory before they enter an area. The default ignores that argument
 '''
def playerInventory(player, side, roundnum, areaBefore = ""): # Have self at beginning when putting into code
    inv = df.loc[(df["side"]==side) & (df["round_num"] == roundnum) & (df["player"] == player) & (df["is_alive"] == True) & (df["area_name"]!= areaBefore)]["inventory"]
    uniqueWeaponsForPlayer = {}
    for i in inv:
        if i[0]["weapon_class"] not in uniqueWeaponsForPlayer:
            uniqueWeaponsForPlayer[i[0]["weapon_class"]] = True

    return uniqueWeaponsForPlayer # Dictionary

playerTimesOnBsite = (playerTimesMethod())
peopleEnteredBSite = {}

# For loop that groups players based on what rounds they entered B site
for i in playerTimesOnBsite: # i is the player names
    variableName = list(playerTimesOnBsite[i].keys()) # Get's the list of rounds a player was on B site
    
    for j in variableName: # j is the round num
        j = int(j)
        if j in peopleEnteredBSite: # If j is in the dictionary, then add player name to the round num list
            peopleEnteredBSite[j].append(i)
        else:
            peopleEnteredBSite[j] = [i] # If round num is new then make a new key in the dictionary and assign it player name


# This for loop gets all the rounds where there were at least 2 players who entered B site and had rifles or smgs
# Stores the rounds in a list
roundsWithRiflesSmgs = []
for roundnum,players in peopleEnteredBSite.items():
    numWithRifles = 0
    avgTime = 0
    for i in players:
        currentInv = playerInventory(i,"T",roundnum)
        if ("Rifle" in currentInv or "SMG" in currentInv):
            numWithRifles += 1
    if numWithRifles > 1:
        roundsWithRiflesSmgs.append(roundnum)


avgTime = 0 # Average entry timer
# For loop that goes through each round where there were at least 2 players who entered B site and had rifles or smgs
# The for loop then gets the average entry time of everyone on the team who entered B site that round.
for rounds in roundsWithRiflesSmgs:
    tempTime = 0
    numPlayers = 0
    for player in team2Players:
        if player in peopleEnteredBSite[rounds]:
            numPlayers += 1
            tempTime += getRoundSeconds('Team2', 'T', 'BombsiteB', player)[rounds]
    avgTime += tempTime/numPlayers

# Divides the average time by the number of rounds there were 2 people with rifles and smgs
avgTime /= len(roundsWithRiflesSmgs)
avgTime = math.ceil(avgTime) # This is the average time elapsed when they enter B site with at least 2 rifles
timer = 115-avgTime
minutes = timer // 60
seconds = timer % 60
print(f"%02i:%02i" % (minutes, seconds)) # This is the final answer
