file = open("example_input", "r")
lines = file.readlines()
file.close()



addition = 0

for line in lines:
    first_digit = ""
    last_digit = ""

    for character in line :
        if character.isdigit() and first_digit == "":
            first_digit = character

        elif character.isdigit() and first_digit != "":
            last_digit = character

    addition += int(str(first_digit) + str(last_digit))

print(addition)