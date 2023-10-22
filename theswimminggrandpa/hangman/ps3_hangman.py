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
    guessed = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed += '_ ' 
        else:
            guessed = guessed + letter + ' '
    return guessed 

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = 'a b c d e f g h i j k l m n o p q r s t u v w x y z' 
    for c in lettersGuessed:
        alpha = alpha.replace(c,'_')  
    return alpha

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
    lettersGuessed = []
    guesses = 8
    print("welcome to hangman")
    print("I have a",len(secretWord),"letter word")
    while guesses > 0:
        print("you have",guesses, "guesses left")
        print(getAvailableLetters(lettersGuessed))
        print(getGuessedWord(secretWord,lettersGuessed))
        letter = input('please guess a letter: ')
        if letter not in secretWord and letter not in lettersGuessed:
            guesses -= 1
            print("oops your guess was incorrect")
        elif letter not in secretWord:
            print("oops you already guessed this letter")
        else:
            print('your guess was correct')
        if letter not in lettersGuessed:
            lettersGuessed += letter
        # print(lettersGuessed)
        if isWordGuessed(secretWord,lettersGuessed):
            print("you won!")
            break
        print('--------------------------------------')
    if not isWordGuessed(secretWord,lettersGuessed):
        print("you lose, loser")
    print("the word was",secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
hangman('its')
