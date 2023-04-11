from turtle import *

# Draws a house
## A Crap house, but still, counts.

## Draw the walls
for sides in range(4):
    forward(200)
    right(90)

## Draw the roof
left(30)
forward(116)
right(60)
forward(116)

## Draw the door
penup()
right(60)
forward(200)
right(90)
forward(80)
right(90)
pendown()
forward(80)
left(90)
forward(40)
left(90)
forward(80)

## Draw the window
penup()
right(90)
forward(20)
right(90)
forward(60)
pendown()
for side in range(4):
    forward(60)
    left(90)




input()