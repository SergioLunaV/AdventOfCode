# Possible cubes: 12 red, 13 green and 14 blue
MAX_RED = 12
MAX_GREEN  = 13
MAX_BLUE = 14

# Read the file
inputFile = open("puzzle_input", "r")
text = inputFile.readlines()
inputFile.close()

power_sum = 0

# Read each line
for line in text:
   # Separate the game and the sets
    splitted_game = line.split(':')
    game = splitted_game[0].split(' ') # Separate "Game" and id
    sets = splitted_game[1].split(';') # Separate sets

    game_id = game[1]    

    # Minimum cubes required of all the sets of a game
    min_red = 1
    min_green = 1
    min_blue = 1

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
            
            cube_quantity = splitted_subset[1]

            cube_color = splitted_subset[2].strip("\n")

            # Number of cubes used in a set
            if(cube_color == "red"):
                red_count += int(cube_quantity)
            elif(cube_color == "green"):
                green_count += int(cube_quantity)
            elif(cube_color == "blue"):
                blue_count += int(cube_quantity)
                
        # Get the highest number of cubes used in the game
        if(red_count > min_red):
            min_red = red_count
        if(green_count > min_green):
            min_green = green_count
        if(blue_count > min_blue):
            min_blue = blue_count
    
    power = min_red * min_green * min_blue
    power_sum += power

print("The addition of the power of the minimum cubes is:", power_sum)