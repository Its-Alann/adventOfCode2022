

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
        
        # I need to lose
        if rpsValues[line.split()[1]] == 1:
            # Op has rock
            if rpsValues[line.split()[0]] == 1:
                scoreCounter += rpsValues["C"]
            # Op has paper
            elif rpsValues[line.split()[0]] == 2:
                scoreCounter += rpsValues["A"]
            # Op has scissors
            elif rpsValues[line.split()[0]] == 3:
                scoreCounter += rpsValues["B"]

        # I need to draw
        elif rpsValues[line.split()[1]] == 2:
            # Op has rock
            if rpsValues[line.split()[0]] == 1:
                scoreCounter += rpsValues[line.split()[0]] + 3
            # Op has paper
            elif rpsValues[line.split()[0]] == 2:
                scoreCounter += rpsValues[line.split()[0]] + 3
            # Op has scissors
            elif rpsValues[line.split()[0]] == 3:
                scoreCounter += rpsValues[line.split()[0]] + 3

        # I need to win
        elif rpsValues[line.split()[1]] == 3:
            # Op has rock
            if rpsValues[line.split()[0]] == 1:
                scoreCounter += rpsValues["B"] + 6
            # Op has paper
            elif rpsValues[line.split()[0]] == 2:
                scoreCounter += rpsValues["C"] + 6
            # Op has scissors
            elif rpsValues[line.split()[0]] == 3:
                scoreCounter += rpsValues["A"] + 6

    print(scoreCounter)
