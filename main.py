import time
from turtle import Screen

import score
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
game_over = False

snake = Snake()
snake_food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        scoreBoard.add_score()
        snake.add_length()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_over = True

    for segment in snake.snake_segments[1::]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_over = True


screen.exitonclick()
