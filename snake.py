from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
#STARTING_POS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create()
        self.head = self.squares[0]

    def create(self):
        for pos in STARTING_POS:
            sq = Turtle("square")
            sq.color("white")
            sq.penup()
            sq.goto(pos)
            self.squares.append(sq)

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            newX = self.squares[i - 1].xcor()
            newY = self.squares[i - 1].ycor()
            self.squares[i].goto(newX, newY)
        self.head.forward(MOVEMENT)

    def restart(self):
        for sq in self.squares:
            sq.goto(1000, 1000)
        self.squares.clear()
        self.create()
        self.head = self.squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        #self.squares[0].left(90.0)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        #self.squares[0].right(90.0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        #self.squares[0].left(180.0)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        #self.squares[0].right(0)

    def tail(self):
        if self.head.heading() == UP:
            pos = (self.squares[-1].xcor(), self.squares[-1].ycor() - 20)
        elif self.head.heading() == DOWN:
            pos = (self.squares[-1].xcor(), self.squares[-1].ycor() + 20)
        elif self.head.heading() == LEFT:
            pos = (self.squares[-1].xcor() + 20, self.squares[-1].ycor())
        else:
            pos = (self.squares[-1].xcor() - 20, self.squares[-1].ycor())

        sq = Turtle("square")
        sq.color("white")
        sq.penup()
        sq.goto(pos)
        self.squares.append(sq)
