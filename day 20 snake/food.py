from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.shape("square")
        self.random_colors = ["white", "red", "blue", "green"]
        self.color(random.choice(self.random_colors))
        self.speed("fastest")
        self.goto(random.randrange(-260, 260, 20), random.randrange(-260, 260, 20))

    def set_random_color(self):
        self.color(random.choice(self.random_colors))

    def refresh_random(self):
        self.set_random_color()
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

    def refresh_with_position(self, x_cord=int(), y_cord=int()):
        self.set_random_color()
        self.goto(x_cord, y_cord)
