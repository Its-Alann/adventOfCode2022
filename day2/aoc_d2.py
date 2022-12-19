

# Creating a dictionary for the values
rpsValues = {
    "A": 1, #Rock 
    "B": 2, #Paper
    "C": 3, #Scissors
    "X": 1, #Rock
    "Y": 2, #Paper
    "Z": 3  #Scissors
}
scoreCounter = 0

# Opening file and reading the lines
with open("day2\d2_input.txt", "r") as f:
    for line in f:
        # If scores are equal
        if rpsValues[line.split()[1]] == rpsValues[line.split()[0]]:
            scoreCounter += rpsValues[line.split()[1]] + 3

        # If I have rock
        elif rpsValues[line.split()[1]] == 1:         
            # Opp has scissors, I win
            if rpsValues[line.split()[0]] == 3:
                scoreCounter += rpsValues[line.split()[1]] + 6
            else:
                scoreCounter += rpsValues[line.split()[1]]

        # If I have paper
        elif rpsValues[line.split()[1]] == 2:
            # Opp has rock, I win
            if rpsValues[line.split()[0]] == 1:
                scoreCounter += rpsValues[line.split()[1]] + 6
            else:
                scoreCounter += rpsValues[line.split()[1]]

        # If I have scissors
        elif rpsValues[line.split()[1]] == 3:
            # Opp has paper, I win
            if rpsValues[line.split()[0]] == 2:
                scoreCounter += rpsValues[line.split()[1]] + 6
            else:
                scoreCounter += rpsValues[line.split()[1]]

    print(scoreCounter)