# FLashcards complete version
"""_summary_
Glossary flashcard program
"""

import csv
from random import choice

def load_flash_file(filename:str) -> dict:
    dic = {}
    data = open(filename,'r')
    glossary = csv.reader(data)
    for entry in glossary:
        dic[entry[0]] = entry[1]
    return dic

def  show_flashcard(dic:dict):
    """Shows user a random flashcard from the provided dic
    """
    flash = choice(list(dic))
    print(f'Define: {flash}')
    input('press enter to continue... ')
    print(f'{dic[flash]}') 
     
def flashcard_loop(dic:dict):
    while True:
        user_in = input('type \'s\' to show a card, type \'q\' to quit!_>: ')
        if user_in == 'q':
            break
        elif user_in == 's':
            show_flashcard(dic)
        else:
            print('Invalid input!')

## Main 
filename = '.\B3P2\sglossary.txt'
print('Welcome!')
dic = load_flash_file(filename)
flashcard_loop(dic)