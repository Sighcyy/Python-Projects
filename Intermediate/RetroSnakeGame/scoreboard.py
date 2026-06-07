from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.text = f"Score: {self.score}"
        self.color('white')
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.text = f"Score: {self.score}"
        self.write(self.text, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

