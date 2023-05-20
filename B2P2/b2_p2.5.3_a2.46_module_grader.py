'''
Kieran burnett
'''
input_scores = [40,20,40,50]
def take_one(input_scores):
    # Compute a students grade based on the mean of the best 3 of 4 scores
    #INPUT: The students scores, a list of 4 integers in the range 0 to 100, with unsumbitted scores as 0
    ## init starting values
    mean_divisor = 3
    sum_of_scores = input_scores[0]
    lowest_index = 0
    ## Compute the sum of the input scores
    for index in range(1, len(input_scores)):
        sum_of_scores += input_scores[index]
        ## find lowest scores index
        if input_scores[index] < input_scores[lowest_index]:
            lowest_index = index
    ## Calculate mean
    sum_of_scores -= input_scores[lowest_index]
    mean = sum_of_scores // mean_divisor
    ## Select student grade
    if mean < 30:
        final_grade = 'fail'
    elif mean < 40:
        final_grade = 'resit'
    else:
        final_grade = 'pass'
    #OUTPUT: The students final grade in a formatted string
    print(f'The studetns final score was {mean}, giving the grade {final_grade}')
    return final_grade

# Computes the mean of the highest 3 integers from input
## Input: input_scores -> List of 4 integers in range 0 - 100 
## Output: an integer representing the computed mean in range 0 - 100
def get_mean(input_scores: list[int]) -> int:
    lowest_index = 0
    sum_of = input_scores[0]
    for index in range(1, len(input_scores)):
        sum_of += input_scores[index]
        if input_scores[index] < input_scores[lowest_index]:
            lowest_index = index
    return (sum_of - input_scores[lowest_index]) // 3

# Computes the grade of the provided mean score
## Input: mean_score -> an interger in the range 0 - 100
## Ouput: a string represnting the computed grade  
def get_grade(mean_score: int) -> str:
    if mean_score < 30:
        return 'fail'
    elif mean_score < 40:
        return 'resit'
    else:
        return 'pass'

# Compute a students grade based on the mean of the best 3 of 4 scores
##INPUT: The students scores, a list of 4 integers in the range 0 to 100, with unsumbitted scores as 0
def take_two(input_scores: list[int]) -> str:
    mean = get_mean(input_scores)
    grade = get_grade(mean)
    print(f'Student avg score {mean}: grade {grade}')
    return grade



##### TESTS
test1 = [30,0,29,30]
test2 = [30,30,29,30]
test3 = [40,20,40,40]
tests = [test1,test2,test3]
test_ex = ['fail', 'resit', 'pass']

for x in range(0, 3):
    exp = test_ex[x]
    act = take_two(tests[x])
    assert exp == act, f'expected: {exp}, got {act}'

