# write a void (non-fruitful) function to draw a squ are
# this means that the function does something, as oposed to returning a specific value 
# use it in a program to draw the image shown below
# assume each side os 20 units
# notice the turtle has already moved away from the last square when the program ends 

import turtle
import math 

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("pink","blue")
tess.pensize(3)

tess.write("Hello")

xs = [48, 117, 200, 240, 160, 260, 220, -45, -60]
# draw a simple rectangle of that height, with a fixed width 

def draw_bar(t, height):
    # get turtle t to draw one bar, of height "
    if height > 200:
        tess.color("pink","red")
    elif height >= 100 and height <= 200:
        tess.color("pink","yellow")
    else:
        tess.color("pink","green")
    t.pendown()
    t.begin_fill()
    if height < 0:
        t.write(' ' + str(height))
    t.left(90)
    t.forward(height) # left side 
    if height >= 0:
        t.write(' ' + str(height))
    t.right(90)
    t.forward(40) # width of bar along the top 
    t.right(90)
    t.forward(height) # and down again 
    t.left(90) # put the turtle facing the way we found it 
    t.end_fill()
    t.penup()
    t.forward(10) # leave small gap after each bar 
   
    
for v in xs:
    draw_bar(tess, v)
# writing this by itself is already 'activating' the function 

# modify this program so that the bar for any value of 200 or more is filled with red
# > 200 = red 
# 100 - 200 = yellow 
# < 100 = green 

#moving on now because it doesn't make sense to keep troubleshooting this one
# write a void function -- which means a function that DOES something as opposed to returns a value# draw_equitriangle(t, sz) which calls from
# draw_poly from the previous question to have its turtle draw an equilateral triangle

# so remember, draw_poly first was 
def draw_poly(t, n, sz):
    # wh ere t is your turtle and had to be defined before
    # n is the sides you want your polygon to have
    # sz is the steps / length of the sides 
    # so if you want to draw a triangle it will look like this 
    for i in range (1,n):
        t.forward(sz)
        t.left(360/n)
    t.forward(sz)

#draw_poly(tess, 3, 20)

# draw_poly(tess, 10, 30)

# ok now we know our draw_poly works 
# let's create another function using variables (t, sz) which calls on draw_polcy to have a turtle draw an equilateral triangle

def draw_equitriangle(t, sz):
    n = 4 
    draw_poly(t, n, sz)
    
# draw_equitriangle(tess,30)

# write a fruitful function - so now something that bears a value, or fruit - to return the sum of all integers up to and including next
# so sum_to(10) would be 1+2+3+4+5+6+7
def sum_to(x):
    sum = 0 
    for i in range(x):
        sum += i 


wn.mainloop()
 
# if you do this, Tess spins for 3645 degrees total,
# 3645 % 360 will give you the final orientation she has from the starting point 
