from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt", mode= "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.text = f"Score: {self.current_score}"
        self.color('white')
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.text = f"Score: {self.current_score} High Score: {self.high_score}"
        self.write(self.text, align= ALIGNMENT, font= FONT)

    def reset_scoreboard(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open(f"data.txt", mode= "w") as file:
                file.write(str(self.current_score))
        self.current_score = 0
        self.update_score()



    def increase_score(self):
        self.current_score += 1
        self.update_score()

