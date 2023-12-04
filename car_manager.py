from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def create_cars(self):

        random_chance = random.randint(1, 6)
        if random_chance <= 4:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setposition(300, random.randrange(-250, 250))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def moveCar(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increaseCarSpeed(self):
        pass
