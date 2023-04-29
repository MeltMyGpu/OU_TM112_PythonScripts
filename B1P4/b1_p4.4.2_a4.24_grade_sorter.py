# Print the grade, given the marks as input

# Input: The marks given for a student, in range 0-100 inclusive
marks = 60

# Find the grade by testing case ranges
if marks < 40:
    grade = 'fail'

if 40 <= marks <= 60:
    grade = 'pass'
    
if 60 < marks < 80:
    grade = 'merit'
    
if marks >= 80:
    grade = 'distinction'
    
# Output: The grade as a string.
print(f"The grade is {grade}")