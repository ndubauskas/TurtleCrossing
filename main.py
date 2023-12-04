import random
import time
from turtle import *
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(tim.moveUp, "w")
screen.onkey(tim.moveDown, "s")
screen.onkey(tim.moveLeft, "a")
screen.onkey(tim.moveRight, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.moveCar()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False

    if tim.ycor() >= 280:
        tim.reset_position()
        scoreboard.addPoint()
        scoreboard.updateScore()

scoreboard.gameOver()


screen.exitonclick()