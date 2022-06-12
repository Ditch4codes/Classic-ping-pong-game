import turtle
import time

wn= turtle.Screen()
wn.title=("Simple ping pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)



# paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.goto(350,0)


# ball
ball1= turtle.Turtle()
ball1.speed("slowest")
ball1.shape("circle")
ball1.color("white")
ball1.penup()
ball1.goto(0,0)
ball1.dx=2
ball1.dy=-2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

# score
score_a=0
score_b=0


# functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    wn.update()


    # move the ball
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)
    time.sleep(0.01)
    

     # border checking
    if ball1.ycor() > 290:
        ball1.sety(290)
        ball1.dy*=-1

    if ball1.ycor() < -290:
        ball1.sety(-290)
        ball1.dy*=-1    
    
    if ball1.xcor() > 390:
        ball1.goto(0,0)
        ball1.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    if ball1.xcor() < -390:
        ball1.goto(0,0)
        ball1.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))


    # paddle-ball collision
    if (ball1.xcor() < -340 and ball1.xcor() >-350) and (ball1.ycor() < paddle_a.ycor()+50 and ball1.ycor() > paddle_a.ycor()-50):
        ball1.setx(-340)
        ball1.dx*=-1    

    if (ball1.xcor() > 340 and ball1.xcor() < 350) and (ball1.ycor() < paddle_b.ycor()+50 and ball1.ycor() > paddle_b.ycor()-50):
        ball1.setx(340)
        ball1.dx*=-1
