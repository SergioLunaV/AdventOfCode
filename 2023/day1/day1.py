# Save the file's data
file = open("input", "r")
lines = file.readlines()
file.close()

spelled_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

addition = 0

for line in lines:
    position_number = {}

    # Convert words to numbers and save in the dictionary
    for spelled_number in spelled_numbers:
        # First occurence
        index = line.find(spelled_number)
        if index != -1:
            position_number[index] = spelled_numbers.index(spelled_number)
        
        # Last occurrence
        index = line.rfind(spelled_number)
        if index != -1:
            position_number[index] = spelled_numbers.index(spelled_number)
        
    # Search digit numbers
    index = 0
    for character in line:
        if character.isdigit():
            position_number[index] = character
        
        index += 1

    # Search the first and last
    min_index = float('inf')
    max_index = float('-inf')
    first_number = ""
    last_number = ""

    for index, number in position_number.items():
        if index < min_index:
            min_index = index
            first_number = number
        if index > max_index:
            max_index = index
            last_number = number
        
    addition += int(str(first_number) + str(last_number))

print(addition)
