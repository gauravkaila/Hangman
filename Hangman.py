# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Gaurav/6.00.1x Files/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    if lettersGuessed == []:
        return False
        
    list_secretWord = []
    for i in range(len(secretWord)):
        x = secretWord[i]
        list_secretWord.append(x)
    print list_secretWord
    
    i = 0
    while i < len(secretWord):
        if list_secretWord[i] in lettersGuessed:  
            i = i+1
        else: 
            return False 
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if lettersGuessed == []:
        guessedWords1 = '_'*len(secretWord)
        return guessedWords1
        
    list_secretWord = []
    for i in range(len(secretWord)):
        x = secretWord[i]
        list_secretWord.append(x)
    
    i = 0
    string_list = []
    guessedWords = str() 
    while i < len(secretWord):
        if list_secretWord[i] in lettersGuessed:  
            string_list = list_secretWord[i]
        else: 
            string_list = '_'
        i +=1
        guessedWords += string_list
    return guessedWords



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    string_lowercase = string.ascii_lowercase

    list_lettersGuessed = []
    for i in range(len(lettersGuessed)):
        list_lettersGuessed.append(lettersGuessed[i])

    list_stringlowercase = []
    for i in range(len(string_lowercase)):
        list_stringlowercase.append(string_lowercase[i])

    for i in list_lettersGuessed:
        if i in list_stringlowercase:
            list_stringlowercase.remove(i)
    
    nonguessedWords = str()
    for i in list_stringlowercase:
        nonguessedWords += str(i)
    return nonguessedWords

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
    #loadWords()
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-------------'
    i = 8
    lettersGuessed = []
    while i > 0:
        print 'You have ' + str(i) + ' guesses left.'
        print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
        guessLetter = str(raw_input('Please guess a letter: '))
        guessLetter = guessLetter.lower()
        if guessLetter in lettersGuessed:
            print 'Oops! Youve already guessed that letter: ' + str(getGuessedWord(secretWord,lettersGuessed))
            print '-------------'
        elif guessLetter in secretWord:
            lettersGuessed.append(guessLetter)
            print 'Good guess:' + str(getGuessedWord(secretWord,lettersGuessed))
            print '-------------'
        else:
            lettersGuessed.append(guessLetter)
            print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord,lettersGuessed))
            i -=1
            print '-------------'
            
        if getGuessedWord(secretWord,lettersGuessed) == secretWord:
            print 'Congratulations, you won!'
            break
        elif i == 0:
            print 'Sorry, you ran out of guesses. The word was ' + str(secretWord)
            
    
    
hangman(chooseWord(wordlist))
input()



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
