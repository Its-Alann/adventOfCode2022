
# To convert the ascii values to the alphabet number
LOWERCASECONVERT = 96
UPPERCASECONVERT = 38

duplicatesList = set()
itemPriority = 0

def stringSplitter(string:str):
    firstHalf = string[0:int((len(string)/2))]
    secondHalf = string[int((len(string)/2)):-1]
    return firstHalf, secondHalf

def dictCreator(string:str):
    firstHalfDict = dict.fromkeys(string, 0)
    return firstHalfDict

def duplicateChecker(string:str):
    stringTuples = stringSplitter(line)
    uniqueFirstHalf = dictCreator(stringTuples[0])
    for letter in stringTuples[1]:
        if letter in uniqueFirstHalf:
                duplicatesList.add(letter)
    return duplicatesList.pop()

with open("day3\d3_input.txt") as f:
    for line in f:
        if str(duplicateChecker(line)).isupper():
            itemPriority += ord(duplicateChecker(line)) - UPPERCASECONVERT
        elif str(duplicateChecker(line)).islower():
            itemPriority += ord(duplicateChecker(line)) - LOWERCASECONVERT
    
    print(itemPriority)