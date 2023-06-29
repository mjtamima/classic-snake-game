from turtle import Turtle
import random

x = 280
x_ = -280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(random.randint(x_, x), random.randint(x_, x))

    def regenerate(self):
        self.goto(random.randint(x_, x), random.randint(x_, x))
