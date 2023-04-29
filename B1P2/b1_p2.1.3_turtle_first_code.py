from turtle import *
# All exercises require a fresh turtle, cannot be ran together.

# Draw a step of a staircase
def draw_step():
    forward(40)
    left(90)
    forward(40)
    right(90)

# Draws L shape 2.1.4 pg.92
def draw_l():
    right(90)
    forward(50)
    left(90)
    forward(30)


# Draw square, A2.5 pg.93
def draw_square(x:int):
    for i in range(4):
        forward(x)
        left(90)


# Draw triangle A2.6 pg.93
def draw_triangle(x:int):
    pendown()
    for i in range(3):
        forward(x)
        left(120)
    penup()

# Activity 2.11: three triangles
def three_triangles(x:int):
    penup()
    #tri 1 
    left(90)
    forward(100)
    right(90)
    draw_triangle(x)
    #tri 2
    right(90)
    forward(100)
    left(90)
    draw_triangle(x)
    #tri 3
    forward(100)
    draw_triangle(x)

## main
three_triangles(60)
x = input()

# for x in range(4):
    # draw_step()
