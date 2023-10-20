import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = 50  
TEXT_Y = 0  

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

stop_sign = turtle.Turtle()
stop_sign.speed(ANIMATION_SPEED)

stop_sign.penup()
stop_sign.goto(0, -diameter / 2)
stop_sign.pendown()

for _ in range(NUM_SIDES):
    stop_sign.forward(LENGTH)
    stop_sign.left(ANGLE)

stop_sign.penup()
stop_sign.goto(TEXT_X, TEXT_Y)
stop_sign.write("STOP", align="center", font=("Arial", 20, "bold"))

turtle.exitonclick()

turtle.done()
