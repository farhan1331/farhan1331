#Imagine an alien was just shot down in a game. Create a
#variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
 
 
alien_color = "green"
 
 
print(alien_color == "green")
if alien_color == "green":
	 print("the player has just earned 5 ponts")
	 
	 
#: Choose a color for an alien as you did in Exercise 5-3, and
#write an if-else chain

if alien_color == ' green':
	print("then player has just earnad five points")
else:
	print("player has just earned 10 points")
	
	
#If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points

if alien_color == 'green':
	print("\nplayer has just earned 5 points")
elif alien_color=='red':
	print("\n player has just earned 15 points")
elif alien_color == 'yellow':
	print("\nplyer has just earned 10 points")
