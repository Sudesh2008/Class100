class Car:
    def __init__(self,model,color,company,speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def  accelerate(self):
        print("Car Accelerated")

    def changeGear(self):
        print("Gear Changed")

car1 = Car("A5","Blue", "Audi", 125)
car2 = Car("T1", "Red", "Toyota", 110)

car1.start()
car2.stop()
car1.accelerate()
car2.start()
print(car1.color)