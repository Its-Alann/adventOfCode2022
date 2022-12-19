# Open the file reader
file = open('day1\d1_input.txt', "r")

# Reads every line in the file
line = file.readlines()

# Three counters for the three top elfs
maxCals = 0
maxCals2 = 0
maxCals3 = 0
calCounter = 0

# Goes through the file
for x in line:
    # If the the line exists add it to the calorie counter
    if x.strip():
        calCounter += int(x)
    # If the line is empty update the counters and reset the calorie counter
    else:
        if maxCals < calCounter:
            maxCals2 = maxCals
            maxCals = calCounter
        elif maxCals2 < calCounter:
            maxCals3 = maxCals2
            maxCals2 = calCounter
        elif maxCals3 < calCounter:
            maxCals3 = calCounter
        calCounter = 0

# Print the final values
print("The elf with the most calories: " + str(maxCals))
print("The elf with the second most calories: " + str(maxCals))
print("The elf with the third calories: " + str(maxCals))
print("The sum is: " + str(maxCals + maxCals2 + maxCals3))

# Closing the file reader
file.close()