# TMA02 Q2c Kieran Burnett Kb26678

# Determine the weighted scores of the provided TMA results.

## initialise the variables.
# INPUT: tma scores, a list of one or more integers that are in the range (0-100).
tma_scores = [65,81,72,78]
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

# OUTPUT: The rounded aggregated weighted tma scores 
print(round(score_total))


### I have also provided a more efficient version of this code below
# def get_tma_wieghted_score(tma_scores :list[int]) -> int:
#     """Returns the weighted average score of the input score list, as an integer rounded to the nearest whole number"""
#     # set up required variables 
#     tma_weighted_scores = []
#     score_total = 0
#     # Get the tma weighting
#     weight_percentage = 1 / len(tma_scores)
#     # get the weighted scores and aggregate them
#     for score in tma_scores:
#         score_total += score * weight_percentage
#     # OUTPUT: The weighted  average score rounded to the nearest whole number, an integer in the range 0 to 100
#     return round(score_total)

# print(get_tma_wieghted_score(tma_scores))