# Determine the TM112 result

# INPUT: the grade score for TMA03, a positive integer in the range 0 to 100 inclusive.
tma03 = 42
# INPUT: the average score of prevouis TMAs, a positive floating-point number in the range 0.0 to 100.0 inclusive.
average = 73.5

## Test exclusive cases to obtain TM112 result.
if (tma03 < 30) or (average < 40.0):
    result = 'fail'
elif (tma03 >= 30) and (40 <= average < 85.0 ):
    result = 'pass'
else:
    result = 'distinction'

# OUTPUT: The obtained result in a formatted string message.
print(f'The student got a {result}')









### TESTING PURPOSES  
def get_result(tma03:int, average:float):
    if (tma03 < 30) or (average < 40.0):
        result = 'fail'
    elif (tma03 >= 30) and (40 <= average < 85.0 ):
        result = 'pass'
    else:
        result = 'distinction'
    return result

### init all test values and expected results
tma03_test_values = [29,30,31,29,30,31]
average_test_values = [39.9,40.0,40.1,84.9,85.0,85.1]
expected_results = ['fail','pass','pass','fail','distinction','distinction']

### testing loop
for test in range(6):
    # get and set this tests values
    tma03 = tma03_test_values[test]
    average = average_test_values[test]
    expected = expected_results[test]
    actual = get_result(tma03,average)

    ## Test agasint fucntions return
    assert actual == expected , f'Test number {test} failed, expected value \'{expected}\' but got value \'{actual}\''
