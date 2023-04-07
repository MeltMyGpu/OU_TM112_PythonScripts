# Draw triangles across page
from turtle import *

number_of_shapes = 4

for shape in range(number_of_shapes):
    # draw triangle
    for sides in range(3):
        forward(40)
        left(180-60)
    
    # Move to next start pos
    penup()
    forward(50)
    pendown()