# This is an edited version of what the textbook requested in order to simplify the testing process.
## 

# Program as function
def grade_sorter(marks:int,):
    # Print the grade, given the marks as input
    # Input: The marks given for a student, in range 0-100 inclusive
    # Find the grade by testing case ranges
    if marks < 40:
        grade = 'fail'
    elif 40 <= marks <= 60:
        grade = 'pass'
    elif 60 < marks < 80:
        grade = 'merit'
    elif marks >= 80:
        grade = 'distinction'
    else:
        grade = 'INVALID INPUT'
    return grade

##  Testing function
def test_grade_sorter():
    ## init Test values
    test_marks = [0,39,40,52,60,61,79,80,100]
    test_grade = ['fail','fail','pass','pass','pass','merit','merit','distinction','distinction']
    ## Test
    for test_number in range(len(test_marks)):
        test_input = test_marks[test_number]
        expected = test_grade[test_number]
        actual = grade_sorter(test_input)
        assert expected == actual , f"expected {expected} but got {actual} for the input {test_input}"

## test
test_grade_sorter()
