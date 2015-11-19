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
ballimage = dw.loadImage("basketballimage.png")
hoopimage = dw.loadImage("hoop.png")


def updateDisplay(state):
    dw.fill(dw.white)
    dw.draw(ballimage, (state[0], state[2]))
    dw.draw(hoopimage, (400, 150))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state

def updateState(state):
    if(state[2] < 0):
        switchState = ((state[3]) * (-1))
        return((state[0] + state[1]),
               state[1], (state[2] + switchState), switchState)
    elif((state[0] >= 365) and (state[2] <= 180)) or ((state[0] >= 365 and state[2])):
        switchState1 = ((state[1]) * (-1))
        return((state[0] + switchState1), switchState1, (state[2] - state[3]), (state[3]*-1))
   #elif(state[0] > 350 and state[2] == 150):
        #switchState1 = ((state[1]) * (-1))
        #return((state[0] + switchState1), switchState1, (state[2] +
    elif((state[0] >= 365) and (state[2] >= 120)):
       return((state[0] + state[1]),state[1], (state[2] + state[3]), state[3])
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
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) == 0:
            newState = 1.5
        else:
            newState = 0 
        return((state[0],newState,state[2],(newState*-1)))
    elif (event.type == pg.KEYDOWN and event.key == pg.K_UP):
        if (state[1] and state[3]) == 0:
            newState2 = -10
            state[3] == 0
            state[1] == 0
            state[0] == 0
        else:
            newState2 = -10
            state[3] == 0
            state[1] == 0
            state[0] == 0
        return(state[0],state[1],(state[2] + newState2),state[3])
    elif (event.type == pg.KEYDOWN and event.key == pg.K_DOWN):
        if (state[2]) == 250:
            newState2 = +10
            state[3] == 0
            state[1] == 0
            state[0] == 0
        else:
            newState2 = +10
            state[3] == 0
            state[1] == 0
            state[0] == 0
        return(state[0],state[1],(state[2] + newState2),state[3])
    elif (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
        if (state[1]) == 0:
            newState1 = 1.5
        else:
            newState1 = 0
        return((state[0],newState1,state[2],(newState1*-1)))
    else:
        return(state)
    

# The ball starts
initState = (0, 0, 250, 0)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
