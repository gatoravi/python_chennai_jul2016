class Car:
    #Constructor
    def __init__(self, model1 = "NA", speed1 = "NA"):
        self.model = model1
        self.speed = speed1
        self.cost = 150000
    def accelerate(self):
        "Accelerates the car"
        self.speed += 100


def main():
    paul_car = Car("Toyota", 100) #instantiating an object of class Car
    print(paul_car.model)
    print("initial speed is ", paul_car.speed)
    paul_car.accelerate()
    print("later speed is ", paul_car.speed)
    yuva_car = Car("Maruti", 20)
    print("initial yuva speed is ", yuva_car.speed)
    yuva_car.accelerate()


main()
