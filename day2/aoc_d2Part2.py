

# Creating a dictionary for the values
rpsValues = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Lose
    "Y": 2,  # Win
    "Z": 3   # Draw
}
scoreCounter = 0

# Opening file and reading the lines
with open("day2\d2_input.txt", "r") as f:
    for line in f:
        
        # I need to Lose
        if rpsValues[line.split()[1]] == 1:
            scoreCounter += rpsValues[line.split()[1]] + 3

    print(scoreCounter)
