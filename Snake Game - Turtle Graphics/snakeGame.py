import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snakey = Snake()
foody = Food()
scorey = Score()

screen.listen()

screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")

screen.update()
playing = True

while playing:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    # checks if the snake eat food
    if snakey.head.distance(foody) < 15:
        foody.change()
        scorey.increase()
        snakey.tail()

    # checks if the snake touched itself
    touch = False
    for i in range(1, len(snakey.squares)):
        if snakey.head.distance(snakey.squares[i]) < 5:
            touch = True

    # game over - checks if the snake touched the screen borders or itself
    if (snakey.head.ycor() < -280 or snakey.head.ycor() > 280 or snakey.head.xcor() < -280
            or snakey.head.xcor() > 280 or touch):
        playing = False
        choise = screen.textinput("", "you lost... \ndo you want to play again? ")
        if choise == "yes":
            screen.resetscreen()
            snakey = Snake()
            foody = Food()
            scorey = Score()

            screen.listen()
            screen.onkey(snakey.up, "Up")
            screen.onkey(snakey.down, "Down")
            screen.onkey(snakey.left, "Left")
            screen.onkey(snakey.right, "Right")

            screen.update()
            playing = True

screen.exitonclick()
