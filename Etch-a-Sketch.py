import turtle 

tim=turtle.Turtle()
screen=turtle.Screen()

def move_forward():
    tim.setheading(0)
    tim.forward(10)

def move_backward():
    tim.setheading(180)
    tim.forward(10)

def move_up():
    tim.setheading(90)
    tim.forward(10)

def move_down():
    tim.setheading(270)
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="Right", fun=move_forward)
screen.onkey(key="Left", fun=move_backward)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="c", fun=clear)



screen.exitonclick()