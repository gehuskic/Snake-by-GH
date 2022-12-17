from turtle import Turtle
import time


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#6f6100")
        self.pencolor("#6f6100")
        self.goto(0, 280)
        self.score_count = int()
        self.type_face = "Arial"
        self.font_size = 12
        self.font_type = "normal"
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))

    def add_one_point(self):
        self.clear()
        self.score_count += 1
        self.pencolor("#6f6100")
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))

    def set_score_amount(self, new_score):
        self.clear()
        self.score_count = new_score
        self.pencolor("#6f6100")
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))

    def enter_message(self):
        self.clear()
        self.goto(0, 150)
        self.write(f"Snake by GH", move=False, align="center",
                   font=(self.type_face, 30, "bold"))
        self.goto(0, 0)
        self.write(f"Can you make it to 50?", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))
        time.sleep(3)
        self.pencolor("#6f6100")
        self.goto(0, 280)
        self.clear()
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))

    def trigger_game_over(self):
        self.clear()
        self.pencolor("#6f6100")
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))
        self.penup()
        self.goto(0, 0)
        self.pencolor("white")
        self.write(f"GAME OVER", move=False, align="center",
                   font=(self.type_face, 30, "bold"))
        self.goto(0, -100)
        self.write(f"Click anywhere to exit", move=False, align="center",
                   font=(self.type_face, 12, self.font_type))

    def trigger_game_won(self):
        self.clear()
        self.write(f"Score: {self.score_count}", move=False, align="center",
                   font=(self.type_face, self.font_size, self.font_type))
        self.goto(0, 0)
        self.pencolor("white")
        self.write(f"YOU'VE WON!", move=False, align="center",
                   font=(self.type_face, 30, "bold"))
        self.goto(-100, -90)
        self.pencolor("white")
        self.goto(0, -100)
        self.write(f"Click anywhere to exit", move=False, align="center",
                   font=(self.type_face, 12, self.font_type))
