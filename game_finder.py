"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	# Replace the line below with your code

	# Create a dictionary to hold the gameID's and have how many players have hit the true shooting percentage as a value
	games = {}

	# Create a list for to return qualified games
	qualified = []

	# Use loop to go through each dictionary and check shooting percentage, adding 1 if players percentage hit to the games dictionary if a gameID has already been added as a key, if not creating one and adding 1
	for x in list:
		total = dict.get("fieldGoal2Attempted") + dict.get("fieldGoal3Attempted") + dict.get("freeThrowAttempted")
		made = dict.get("fieldGoal2Made") + dict.get("fieldGoal3Made") + dict.get("freeThrowMade")
		percent = made/total
		if ( percent >= true_shooting_cutoff):
			games[str(dict.get("gameIDs")] += 1
			
	# Use a loop to go through the games{} dictionary to check which ones have a greater number of players who hit the percentage than player_count, and adding that game to the qualified list
	for x in games:
		if games.get(x) >= player_count:
			qualified.append(x)

	# Used to sort the qualified list
	qualified.sort()

	# returns the qualified list
	return qualified
	
	pass
