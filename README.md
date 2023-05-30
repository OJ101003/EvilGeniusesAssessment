# SWE Intern Assessment for Evil Geniuses
## Required external modules
- Pandas
- MatPlotLib

I used MatPlotLib for question 2C because it already has a lot of packages in common with Numpy, and because it's the easiest way I found to get a descriptive heatmap that is interactable and can be used to get specific coordinates on the grid provided. The benefits of using an external library far exceeded any downsides by providing greater accuracy, more details, and allowing customization.

## Question 2a (Script in question2a.py):
I determined that entering B site from the light blue boundary was **not** a common strategy used by Team 2 on T side. Using the code in question2a.py, I found that only player 5 and 9 used the choke point to enter B site on round 16 meaning only 2 people used the choke point as an entryway to B site while given that Team 2 is on T side.
The text outputted was:

```
Player5 passed through the chokepoint on round number: 16
Player9 passed through the chokepoint on round number: 16

Number of times the chokepoint was passed through to get to B: 2
```

## Question 2b (Script in question2b.py):
I found that the average timer that players on Team2 on T side entered B site with at least 2 rifles or SMGs was 1:24. The output was just ```01:24```.

## Question 2c (Script in question2c.py):
Using methods found in previous scripts and using MatPlotLib, I made a heatmap that showed where the most activity was on BombsiteB. After doing in game testing and looking at the coordinates on my heatmap and in game, I found that the area of the map classified as "BombsiteB" was larger than what it was led to be using the map provided by "Simple Radar." The heatmap provided shows the areas that Team 2 have the most frequency of being at in Bombsite B based off the colors on the heatmap. Using the program it also showed coordinates where the most frequently visited areas were so you could go in game and go to the coordinates. 


### Question 2C screenshots
<p align="center">
<img src="https://images2.imgbox.com/be/ae/jKskm2m9_o.png" alt= “2COutput” width="70%" height = width>
</p>
<p align="center">
<strong>The areas highlighted blue are the general locations where there is most activity by Team2 on CT side</strong>
<img src="https://images2.imgbox.com/fc/58/qWUF3Olj_o.jpg" alt= “MapHighlight” width="50%" height = width >
</p>


## Question 3
Given a week-long timeframe, solutions would vary depending if I was working with a team or by myself.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If I was working by myself a solution I would implement would be a GUI of some sort that can show all the data without code being needed. This GUI would feature the option to input custom boundaries and to get statistics for specific tasks, such as for question 2b. Of course the coaching staff would need to do some basic statistical calculations themselves since I wouldn’t want to make the program only able to solve super specific tasks.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If working with a team, a solution I would want to implement would be a web based system that would allow different criterias and boundaries to be selected to output certain statistics. Using Flask would make light work to implement some sorts of API that would get information from the scripts I coded. The web UI would also feature some sort of export feature to get the data generated. Deploying the web app to a local server would be the most cost effective in my eyes if it’s only going to be used for the coaching staff at evil geniuses, however if needed in the future it could be implemented in a cloud based platform such as AWS or GCP.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I believe the biggest factor to the success of either solution would be proper documentation and training provided to the coaches so they know what they’re looking at. After implementing each solution I would go and provide some sort of training session to the coaches so they understand how to use the program and I’d use that as an opportunity to get insight into what needs to be fixed or implemented.
