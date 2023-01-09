import turtle
import winsound

# Score

Score_A = 0
Score_B = 0

wn = turtle.Screen()
wn.title("MIduk.techEd")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("magenta")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

# function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # paddles' movement boundary
    paddle_a.sety(paddle_a.ycor())
    paddle_b.sety(paddle_b.ycor())

    # bounch the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font=("courier", 24, "normal"))
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        Score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(Score_A, Score_B), align="center", font=("courier", 24, "normal"))

# paddle collision

    if (ball.xcor() > 330 and ball.xcor() < 335) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif (ball.xcor() < -330 and ball.xcor() > -335) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    elif paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    elif paddle_b.ycor() > 250:
        paddle_b.sety(250)
    elif paddle_b.ycor() < -250:
        paddle_b.sety(-250)

