'''
Kieran Burnett
'''

# Get a count indicating the amount of temperature reading that are below zero

## Counts the number of negative floats in a list.
## INPUT: temperature_list -> A list containing seven floats of any value.
## OUTPUT: A interger representing the number of negative values in the input list
def negative_temperatures_counter(temperature_list: list[float]) -> int:
    output_count = 0 
    for reading in temperature_list:
        if reading < 0.0:
            output_count += 1
    return output_count

# TESTING
## Test cases
test1 = [1,0,1,1,0,1,1]
test2 = [-1,-1,-1,-1,-1,-1,-1]
test3 = [-1,1,0,-1,0,1,-1]
tests = [test1,test2,test3] 

## Expected test result
test_ex = [0,7,3]

## test loop
for count in range(0,3):
    result = negative_temperatures_counter(tests[count])
    assert result == test_ex[count], f'expected {test_ex[count]} but got {result}'