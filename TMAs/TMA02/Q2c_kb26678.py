# TMA02 Q2c Kieran Burnett Kb26678

# Determine the weighted scores of the provided TMA results.

## initialise the variables.
# INPUT: tma scores, a list of one or more integers that are in the range (0-100).
tma_scores = [65,81,72,51]
tma_weighted_scores = []

## calculate the tma weighting as a float in range 0.0-1.0 representing a percentage .
weight_percentage = 1 / len(tma_scores)

## Construct the new list of weighted scores.
for score in tma_scores:
    tma_weighted_scores.append(score * weight_percentage)

## Aggregate the weighted list values
score_total = 0
for score in tma_weighted_scores:
    score_total += score

# OUTPUT: The aggregated weighted tma scores rounded to nearest whole number 
print(round(score_total))


'''
# This line also performs the same fucntion as the above code
print(round(sum(tma_scores)/ len(tma_scores)))
'''