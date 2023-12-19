from turtle import Screen
import time
from snake import Snake
import food
import scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = food.Food()
score = scoreboard.Score()
score.show()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")

game_is_on = True

while game_is_on:

    snake.move()

    if snake.segments[0].distance(food) <= 15:
        food.refresh()
        score.calculate()
        snake.snake_gross()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 \
            or snake.segments[0].ycor() < -280:
        score.reset_round()
        snake.reset_snake()

    for segment in snake.segments[3:]:
        if snake.segments[0].distance(segment) < 10:
            score.reset_round()
            snake.reset_snake()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
