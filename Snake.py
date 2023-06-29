from turtle import Turtle

ps = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.tim = []
        self.create_snake()
        self.head = self.tim[0]

    def create_snake(self):
        for i in range(0, 3):
            self.tim.append(Turtle(shape="square"))
            self.tim[i].color("white")
            self.tim[i].penup()
            self.tim[i].goto(ps[i])

    def move(self):
        for i in range(len(self.tim) - 1, 0, -1):
            x = self.tim[i - 1].xcor()
            y = self.tim[i - 1].ycor()
            self.tim[i].goto(x, y)
        self.tim[0].forward(20)

    def move_up(self):
        if self.tim[0].heading() == 0:
            self.tim[0].left(90)
        elif self.tim[0].heading() == 180:
            self.tim[0].right(90)

    def move_left(self):
        if self.tim[0].heading() == 90:
            self.tim[0].left(90)
        elif self.tim[0].heading() == 270:
            self.tim[0].right(90)

    def move_down(self):
        if self.tim[0].heading() == 0:
            self.tim[0].right(90)
        elif self.tim[0].heading() == 180:
            self.tim[0].left(90)

    def move_right(self):
        if self.tim[0].heading() == 90:
            self.tim[0].right(90)
        elif self.tim[0].heading() == 270:
            self.tim[0].left(90)

    def increase_size(self):
        val = Turtle()
        val.penup()
        val.shape("square")
        val.color("white")
        val.goto(self.tim[-1].position())
        self.tim.append(val)

    def collision(self):
        flag = False
        for i in self.tim[1:]:
            if self.head.distance(i) < 10:
                flag = True
                break
        return flag

