# TMA02 Q2b Kieran Burnett KB26678

# Add up the decimal values in the new list
## Initialise the input values
# INPUT: the weighted tma scores, a list of one or more floats in the range 0.0 to 100.0
weighted_tma_scores = [16.25,20.25,18.00,22.50]
score_total = 0

## Aggregate the weighted list values
for score in weighted_tma_scores:
    score_total += score

# OUTPUT: The rounded aggregated weighted tma scores 
print(round(score_total))