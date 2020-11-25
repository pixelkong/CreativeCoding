"""
Created on Tue Nov 24 17:46:05 2020

@sazamore: Dr. Z
ATLAS Institute at CU Boulder

Just a lil somethin to play around with sound response. 
Using my module, soundResponse!
"""
import soundResponse as SR
import turtle


panel = turtle.Screen()
panel.clear()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.setworldcoordinates(0, w, h, 0) 
turtle.update()  
turtle.tracer(0)


circ = turtle.Turtle(shape='circle')
circ.up()
circ.goto(300,300)

intro = turtle.Turtle(visible=False)
intro.up()
intro.color('violet')
intro.goto(50,50)
intro.write("Press the 's' key to start",align='left',font=('courier',30))

music = SR.Ctrlr('tech.wav') # create object
run = True

def stop():
    '''callback function that stops animation while it's running'''
    global run
    run = False

def go():
    '''Callback function that plays sound and does entire animation'''
    global run,intro
    intro.clear()
    panel.update()
    music.start() # start song
    
    while run:
        amp = music.getCurrAmp()[0]/1000 #work only with the first value returned, the amplitude
        circ.shapesize(amp) 
    #    print(amp)
    
        if amp > 3:
            circ.color('lightblue','lightblue') #turn light color if really loud.
        else:
            circ.color('black','black')
    
        turtle.update()
        
        # quit the while loop when the song ends
        if amp ==-1:
            run = False
        panel.onkey(stop,'s')

panel.onkey(go,'s')
turtle.listen()
        
turtle.done()