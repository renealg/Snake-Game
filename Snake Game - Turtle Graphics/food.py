import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.location = (random.randint(-250, 250), random.randint(-250, 250))
        self.create()

    def create(self):
        #cir = Turtle("circle")
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(self.location)

    def change(self):
        self.location = (random.randint(-250, 250), random.randint(-250, 250))
        self.goto(self.location)

