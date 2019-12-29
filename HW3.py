# Created on December 26, 2019


import sys
import re
import operator

NO_GUESSES = "I don't know any word of a given length..."
ONE_MORE_TRY = 'Would you like to play one more time? (y/n): '
YES = 'Y'
BYE = 'Bye, see you next time! :)'
WELCOME ='Welcome to a Guessing Word Game!'
THINK_A_WORD = "Think of a word and enter it's length: "
POSITIONS_OF_AVAILABLE_LETTERS ='\n If letter(s): "{}" is available in the hidden word, \n please enter comma separated position(s) counting from 0, \n or just press Enter if the letter is absent: '
EMPTY_STRING = ''
COMMA = ','
DOT = '.'
GUESSED_WORD = 'I guess the hidden word is: "{}"'
CANT_GUESS = "You won! Can't guess the word matching specified letters"
NO_TRIES_LEFT = "No more tries left, so you're probably cheating!"
PATH_TO_DATABASE = 'C:\Python\words.txt'

def searchWords(textFile):
    text = re.findall (r'\w+', textFile.read().lower())
    return text   

def splitWord(word): 
    return [char for char in word]

def sumFreq(d):
    sum_freq = 0
    for key in d:
        sum_freq += d[key]
    return sum_freq
        
def searchUniqueWords(inputList,givenWordLength):       
    listSet = set(inputList) 
    unique_words_list = sorted(list(listSet))
    possibleWordsMatchedReg = [el.lower() for el in unique_words_list if len(el) == givenWordLength]
    if possibleWordsMatchedReg==[]:
        print (NO_GUESSES)
        newGame()
    else:
        return possibleWordsMatchedReg

def getCharFrequency(wordSubset):
    wordsString = EMPTY_STRING.join(wordSubset)
    result = {}
    freq = {}
    sumFreqChars =0
    for char in wordsString:
        try:
            result[char] +=1  # If char already in result dictionary, increase its count
            sumFreqChars +=1                    
        except KeyError:
            result[char] = 1  # If char not in result dict yet, start counting it
            sumFreqChars +=1                   
    for char in result:
        freq[char]=round(result[char]*100/sumFreqChars,2)

    result = sorted(freq.items(), key=operator.itemgetter(1), reverse=True) 
    return result

def newGame():
    answer = input(ONE_MORE_TRY).upper()
    if answer.startswith(YES):
        startGame()
    else:
        print(BYE)
        sys.exit() 

def startGame():
    if len(sys.argv) < 2:        
        with open(PATH_TO_DATABASE) as f:
            print(WELCOME)
            given_word_length = int(input(THINK_A_WORD))
            search_expr = DOT * given_word_length
            word_subset = searchUniqueWords(searchWords(f),given_word_length)  # Select words with given length
            tried_chars = []
            GameOn = True
            while GameOn:
                char_counts = getCharFrequency(word_subset)
                for x in range(len(char_counts)):
                    char_counts = getCharFrequency(word_subset)
                    mostFreqChar = char_counts[x][0] # Get most frequent char
                    if mostFreqChar in tried_chars:
                        continue  # Try next char if such a char already played
                    else:
                        tried_chars.append(mostFreqChar)
                    occurencesList = input(POSITIONS_OF_AVAILABLE_LETTERS.format(mostFreqChar)).split(COMMA)
                    if occurencesList != [EMPTY_STRING]:  # if some positions entered, form regexp for further word's filtering
                        search_expr = list(search_expr)  # convert regexp from string to list for modification
                        for pos in occurencesList:
                            search_expr[int(pos)] = mostFreqChar
                        search_expr = EMPTY_STRING.join(search_expr)  # convert regexp back from list to string
                        r = re.compile(search_expr)
                        word_subset = list(filter(r.match, word_subset))
                        if len(word_subset) == 1:
                            print(GUESSED_WORD.format(word_subset[0]))
                            newGame()
                        elif len(word_subset) == 0:
                            print(CANT_GUESS)
                            newGame()
                        else:
                            break  # There're still words to guess, retry with new char frequencies on new wordSubset
                    else:
                        if x == len(char_counts):
                            print(NO_TRIES_LEFT)
                            sys.exit()
                        continue  # if nothing entered, than no char the word includes, so repeat with next most popular char
    else:
        with open(sys.argv[1], 'r') as f:            
            searchWords(f)                
 
if __name__ == '__main__':
    startGame()
