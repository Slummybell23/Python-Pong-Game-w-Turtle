from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("normal")
        self.x_move = 10
        self.y_move = 10

    # FUNCTION TO BE USED BEFORE BEFORE BEFORE THE MOVE FUNCTION TO CALCULATE PREVIOUS LOCATION
    # def pre_value(self):
    #     self.preX = self.xcor()
    #     self.preY = self.ycor()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.x_bounce()
        self.speed("fast")
