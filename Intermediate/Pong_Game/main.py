from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


score = Scoreboard()



right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()


screen.listen()
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")
screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "s")






game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()