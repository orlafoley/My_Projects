# List of five-letter words taken from https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93
# This is intended to take in letters that someone has discovered are grey/yellow/green from playing Wordle
# It sorts through a list of these words using this information to give you valid guesses
# You will receive any remaining valid words in an alphabetically sorted list

def wordleList(filename):
    """
    :param filename: text file of Wordle words
    :return: List of five-letter words
    """

    filein = open(filename, 'r')
    words = filein.readlines()
    dictionary = []

    for word in words:
        word = word.strip('\n').split('\t')
        dictionary += word

    filein.close()

    return dictionary

wordList = wordleList("valid-wordle-words.txt")

def removeWord(words, letter):
    """
    Removes words from the list if they contain a grey letter
    """
    return [word for word in words if letter not in word]

def keepWord(words, letter):
    """
    Keeps words in the list if they contain a letter
    """
    return [word for word in words if letter in word]

def yellowWord(words, letter, place):
    """
    Keeps words in the list if they contain a letter not in a place
    """
    return [word for word in words if letter not in word[place]]

def greenWord(words, letter, place):
    """
    Keeps words in the list if they contain a green letter
    """
    return [word for word in words if letter in word[place]]

def greyLetters(wordList):
    """
    Enter letters that are confirmed not to be in the word
    """
    wrongLetter = input("Have you got any grey letters you have not entered? Y/N ")
    wrongLetter = wrongLetter.capitalize()[0]
    if wrongLetter == "Y":
        whichLetter = input("Please enter the grey letter: ").lower()[0]
        wordList = removeWord(wordList, whichLetter)
        return greyLetters(wordList)
    elif wrongLetter == "N":
        return yellowLetters(wordList)
    else:
        return "Invalid response"
        exit()

def yellowLetters(wordList):
    """
    Enter letters that are in the word but in the wrong place
    """
    probableLetter = input("Have you got any yellow letters you have not entered? Y/N ")
    probableLetter = probableLetter.capitalize()[0]
    if probableLetter == "Y":
        whichLetter = input("Please enter the yellow letter: ").lower()[0]
        position = int(input("Please enter the position of the letter (letter 1/2/3/4/5): "))
        position -= 1
        wordList = keepWord(wordList, whichLetter)
        wordList = yellowWord(wordList, whichLetter, position)
        return yellowLetters(wordList)
    elif probableLetter == "N":
        return greenLetters(wordList)
    else:
        return "Invalid response"
        exit()

def greenLetters(wordList):
    """
    Enter letters that are both in the word and in the correct place
    """
    rightLetter = input("Have you got any green letters you have not entered? Y/N ")
    rightLetter = rightLetter.capitalize()[0]
    if rightLetter == "Y":
        whichLetter = input("Please enter the green letter: ").lower()[0]
        position = int(input("Please enter the position of the letter (letter 1/2/3/4/5): "))
        position -= 1
        wordList = greenWord(wordList, whichLetter, position)
        return greenLetters(wordList)
    elif rightLetter == "N":
        print(wordList)
    else:
        return "Invalid response"
        exit()

greyLetters(wordList)
