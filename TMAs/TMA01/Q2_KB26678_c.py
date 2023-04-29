# 23/04/09 - TM112 - TMA01 - Kieran_Burnett - KB26678   
from turtle import *
# draw a frieze pattern
# Set starting values
number_of_elements = 4
spoke_count = 6
spoke_length = 50
spoke_angle = 36
element_spacing = 125

for element in range(number_of_elements):
    left(180)
    ## Draw element of pattern
    for spoke in range(spoke_count):
        forward(spoke_length)
        penup()
        right(180)
        forward(spoke_length)
        left(180-spoke_angle)
        pendown()
    ## Move to start of next element
    left(spoke_angle)
    penup()
    forward(element_spacing)
    pendown()

