# using the SimpleGraphics library
from SimpleGraphics import *

# tell SimpleGraphics to only draw when I use the update() function
setAutoUpdate(False)


# use the random library to generate random numbers
import random


# size of the circles drawn
diameter = 15

resize(600, 300)


##
# returns a vaid color based on the input coordinates
#
# @param x is an x-coordinate 
# @param y is a y-coordinate 
# @return a colour based on the input x,y values for the given flag
##
def define_colour(x,y):
  x1 = getWidth()/3
  y1 = 0
  x2 = 0
  y2 = getHeight()
  m1 = (y2-y1)/(x2-x1)
  c = y2 - x2*m1
  
  x3 = 2*getWidth()/3
  y3 = 0
  x4 = 0
  y4 = getHeight()
  m2 = (y4 - y3)/(x4 -x3)
  d = y4 - x4*m2
  
  x5 = getWidth()
  y5 = getHeight()/3
  x6 = 0
  y6 = getHeight()
  m3 = (y6 - y5)/(x6 - x5)
  e = y6 - x6*m3

  x7 = getWidth()
  y7 = 2*getHeight()/3
  x8 = 0
  y8 = getHeight()
  m4 = (y8 - y7)/(x8 - x7)
  f = y8 - x8*m4


  if y <= (m1*x + c):
    return 'blue'
  if y <= (m2*x + d) and y >= (m1*x + c):
    return 'yellow'
  if y <= (m3*x + e) and y >= (m2*x + d):
    return 'red'
  if y <= (m4*x + f) and y >= (m3*x + e):
    return 'white'
  if y >= (m4*x + f):
    return 'green'





######################################################################
#
# Do NOT change anything below this line
#
######################################################################

# repeat until window is closed
while not closed():
  for i in range(500):
    # generate random x and y values 
    x = random.randint(0, getWidth())
    y = random.randint(0, getHeight())

    # set colour for current circle
    setFill( define_colour(x,y) )

    # draw the current circle
    ellipse(x, y, diameter, diameter)

  update()
