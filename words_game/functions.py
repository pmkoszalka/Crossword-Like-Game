import random
import nltk
from words_game.constants import *

def randomize():
    '''Randomizes the vowels and consonants'''
    random.shuffle(VOWELS)
    random.shuffle(CONSONANTS)


def diagram_letters_func():
    '''Creates letters for diagrams'''

    diagram_letters_list = []

    for number in range(NUMBER_LETTERS_DIAGRAM):
        diagram_letters_list.append((VOWELS + CONSONANTS)[number])

    return diagram_letters_list

def board(diagram_letters_list):
    '''Creates a board for the game'''

    print(' {}| {}|  {}'.format(diagram_letters_list[0],diagram_letters_list[1],diagram_letters_list[2]))
    print('__|__|__')
    print('  |  | ')
    print(' {}| {}|  {}'.format(diagram_letters_list[3],diagram_letters_list[4],diagram_letters_list[5]))
    print('__|__|__')
    print('  |  | ')
    print(' {}| {}|  {}'.format(diagram_letters_list[6],diagram_letters_list[7],diagram_letters_list[8]))

def words(diagram_letters_list, letters_number):
    '''Creates words from the letters'''

    freqdict = nltk.FreqDist(diagram_letters_list)
    obligatory_letter = diagram_letters_list[4]
    dictionary_of_words = nltk.corpus.words.words()
    words = [word for word in dictionary_of_words if obligatory_letter in word and len(word)>=letters_number and freqdict >= nltk.FreqDist(word)]
    return words

def measure_and_join(list_of_words : list):
    '''Outputs words from a list without list\'s brackets'''

    if len(list_of_words) == 0:
        return ''
    elif len(list_of_words) == 1:
        return list_of_words[0]
    else:
        return ', '.join(list_of_words)