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

# Display the state by drawing a ball at that x coordinate
myimage = dw.loadImage("basketballimage.png")
ballimage = dw.loadImage("hoop.png")

def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(myimage, (state[0], state[2]))
    dw.draw(ballimage, (380,200))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
'''
def updateState(state):
    return((state[0]+state[1]), state[1], (state[2] + state[3]), state[3])
'''
def updateState(state):
    if(state[2] < 0 or state[2] > height):
        switchState = ((state[3]) * (-1))
        return((state[0] + state[1]),
               state[1], (state[2] + switchState), switchState)
    else:
        return((state[0] + state[1]),
               state[1], (state[2] + state[3]), state[3])
################################################################

def endState(state):
    if (state[0] > width or state[0] < 0):
        return True
    else:
        return False


################################################################

def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.KEYUP and event.key == pg.K_SPACE):
        if (state[1]) == 0:
            newState = 1
        return((state[0], newState, state[2],(newState*-1) ))
    else:
        return(initState)

################################################################

# The ball starts  
initState = (0,0,250,0)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
