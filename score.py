from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        # self.highScore = 0
        with open("highScore.txt") as file:
            self.highScore = int(file.read())
        self.write(f"Score = {self.score}, High Score: {self.highScore}", True, align="center", font=('Arial', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.goto(0, 250)
        self.write(f"Score = {self.score}, High Score: {self.highScore}", True, align="center", font=('Arial', 20, 'normal'))

    def restart(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScore.txt", mode="w") as file:
                file.write(str(self.highScore))
        self.score = 0
        self.clear()
        self.goto(0, 250)
        self.write(f"Score = {self.score}, High Score: {self.highScore}", True, align="center", font=('Arial', 20, 'normal'))
