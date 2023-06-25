'''
Kieran Burnett - 25/06/23 - TMA02 Q4c Part III
'''

def calculate_painting_pricing_estimation(surface, price_per_gallon) -> float:
    ''' 
    Calculates the estimated cost of a painting job using internal CONST values.
        INPUT: surface -> (non-zero, non-negative, integer) The surface area in metres squared of the wall that is to be painted.
        INPUT: price_per_gallon -> (non-zero, non-negative, float, rounded to 2 decimal places) The cost in pounds sterling per gallon of paint.
        OUTPUT: estimated_cost -> (non-zero, non-neagtive, float, rounded to 2 decimal places) The estimated cost of the painting job.
    '''
    # Init const values
    METER_PER_GALL = 60
    HOUR_PER_GALL = 5
    LABOUR_PER_HOUR = 32.50
    PERSONAL_NUMBER = 1.01750
    
    # Calculate material costs
    required_gallons_paint = surface / METER_PER_GALL
    cost_paint = required_gallons_paint * price_per_gallon
    
    # Calculate labour costs
    labour_hours = HOUR_PER_GALL * required_gallons_paint
    cost_labour = labour_hours * LABOUR_PER_HOUR
    
    # Calculate total cost
    estimated_cost = PERSONAL_NUMBER * (cost_labour + cost_paint)
    
    return round(estimated_cost,2) 


result = calculate_painting_pricing_estimation(360,14.00)
print(result)
assert result == 1077.51
