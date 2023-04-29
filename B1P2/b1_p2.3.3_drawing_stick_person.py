from turtle import *

# Draw a stick person
speed(1)
## Draw the head
for sides in range(4):
    forward(40)
    left(90)
    
## draw top of torso
penup()
forward(20)
right(90)
pendown()
forward(30)

## Draw arms
penup()
right(90)
forward(50)
right(180)
pendown()
forward(100)

## Draw rest of torso
penup()
right(180)
forward(50)
left(90)
pendown()
forward(50)

##Draw legs
### Draw left leg
right(30)
forward(60)
penup()
right(180)
forward(60)

### draw right leg
right(120)
pendown()
forward(60)

input()