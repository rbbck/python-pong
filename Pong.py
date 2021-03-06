# based on @TokyoEdTech, but with some modifications that I would do

import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# controller definition
class controller(turtle.Turtle):
    def __init__(self, id, xPos, yPos):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xPos, yPos)

# ball definition
class ball(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0,0)

# "instantiate" both controllers
controllerA = controller("1", -350, 0)
controllerB = controller("2", 350, 0)

# "instantiate" the ball
ball = ball()

# the speed of the ball
movespeed = 0.2
movespeedX = movespeed
movespeedY = movespeed

# score
scoreA = 0
scoreB = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)

# displays the score on the screen
def displayScore():
    score.clear()
    score.write("Player A: "+str(scoreA)+" Player B: "+str(scoreB), align="center", font=("Courier", 24, "normal"))
displayScore()

def playSound():
    os.system("aplay touch.wav&")

# move functions
def move1UP():
    y = controllerA.ycor()
    y += 20
    controllerA.sety(y)

def move1DOWN():
    y = controllerA.ycor()
    y -= 20
    controllerA.sety(y)

def move2UP():
    y = controllerB.ycor()
    y += 20
    controllerB.sety(y)

def move2DOWN():
    y = controllerB.ycor()
    y -= 20
    controllerB.sety(y)

# keyboard binding
window.listen()
window.onkeypress(move1UP, "w")
window.onkeypress(move1DOWN, "s")
window.onkeypress(move2UP, "Up")
window.onkeypress(move2DOWN, "Down")

# loop
while True:
    window.update()

    # move the ball
    ball.setx(ball.xcor() + movespeedX)
    ball.sety(ball.ycor() + movespeedY)

    # ball | border collision checking
    if(ball.ycor() > 290):
        ball.sety(290)
        movespeedY *= -1
        playSound()

    if(ball.ycor() < -290):
        ball.sety(-290)
        movespeedY *= -1
        playSound()

    if(ball.xcor() > 390):
        ball.goto(0,0)
        movespeedX *= -1
        scoreA += 1
        displayScore()
        playSound()

    if(ball.xcor() < -390):
        ball.goto(0,0)
        movespeedX *= -1
        scoreB += 1
        displayScore()
        playSound()

    # ball | player collision checking

    if ball.xcor() > 340 and ball.ycor() < controllerB.ycor() + 50 and ball.ycor() > controllerB.ycor() - 50:        
        ball.setx(340)
        movespeedX *= -1   
        playSound() 

    elif ball.xcor() < -340 and ball.ycor() < controllerA.ycor() + 50 and ball.ycor() > controllerA.ycor() - 50:
        ball.setx(-340)
        movespeedX *= -1    
        playSound()