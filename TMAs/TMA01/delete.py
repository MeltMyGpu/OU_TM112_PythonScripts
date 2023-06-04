input_list1 = [0, 3, 5, 7, 5, 4, 2, 0, -0.2, 22]
input_list = [5, 4, 2, 22]

# get count of out of range values
count = 0
for number in input_list:
    if (0.0 > number) or (5.0 < number):
        count += 1

# get percentage if any out of range exist
percentage = 0
if count > 0:
    percentage = ((count / len(input_list)) * 100)

# round down
import math
percentage = math.floor(percentage)
# output
print(f'{percentage} % of values are outside the range')