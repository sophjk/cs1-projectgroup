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
pg.mixer.init
myfont = pg.font.SysFont("monospace", 15)
swish = pg.mixer.Sound("swish.wav")
boo = pg.mixer.Sound("boo.wav")
rim_sound = pg.mixer.Sound("rim.wav")
#basket_hoops = 0
#hoop_height = 150

################################################################

# Display the state by drawing a ball at that x coordinate
ballimage = dw.loadImage("basketballimage.png")
hoopimage = dw.loadImage("hoop.png")

def updateDisplay(state):

    dw.fill(dw.white)
    dw.draw(ballimage, (state.x, state.y))
    dw.draw(hoopimage, (400, state.hoop))
    Score = 'Score: ' + str(state.pts)
    label = dw.makeLabel(Score, 'helvetica', 30, (0, 0, 0))
    dw.draw(label, (220, 420))


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state.x, and delta-pos
# as state.dx. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state

def updateState(state):
    ball_rect = ballimage.get_rect()
    ball_width = ball_rect.width
    half_bw = ball_width / 2
    hoop_rect = hoopimage.get_rect()
    rim = 500 - hoop_rect.width
    hoop_height = state.hoop
    if(state.y < 0):
        #ball bounce when hits top
        switchState = ((state.dy) * (-1))
        state.x = state.x + state.dx 
        # state.dx = state.dx
        state.y = (state.y + switchState)
        state.dy = switchState
        # state.pts = state.pts
        # state.hoop = state.hoop
    
    elif((rim + 30) <= (state.dx)  <= 500 and (hoop_height - 10) <= state.y <= (hoop_height + 2)):
         #they scored
       # label = myfont.render("Your Score: " + str(state.pts + 1), 1, (0,0,0))
       # screen.blit(label, (10,10))
        swish.play()
        print("nice")
        print(state.pts + 1)
        new_hoop_height = randint(100, 400)
        state.pts = state.pts + 1
        state.hoop = new_hoop_height
    elif ((rim - 10) <= (state.x + half_bw) <= (rim + 20) and
          (hoop_height - 5) <= state.y <= (hoop_height + .5)):
        rim_sound.play()
        print("brick")
        state.x = 0
        state.dx = 0
        state.y = 250
        state.dy = 0
        state.pts = 0

    elif(state.x >= 500):
        #they missed air ball
        boo.play()
        print("booo")
        print(0)
        state.x = 0
        state.dx = 0
        state.y = 250
        state.dy = 0
        state.pts = 0
        
        #return (0, 0, 250, 0, basket_hoops, hoop_height)
    else:
        state.x = state.x + state.dx
        state.y = state.y + state.dy
    return state
  
    
################################################################

def endState(state):  
    if (state.x < 0):
        return True
        
    else:
        return False
    


################################################################


def handleEvent(state, event):
    if (event.type == pg.KEYDOWN and event.key == pg.K_UP):
        if (state.x == 0 and state.y > 10):
           # newState2 = -10
           state.y -= 10
       # else:
           # newState2 = 0
          # state.y = state.y + 10
            
           # state.y = state.y + newState2

    elif (event.type == pg.KEYDOWN and event.key == pg.K_DOWN):
        if (state.x == 0 and state.y < 450):
           # newState2 = +10
           state.y += 10
       # else:
       #     newState2 = 0
       #     state.y = state.y + newState2
    elif (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
        state.dx = 10
        state.dy = -10
      #  if (state.dx) == 0:
       #     newState1 = 1.5
       # else:
       #     newState1 = 0
       #     state.dx = newState1
       #     state.dy = newState1*-1

    elif (event.type == pg.KEYDOWN and event.key == pg.K_q):
        #end the game with an event by moving the ball to an
        #expect position less than 0
        state.x = -1 
    
    return state
    
#hoop_height = 150
# The ball starts
#initState = (0, 0, 250, 0, 0, 150)

class State:
    def __init__(self, x, dx, y, dy, pts, hoop):
        self.x = x #0
        self.dx = dx #0
        self.y = y  #250
        self.dy = dy #0
        self.pts = pts #0
        self.hoop = hoop #150

initState = State(0, 0, 250, 0, 0, 150)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
