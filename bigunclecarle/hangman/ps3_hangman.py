# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guessed = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed = False
    return guessed


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    # Get each letter (Loop) through secret word (for loop)
    #   if letter is in letters guessed then 
    #     store the letter and a space in output string
    #   else
    #     store the underscore '_' and a space
    # retun the output string
    # 'a _ _ l _' ['a', 'q', 'z', 'x', 'l']
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed = guessed + letter + ' '
        else:
            guessed = guessed + '_ '
    return guessed


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # 'a b c _ e f ...'
    # FILL IN YOUR CODE HERE...
    def getAvailableLetters(lettersGuessed):
        letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
        for c in lettersGuessed:
            letters = letters.replace(c,'_')
        return letters
        print(letters)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
    letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print,len(secretWord),('letters in this word')
    print('welcome to the game of hangman')
    tries = 8
    lettersGuessed = []
    while tries > 0:
        print('You have', tries, 'tries left')
        print(getAvailableLetters(lettersGuessed))
        print(getGuessedWord(secretWord, lettersGuessed))
        letter = input('give me a letter')
        if letter not in secretWord and letter not in lettersGuessed:
            tries-=1
            print('Oops, your guess is incorrect!')
        if letter not in lettersGuessed: 
            lettersGuessed += letter
        if isWordGuessed(secretWord, lettersGuessed):
            print('you guessed the secret word!')
            break
        print('---------------------------------------------')
    if not isWordGuessed(secretWord, lettersGuessed):
        print('You lose')
    print('The word was', secretWord)
        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
