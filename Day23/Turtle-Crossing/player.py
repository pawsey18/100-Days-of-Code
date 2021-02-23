from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POS)