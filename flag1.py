# using the SimpleGraphics library
from SimpleGraphics import *

# use the random library to generate random numbers
import random

diameter = 15


##
# returns a valid colour based on the input coordinates
#
# @param x is an x-coordinate 
# @param y is a y-coordinate 
# @return a colour based on the input x,y values for the given flag
##
def define_colour(x,y):
  ##(x-(xcoordinate of circle centre))**2 + ((y-(ycoordinate of circle centre))
  # < R**2
  if ((((x - (getWidth()/2))**2) + ((y - (getHeight()/2))**2))) < (((getHeight()/2)-(getHeight()/5))**2):
    colour = "red"
  else:
    colour = "white"
  # add your code to this method and change the return value
  # This is the ONLY place you should modify this file
  # (except for maybe changing the size of the graphics window)
  ##
  return colour


# repeat until window is closed
while not closed():

  # generate random x and y values 
  x = random.randint(0, getWidth())
  y = random.randint(0,getHeight())

  # set colour for current circle
  setFill( define_colour(x,y) )

  # draw the current circle
  ellipse(x, y, diameter, diameter)
