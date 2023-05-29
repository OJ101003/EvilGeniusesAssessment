'''
Pandas is the only external library used in this class because Pandas is the easiest way to read parquet files in python and have them in Dataframes that are easy to read and write
Pandas also has a lot of extremely powerful filtering tools that takes a huge amount of the work. Since pandas is written in a mix of python and C it should be faster than just doing everything in python only
'''

import pandas as pd
import os

class ProcessGameState():
    def __init__(self, filePath):
        if not os.path.isfile(filePath):
            print("That file does not exist")
        self.filePath = filePath # Gets the filepath as a constructor
        self.df = pd.read_parquet(self.filePath) # Reads the parquet file containing the data and processes it as a pandas DF

    def getDF(self):
        return self.df
    
    def withinBoundary(self, point, coordinateSet): # Point in polygon algorithm
        num_intersections = 0
        x, y = point

        # Using the point in polygon method, we get the point the user wants to see if it's within a boundary and then we get a list of coordinates that make up the border of the area we are examining
        for i in range(len(coordinateSet)): 
            x1, y1 = coordinateSet[i]
            x2, y2 = coordinateSet[(i + 1) % len(coordinateSet)]
            if ((y1 <= y and y < y2) or (y2 <= y and y < y1)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
                num_intersections += 1
        
        return num_intersections % 2 == 1
    
    def playerInventory(self, player, side, roundnum): # Checks a players inventory given the player, side, and round number
        # Makes a inv df that is the original dataframe with all the filters applied and then gets the inventory column of that dataframe
        inv = self.df.loc[(self.df["side"]==side) & (self.df["round_num"] == roundnum) & (self.df["player"] == player) & (self.df["is_alive"] == True)]["inventory"] 
        uniqueWeaponsForPlayer = {} # Dictionary where the keys are the weapon classes and the values are booleans where it's True if they're in the inventory
        for i in inv: # Goes through every row in the dataframe
            if i[0]["weapon_class"] not in uniqueWeaponsForPlayer: # This gets the dictionary (i[0]) then gets the weapon class from that dictionary ([weapon_class])
                uniqueWeaponsForPlayer[i[0]["weapon_class"]] = True # If the weapon class isn't in the dictionary already then it makes a new key value pair with the weapon class and a true boolean

        return uniqueWeaponsForPlayer # Returns the dictionary