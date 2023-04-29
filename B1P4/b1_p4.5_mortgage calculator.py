# work out the monnthly repayments for a mortgage

# INIT
# INPUT: mortgage, the amount borrowed, a positive number in units pounds
mortgage = 151_700
# INPUT: rate, the monthly percentage rate of interest on the motgage, based on the yearly interest rate, a float in range 0.0-1.0 
rate = 0.044 / 12
# INPUT: paymenyt, the amount paid by the loan holder each month, positive number in units pounds
payment = 820
month = 0

## main loop
while( mortgage > 0 ):
    mortgage += mortgage * rate
    mortgage = mortgage - payment
    print(f"Outstanding {mortgage}")
    month += 1
    
print(month/12)