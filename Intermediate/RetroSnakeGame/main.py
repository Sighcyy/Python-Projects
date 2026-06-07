from turtle import Screen
import time

from scoreboard import Scoreboard
from food import Food
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) #Turns off auto-update
screen.listen() #opens the screen for taking in input


snake = Snake() #creates the snake for us too since we call the create_snake class from the start
food = Food() #Creates a food object, with a bunch of premade attributes from the turtle class which we defined in the food class file


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




screen.update()

score = Scoreboard()

game_on = True

while game_on:
    screen.update()
    snake.move()
    time.sleep(0.09)  # 1 second delay

    #detect food collision
    #Basically if the first segment or the head is under 15 pizxels away from our food object then we
    if snake.segments[0].distance(food) < 20:
        score.increase_score()
        food.refresh()
        snake.extend()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()

    #Detect Tail Collision
    for segment in snake.segments:
        if snake.segments[0].distance(segment) < 10 and snake.segments[0] != segment:
            game_on = False
            score.game_over()





screen.exitonclick()
