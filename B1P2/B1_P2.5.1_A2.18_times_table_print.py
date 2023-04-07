# Prints the times tables up to a value 'size'

size = 12

for row in range(1, size+1):
    for column in range(1 ,size+1):
        print(row * column, end=' ')
    print()

