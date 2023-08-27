# Starter file for TM112 2023D TMA03 Q2


"""
This flashcard program allows the user to ask for a element_list entry.
In response, the program randomly picks an key from all element_list
entries. It shows the key and prompts the user for the corresponding  
entries symbol. If the user is correctly the user is infomred and the 
entry is deleted from element_list, otherwise the user is informed 
and corrected.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# IMPORTANT
# Q2 (a)(iii) Make changes only to
# -- the docstring for the program as a whole;
# -- the docstring of the show_flashcard() function;
# -- the body of the show_flashcard() function.


def show_flashcard():
    """ Show the user a random key from element_list and ask them
        to provide the corresponding entries symbol. If the 
        user is correct the entry is deleted from 
        the dictionary, otherwise the user is corrected.
    """
    # Obtain random entry and prompt user input
    random_key = choice(list(element_list))
    correct_symbol = element_list[random_key]
    user_answer = input(f'Please enter the corresponding symbol for {random_key}: ')
    
    # Check answer and respond accordingly 
    if user_answer == correct_symbol:
        print(f'That is correct! The symbol for {random_key} is {user_answer}. ')
        del element_list[random_key]
    else:
        print(f'Incorrect, the correct symbol for {random_key} is {correct_symbol}. ')

    
## Set up the element_list
element_list = {'Sodium':'Na',
                'Potassium':'K',
                'Iron':'Fe',
                'Copper':'Cu',
                'Silver':'Ag',
                'Tin':'Sn',
                'Antimony':'Sb',
                'Tungsten':'W',
                'Gold':'Au',
                'Mercury':'Hg',
                'Lead':'Pb'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q' or len(element_list) == 0:
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')              
