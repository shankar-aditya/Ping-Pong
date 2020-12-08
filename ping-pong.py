import turtle 

win = turtle.Screen() 
win.title("Pingpong by Aditya")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=0.53)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  PlAYER B: 0", align="center", font=("Courier", 24, "normal"))

#Function to move paddle up or down
def paddle_a_up():
    if(paddle_a.ycor()<250):
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    if(paddle_a.ycor()>-250):
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    if(paddle_b.ycor()<250):
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if(paddle_b.ycor()>-250):
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

#Keyboaed binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
    win.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #If ball touches top or bottom boundary
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    #If ball crosses right or left boundary
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  PlAYER B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  PlAYER B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Paddle and ball collision
    #If the player hits the ball
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()<paddle_b.ycor()+70 and ball.ycor()>paddle_b.ycor()-70):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()<-340 and ball.xcor()>-350 ) and (ball.ycor()<paddle_a.ycor()+70 and ball.ycor()>paddle_a.ycor()-70):
        ball.setx(-340)
        ball.dx *= -1