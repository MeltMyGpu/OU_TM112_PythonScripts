data = [10,8,3,5]
print(data)

revindex = len(data)-1
for i in range(len(data)):
    if revindex < i:
        break
    temp = data[i]
    data[i] = data[revindex]
    data[revindex] = temp
    revindex -= 1
    
print(data)