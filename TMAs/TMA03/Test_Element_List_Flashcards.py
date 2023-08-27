'''
This file in combination with the input stream file 'inputs.txt'
tests the function of 'Element_List_Flashcards_23D.py',
which will be referred to as 'subject' in futher documentation.

It does by looping the function 'show_flashcard()' from the 'subject',
and changing the contents of the 'subject' dictionary 'element_list' to
a predefined single entry each loop, removing the effect of the random
choice within the subject function.

The contents of 'inputs.txt' are then to be piped into the standard stream when
this script is ran, and the output of the stream in piped into 'output.txt'.
This file can then be visually checked for the expected behavour.
--------------------------------------------------------------------
To run test via powershell, navigate to src folder and run command
" Get-content input.txt | python3 Test_Element_List_Flashcards.py > output.txt"
--------------------------------------------------------------------
'''

import Element_List_Flashcards_23D as subject
test_dic = {
    '1':'correct',
    '2':'incorrect',
    '3':'correct2',
    #next test should cause 'index error'
}
for test_count in range(1,4):
    if test_count < 4:
        subject.element_list = {}
        subject.element_list[str(test_count)] = test_dic[str(test_count)]
    subject.show_flashcard()

# import importlib
# importlib.reload(subject)

