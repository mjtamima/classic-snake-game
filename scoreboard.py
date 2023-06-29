from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(0,270)
        self.score = 0
        self.color("white")
        self.write(f"Score:{self.score}",align="center",font=('Courier',20,'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=('Courier',20,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over.",align="center",font=('Courier',20,'normal'))
