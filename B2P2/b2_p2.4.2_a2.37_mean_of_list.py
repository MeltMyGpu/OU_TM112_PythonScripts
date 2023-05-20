'''
Kieran Burnett
First is using my deconstruction
'''
# Calculate the mean of a given list of daily temperatures
# INPUT: Temperature list, A list conatining seven floats of any value, all in the same units
weekly_temperatures = [1,2,3,4,5,6,7]

## get the sum of the list
list_sum = 0
for item in weekly_temperatures:
    list_sum += item
    
## calculate the mean of the list
list_mean = list_sum / (len(weekly_temperatures))
## Output results
print(f'The mean temperature is {list_mean}')

'''
This is using the textbook decosruction
'''
list_sum = 0
list_mean = 0
length = 0
## get sum of the list
for item in weekly_temperatures:
    list_sum += item
    ## get length of the list
    length += 1
## calculate the mean of the list
list_mean = list_sum / (length)

print(f'The mean temperature is {list_mean}: book way')