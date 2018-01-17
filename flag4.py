# using the SimpleGraphics library
from SimpleGraphics import *

# tell SimpleGraphics to only draw when I use the update() function
setAutoUpdate(False)


# use the random library to generate random numbers
import random
import math


# size of the circles drawn
diameter = 15

resize(600, 600)


##
# returns a vaid color based on the input coordinates
#
# @param x is an x-coordinate 
# @param y is a y-coordinate 
# @return a colour based on the input x,y values for the given flag
##
def define_colour(x,y):
  m0 = (getWidth()/3)**2
  a = math.sqrt(m0/2)
  x1 = 0
  y1 = a
  x2 = getWidth() - a
  y2 = getHeight()
  m1 = (y2-y1)/(x2-x1)
  c = y2 - x2*m1

  x3 = a
  y3 = 0
  x4 = getWidth()
  y4 = getHeight() - a
  m2 = (y4 - y3)/(x4 -x3)
  d = y4 - x4*m2
  if y >= (m1*x + c):
    return 'red'
  if y <= (m2*x + d):
    return 'red'
  else:
    return 'white'
  
    
  ##
  # add your code to this method and change the return value
  ##






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
