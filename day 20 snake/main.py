from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import random


def snake_game_launch():
    sgame1 = Snake(starting_snake_segments=3)
    score = ScoreBoard()
    sgame1.setup_game_environment()
    score.enter_message()
    food = Food()
    sgame1.develop_snake_body()
    game_speed = 0.1

    # generates a new location where food can spawn,
    # in a location where the snake isn't in already
    def locate_new_food_xy_cord():
        located_new_food_cord = False
        proposed_food_x_cord = int()
        proposed_food_y_cord = int()
        while not located_new_food_cord:
            proposed_food_x_cord = random.randrange(-260, 280, 20)
            proposed_food_y_cord = random.randrange(-260, 280, 20)
            sufficient_cord = True
            for segment_snake in sgame1.snake_segments_objects:
                if segment_snake.distance(proposed_food_x_cord, proposed_food_y_cord) < 15:
                    sufficient_cord = False
            if sufficient_cord:
                located_new_food_cord = True
        return proposed_food_x_cord, proposed_food_y_cord

    # main loop of the game
    game_is_on = True
    while game_is_on:
        time.sleep(game_speed)
        sgame1.screen_object.listen()
        sgame1.screen_object.onkey(key="Up", fun=sgame1.up_keyboard_input)
        sgame1.screen_object.onkey(key="Down", fun=sgame1.down_keyboard_input)
        sgame1.screen_object.onkey(key="Left", fun=sgame1.left_keyboard_input)
        sgame1.screen_object.onkey(key="Right", fun=sgame1.right_keyboard_input)
        last_segment = sgame1.snake_segments_objects.pop(0)
        xy_cord = sgame1.snake_segments_objects[-1].position()
        last_segment.setposition(xy_cord)
        last_segment.setheading(sgame1.snake_heading)
        last_segment.forward(20)
        sgame1.snake_segments_objects.append(last_segment)

        # checks to see if snake had ate the food
        if sgame1.snake_segments_objects[-1].distance(food) < 15:
            x_cord, y_cord = locate_new_food_xy_cord()
            food.refresh_with_position(x_cord, y_cord)
            score.add_one_point()
            sgame1.grow_one_segment()

        # detects collision with wall
        if sgame1.snake_segments_objects[-1].xcor() > 280 or sgame1.snake_segments_objects[-1].xcor() < -280:
            score.trigger_game_over()
            game_is_on = False
        elif sgame1.snake_segments_objects[-1].ycor() > 280 or sgame1.snake_segments_objects[-1].ycor() < -280:
            score.trigger_game_over()
            game_is_on = False

        # detects collision with tail using slicing with the snake body list
        for segment in sgame1.snake_segments_objects[:-2]:
            if sgame1.snake_segments_objects[-1].distance(segment) < 10:
                score.trigger_game_over()
                game_is_on = False

        # detects if your snake has grown to 50 or over,
        # declares that you have won and ends the game
        sgame1.screen_object.update()
        if score.score_count >= 50:
            score.trigger_game_won()
            game_is_on = False

    # closes the window when the user clicks on it
    sgame1.screen_object.exitonclick()


snake_game_launch()
