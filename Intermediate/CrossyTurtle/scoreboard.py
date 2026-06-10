from turtle import Turtle
import car_manager
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_score()



    def update_score(self):
        self.color("Black")
        self.goto(-220, 230)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over_level(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
        
