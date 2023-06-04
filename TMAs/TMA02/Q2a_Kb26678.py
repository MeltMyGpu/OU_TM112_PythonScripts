# TMA02 Q2a Kieran Burnett Kb26678

# Determine the weighted scores of the provided TMA results.

## initialise the variables.
# INPUT: tma scores, a list of one or more integers that are in the range (0-100).
tma_scores = [65,81,72,90]
tma_weighted_scores = []

## calculate the tma weighting as a float in range 0.0-1.0 representing a percentage .
weight_percentage = 1 / len(tma_scores)

## Construct the new list of weighted scores.
for score in tma_scores:
    tma_weighted_scores.append(score * weight_percentage)

## OUTPUT: The constructed list of weighted tma scores
print(tma_weighted_scores)