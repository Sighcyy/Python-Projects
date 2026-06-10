import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



player = Player()
screen.onkeypress(player.move, "space")

score = Scoreboard()

car_manager = CarManager()
car_manager.hideturtle()



speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        score.next_level()
        speed *= 0.90
    for car in car_manager.all_cars:
         if car.distance(player) < 20:
            game_is_on = False
            score.game_over_level()






screen.exitonclick()