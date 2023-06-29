from turtle import Screen
from Snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        food.regenerate()
        score.update_score()
        snake.increase_size()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    if snake.collision():
        game_is_on = False
        score.game_over()

screen.exitonclick()
