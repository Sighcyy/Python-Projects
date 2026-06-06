from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Who will make it to the finish line first?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []




for turtle_index in range(0,6):
    all_turtles.append(Turtle())
    all_turtles[turtle_index].shape("turtle")
    all_turtles[turtle_index].color(colors[turtle_index])
    all_turtles[turtle_index].penup()
    all_turtles[turtle_index].goto(x= -230,y= y_positions[turtle_index])



if user_bet:
    is_race_on = True

random_amount = random.randint(0,10)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win!")
            else:
                print(f"You lose! {winning_color} won")
        random_amount = random.randint(0,10)
        turtle.forward(random_amount)


screen.exitonclick()
