from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-250,250)
        self.write(self.score, align="center", font=FONT)

    def addPoint(self):
        self.score += 1

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER Score:{self.score}", align="center", font=("Courier", 35, "normal"))
