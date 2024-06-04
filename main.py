import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

TIME_GAP = 0.1

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


def snake_game():
    global TIME_GAP

    game_is_on = True

    snake.reset()
    scoreboard.reset()
    food.new_location()

    while game_is_on:
        screen.update()
        time.sleep(TIME_GAP)

        snake.move()

        if snake.head.distance(food) < 15:
            food.new_location()
            snake.extend()
            scoreboard.score += 1
            scoreboard.score_card()
            if scoreboard.score % 10 == 0:
                TIME_GAP /= 1.25
            else:
                TIME_GAP /= 1.05

        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
            TIME_GAP = 0.1
            scoreboard.game_over()
            game_is_on = False

        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                TIME_GAP = 0.1
                scoreboard.game_over()
                game_is_on = False


screen.onkey(key="r", fun=snake_game)

snake_game()

screen.exitonclick()
