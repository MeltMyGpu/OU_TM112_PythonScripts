
'''
Kieran Burnett
19 jun 2023
Extracts data from cvs files and calulates the correlation coefficient
'''

import os
# Imports
from table_utils import *
from stats_utils import *
# load input data
happ_data = to_float(load('geog_2.txt'))
mort_data = to_float(load('mort_1.txt'))
# Init varaibles
happ_out = []
mort_out = []
happ_index = 0
# Extract authoirty names
happ_auths = cols(happ_data,1,1)
mort_auths = cols(mort_data,0,0)
# Find matching data from inputs
for auth in happ_auths:
    if mort_auths.count(auth) > 0:
        mort_index = mort_auths.index(auth) 
        happ_out.append(happ_data[happ_index][2])
        mort_out.append(mort_data[mort_index][1])
    happ_index += 1
# Get correlation coefficient
x = corr_coef(happ_out, mort_out)
print(x)
        
