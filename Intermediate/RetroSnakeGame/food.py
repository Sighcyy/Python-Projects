from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        #Basically when you intialize in the main file food = Food() , we are basically saying its a turtle with these
        #pre made attributes which you are setting
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")

        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)


        #All of this happens when you create a food object

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)


