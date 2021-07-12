# Importing The Libraries :
from turtle import Turtle, Screen
import random

color = ["red", "yellow", "green", "orange", "blue", "purple"]  # Defining Colors
screen = Screen()
screen.setup(width=500, height=400) # setting The screen Size to be aware of  co ordinate of turtle race
all_turtle = []
print("Choose A bet among : RED, YELLOW, GREEN, BLUE, PURPLE.\nWho do you think will win?")
user_ip = screen.textinput(title="Bet", prompt="On Which Turtle you'll bet ? ").lower()  # asking for bet

for i in range(0, len(color)):
    t = Turtle(shape="turtle")
    t.penup()                      # coz we don't want to print The lines
    t.goto(x=-230, y=180 - 69 * i)
    t.color(color[i])              # acquiring color from color list
    all_turtle.append(t)           # appending the turtles in a list

if user_ip:
    is_race_on = True             # Checking is user put a bet or not

screen.title("Turtle Race")
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230: # checking if the winning turtle reached the finish line or not
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_ip:
                print(f"{winning_color} turtle won the Race .")
                break
            else:
                print(f"You've lost. \nYour {user_ip} turtle was too slow to win the race ;) \n{winning_color} turtle "
                      f"won the race")
        rand_dist = random.randint(0, 10) # generating random forward for each steps for each turtles. So that no
        # turtles moves with same speed during the whole race.
        turtle.forward(rand_dist)
screen.exitonclick()
