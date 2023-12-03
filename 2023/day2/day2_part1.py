# Possible cubes: 12 red, 13 green and 14 blue
MAX_RED = 12
MAX_GREEN  = 13
MAX_BLUE = 14

# Read the file
inputFile = open("example_input", "r")
text = inputFile.readlines()
inputFile.close()

game_sum = 0

# Read each line
for line in text:
   # Separate the game and the sets
    splited_game = line.split(':')
    game = splited_game[0]
    sets = splited_game[1]

    game_id = game[len(game)-1] # Take the game's id

    # Separate the sets 
    splited_sets = sets.split(';')