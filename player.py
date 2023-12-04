from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.color("black")
        self.shape("turtle")
        self.left(90)

    def moveUp(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.setposition(self.xcor(), new_y)

    def moveDown(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.setposition(self.xcor(), new_y)

    def moveLeft(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.setposition(new_x, self.ycor())

    def moveRight(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.setposition(new_x, self.ycor())

    def reset_position(self):
        self.setposition(STARTING_POSITION)
