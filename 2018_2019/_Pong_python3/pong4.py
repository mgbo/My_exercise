
# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech
# Part 4: Moving the ball

import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball_dx = 2 # every time our ball moves by two pixels
ball_dy = 2

# Function
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

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
	wn.update()	

	# Move the ball
	ball.setx(ball.xcor() + ball_dx)
	#print (ball.xcor())
	ball.sety(ball.ycor() + ball_dy)

	# # Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball_dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball_dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball_dx *= -1

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball_dx *= -1
