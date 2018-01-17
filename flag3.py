# using the SimpleGraphics library
from SimpleGraphics import *

# use the random library to generate random numbers
import random

# size of the circles
diameter = 20


##
# sets the name of the output window
# sets the size of the output window
#
# you can change these
##
setWindowTitle("Flag of Poland")
resize(500,400)




##
# returns a vaid color based on the input coordinates for the flag of Poland
# The Polish flag is two horizontal bars: the top bar is white and
# the bottom is red. They each occupy 1/2 of the flag.
#
# @param x is an x-coordinate 
# @param y is a y-coordinate 
# @return a colour based on the input x,y values for the given flag
##
def define_colour(x,y):
  if y<getHeight()/2:
    c = 'white'
  else:
    c = 'red'

  return c



# repeat until window is closed
# do NOT change anything in this while loop
while not closed():

  # generate random x and y values 
  x = random.randint(0, getWidth())
  y = random.randint(0,getHeight())

  # set colour for current circle
  setFill( define_colour(x,y) )

  # draw the current circle
  ellipse(x, y, diameter, diameter)