
# To convert the ascii values to the alphabet number
LOWERCASECONVERT = 96
UPPERCASECONVERT = 38

duplicatesList = list()
itemPriority = 0
lineCounter = 1
stringConcat = ""

def stringSplitter(string:str):
    firstHalf = string[0:int((len(string)/2))]
    secondHalf = string[int((len(string)/2)):-1]
    return firstHalf, secondHalf

def dictCreator(string:str):
    dictionary = dict.fromkeys(string, 0)
    return dictionary

def duplicateChecker(string:str):
    stringTuples = stringSplitter(line)
    uniqueFirstHalf = dictCreator(stringTuples[0])
    for letter in stringTuples[1]:
        if letter in uniqueFirstHalf:
                duplicatesList.add(letter)
    return duplicatesList.pop()

with open("day3\d3_input.txt") as f:
    for line in f:
        if lineCounter % 3 != 0:
            stringConcat += line
        if lineCounter % 3 == 0:
            stringConcat += line
            duplicatesList.append(stringConcat)
        lineCounter += 1
    
    print(duplicatesList)
