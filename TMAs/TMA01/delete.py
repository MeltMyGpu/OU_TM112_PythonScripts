
seed = 3
a = 9
b = 5
c = 8
flag = False

print(seed)
while not flag :
    seed = seed * a
    seed = seed + b
    seed = seed % c
    print(seed)
    if seed == 3:
        flag = True


print(pow(2,6) )
