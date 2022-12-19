
# Open the file reader
file = open('day1\d1_input.txt', "r")

# Reads every line in the file
line = file.readlines()


# Initializes the counters needed
maxCals = 0
calCounter = 0

# Goes through the file
for x in line:
    # If line is present, add it to the counter
    if x.strip():
        calCounter += int(x)
    # If the line is empty check if the sum if greater than the total
    else: 
        if maxCals < calCounter:
            maxCals = calCounter
        calCounter = 0

print("The max amount of calories an elf has is: " + str(maxCals))

# Closing the file reader
file.close()