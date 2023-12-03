# Possible cubes: 12 red, 13 green and 14 blue
MAX_RED = 12
MAX_GREEN  = 13
MAX_BLUE = 14

# Read the file
inputFile = open("puzzle_input", "r")
text = inputFile.readlines()
inputFile.close()

game_id_sum = 0

# Read each line
for line in text:
   # Separate the game and the sets
    splitted_game = line.split(':')
    game = splitted_game[0].split(' ') # Separate "Game" and id
    sets = splitted_game[1].split(';') # Separate sets

    game_id = game[1]    
    valid_game = True

    for set in sets:
        # Separate each get of cubes
        subsets = set.split(',')

        # Number of cubes of each color used in a set
        red_count = 0
        green_count = 0
        blue_count = 0

        for subset in subsets:
            # Separate each cube
            splitted_subset = subset.split(' ')
            
            cube_quantity = int(splitted_subset[1])

            cube_color = splitted_subset[2].strip("\n")

            # Number of cubes used in a set
            if(cube_color == "red"):
                red_count += cube_quantity
            elif(cube_color == "green"):
                green_count += cube_quantity
            else:
                blue_count += cube_quantity
                
        if(red_count > MAX_RED) or (green_count > MAX_GREEN) or (blue_count > MAX_BLUE):
            valid_game = False
            break

    if(valid_game == True):
        game_id_sum += int(game_id)

print("The sum of the ID's of the valid games is:", game_id_sum)