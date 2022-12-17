from turtle import Screen, Turtle


class Snake:
    def __init__(self, starting_snake_segments):
        self.snake_segments = starting_snake_segments
        self.snake_segments_objects = []
        self.screen_object = None
        self.snake_heading = 0

    def setup_game_environment(self):
        self.screen_object = Screen()
        self.screen_object.setup(width=600, height=600)
        self.screen_object.bgcolor("#bbc701")
        self.screen_object.title("Snake by GH")
        self.screen_object.tracer(0)

    def develop_snake_body(self):
        for number in range(self.snake_segments):
            iteration = number
            number = Turtle(shape="square")
            number.penup()
            number.color("#6f6100")
            number.forward(20 * iteration)
            self.snake_segments_objects.append(number)

    def up_keyboard_input(self):
        if self.snake_heading != 270:
            self.snake_heading = 90

    def down_keyboard_input(self):
        if self.snake_heading != 90:
            self.snake_heading = 270

    def left_keyboard_input(self):
        if self.snake_heading != 0:
            self.snake_heading = 180

    def right_keyboard_input(self):
        if self.snake_heading != 180:
            self.snake_heading = 0

    def grow_one_segment(self):
        xy_cord_of_last_segment = self.snake_segments_objects[-1].position()
        self.snake_segments += 1
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("#6f6100")
        new_segment.setposition(xy_cord_of_last_segment)
        new_segment.setheading(self.snake_heading)
        new_segment.forward(20)
        self.snake_segments_objects.append(new_segment)
