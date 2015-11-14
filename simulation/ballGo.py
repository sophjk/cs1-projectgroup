# Try to get the ball in the hoop

import runWorld as rw
import drawWorld as dw
import pygame as pg

# Initialize world
name = "Aim, click, and shoot the ball!"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("basketballimage.png")

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(myimage, (state[0], state[2]))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    return((state[0]+state[1]),state[1], (state[2] + state[3]), state[3])

################################################################

def endState(state):
    if (state[0] > width or state[0] < 0 or state[2] < 0 or state[2] > height):
        return True
    else:
        return False


################################################################

def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) == 1:
            newState = -1
        else:
            newState = 1   
        return((state[0],newState))
    else:
        return(state)

################################################################

# The cat starts at the left, moving right 
initState = (0,1,300,-1)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
