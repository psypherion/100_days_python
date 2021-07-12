from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(6)
def move_back():
    tim.backward(6)
def counter_clock():
    tim.left(6)
def clock_wise():
    tim.right(6)
def cls():
    tim.reset()
screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_back)
screen.onkeypress(key="a",fun=counter_clock)
screen.onkeypress(key="d",fun=clock_wise)
screen.onkey(key="c",fun=cls)

screen.exitonclick()




