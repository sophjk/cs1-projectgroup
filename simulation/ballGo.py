# Try to get the ball in the hoop lol

import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

# Initialize world
name = "Use the up and down arrow keys, then press space bar."
width = 500
height = 500
rw.newDisplay(width, height, name)
pg.init()
myfont = pg.font.SysFont("monospace", 15)
#basket_hoops = 0
#hoop_height = 150

################################################################

# Display the state by drawing a ball at that x coordinate
ballimage = dw.loadImage("basketballimage.png")
hoopimage = dw.loadImage("hoop.png")

def updateDisplay(state):

    dw.fill(dw.white)
    dw.draw(ballimage, (state[0], state[2]))
    dw.draw(hoopimage, (400, state[5]))
    Score = 'Score: ' + str(state[4])
    label = dw.makeLabel(Score, 'helvetica', 30, (0, 0, 0))
    dw.draw(label, (220, 420))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state

def updateState(state):
    ball_rect = ballimage.get_rect()
    ball_width = ball_rect.width
    half_bw = ball_width / 2
    hoop_rect = hoopimage.get_rect()
    rim = 500 - hoop_rect.width
    hoop_height = state[5]
    if(state[2] < 0):
        #ball bounce when hits top
        switchState = ((state[3]) * (-1))
        return((state[0] + state[1]), 
               state[1], (state[2] + switchState), switchState, state[4], state[5])
    
    elif(rim <= (state[0] + half_bw)  <= 500 and (hoop_height - .5) <= state[2] <= (hoop_height + .5)):
         #they scored
       # label = myfont.render("Your Score: " + str(state[4] + 1), 1, (0,0,0))
       # screen.blit(label, (10,10))
        print("nice")
        print(state[4] + 1)
        new_hoop_height = randint(100, 400)
        return (0, 0, 250, 0, state[4] + 1, new_hoop_height)
    elif(state[0] >= 500):
        #they missed
        print("booo")
        print(0)
        return (0, 0, 250, 0, 0, hoop_height)
        
        #return (0, 0, 250, 0, basket_hoops, hoop_height)
    else:
        return((state[0] + state[1]),
               state[1], (state[2] + state[3]), state[3], state[4], state[5])
################################################################

def endState(state):  
    if (state[0] < 0):
        return True
        
    else:
        return False
    


################################################################

def handleEvent(state, event):
    if (event.type == pg.KEYDOWN and event.key == pg.K_UP):
        if (state[0] and state[2] > 10) == 0:
            newState2 = -10
        else:
            newState2 = 0
        return(state[0],state[1], (state[2] + newState2),state[3], state[4], state[5])
    elif (event.type == pg.KEYDOWN and event.key == pg.K_DOWN):
        if (state[0] and state[2] < 450) == 0:
            newState2 = +10
        else:
            newState2 = 0
        return(state[0],state[1],(state[2] + newState2),state[3], state[4], state[5])
    elif (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
        if (state[1]) == 0:
            newState1 = 1.5
        else:
            newState1 = 0
        return(state[0],newState1,state[2],(newState1*-1), state[4], state[5])
    elif (event.type == pg.KEYDOWN and event.key == pg.K_q):
        #end the game with an event by moving the ball to an
        #expect position less than 0
        return(-1, state[1], state[2], state[3], state[4], state[5])
    else:
        return state
    
#hoop_height = 150
# The ball starts
initState = (0, 0, 250, 0, 0, 150)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
