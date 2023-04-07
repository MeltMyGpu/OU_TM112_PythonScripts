'''
Print triangle like this

***
**
*
'''
size = 3
for line in range(size):
    for asterisk in range(size-line):
        print('*',end='')
    print()