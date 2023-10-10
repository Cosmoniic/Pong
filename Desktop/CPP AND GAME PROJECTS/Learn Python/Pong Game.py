import turtle

#set the window up

wn = turtle.Screen()
wn.setup(width=1400, height=900)
wn.bgcolor("yellow")
wn.title("Pong Game by Cosmosityyy")
wn.tracer(0)


#first paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=10,stretch_len=2)
paddle_1.color("magenta")
paddle_1.penup()
paddle_1.goto(-640,0)

#second paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=10,stretch_len=2)
paddle_2.color("magenta")
paddle_2.penup()
paddle_2.goto(640,0)

#the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(2,2)
ball.penup()
ball.color("magenta")
ball.goto(0,0)
ball.dx=0.4
ball.dy=0.4

#scoreboard intialisation
score_1=0
score_2=0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("magenta")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,410)
scoreboard.write("Player 1: 0  Player 2: 0", align="center", font=("courier",24,"normal"))



#functions
def paddle_1_up():
    y=paddle_1.ycor()
    y+= 20
    paddle_1.sety(y)

wn.listen()
wn.onkeypress(paddle_1_up,"w")

def paddle_1_down():
    y=paddle_1.ycor()
    y-=20
    paddle_1.sety(y)

wn.listen()
wn.onkeypress(paddle_1_down,"s")

def paddle_2_up():
    y=paddle_2.ycor()
    y+=20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_2_up,"u")

def paddle_2_down():
    y=paddle_2.ycor()
    y+=-20
    paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_2_down,"n")



while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #border checking

    if ball.ycor()>440:
        ball.sety(440)
        ball.dy*=-1

    if ball.ycor()<-440:
        ball.sety(-440)
        ball.dy*=-1

    #player 1 score
    if ball.xcor()>680:
        ball.goto(0,0)
        ball.dx*=-1
        score_1+=1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier",24,"normal"))


    #player 2 score
    if ball.xcor()<-680:
        ball.goto(0,0)
        ball.dx*=-1
        score_2+=1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("courier",24,"normal"))

    if paddle_1.ycor()>350:
        paddle_1.sety(350)
    
    if paddle_1.ycor()<-350:
        paddle_1.sety(-350)
    
    if paddle_2.ycor()>350:
        paddle_2.sety(350)
    
    if paddle_2.ycor()<-350:
        paddle_2.sety(-350)

    if (ball.xcor()>630 and ball.xcor()<670) and (ball.ycor()<paddle_2.ycor()+90 and ball.ycor()>paddle_2.ycor()-90):
        ball.setx(630)
        ball.dx*=-1

    if(ball.xcor()<-630 and ball.xcor()>-670) and (ball.ycor()<paddle_1.ycor()+90 and ball.ycor()>paddle_1.ycor()-90):
        ball.setx(-630)
        ball.dx*=-1