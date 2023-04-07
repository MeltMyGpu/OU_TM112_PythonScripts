# print a triangle of '*' that is lower on the left
'''
  *
 **
***
'''

size = 3
for line in range(1,size+1):
    print(' '*(size-line), end='')
    for asterisk in range(1,line+1):
        print('*',end='')
    print()

## This example from the book can be done in a much simpler way
for line in range(1,size+1):
    spaces = size - line
    print((' ' * spaces) + ('*' * line) )