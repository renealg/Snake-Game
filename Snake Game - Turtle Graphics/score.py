from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.write(f"Score = {self.score}", True, align="center", font=('Arial', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.goto(0, 250)
        self.write(f"Score = {self.score}", True, align="center", font=('Arial', 20, 'normal'))
