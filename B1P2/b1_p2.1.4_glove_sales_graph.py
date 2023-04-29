# Produc graph for gloves sales
from turtle import *

# Set up varibles
gloves1 = 10
gloves2 = 8
glovesSales = [10,8,4,5]

# makes x axis
goto(80,0)

#make y axis
goto(0,0)
goto(0,100)

#plot data
goto(0,0)
x = 20
for data in glovesSales:
    goto(x, data*10)
    x += 20
    
input()
