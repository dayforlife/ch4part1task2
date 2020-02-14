class Airplane():
    def __init__(self,mark, model, year, max_speed):
        self.mark = mark
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
    
    def take_off(self):
        self.is_flying = True
        return f"{self.mark}{self.model} was take off"

    def land(self):
        self.is_flying = False
        return f"{self.mark}{self.model} landed, the odometr = {self.odometer}km"

    def fly(self):
        self.odometr += 100
        return f"{self.mark}{self.model} is flying now {self.odometer}km during the flying {self.max_speed}km/h"
plane1 = Airplane(
    "Boeng", "580", "2020", 2000
)

print(plane1.take_off())
print(plane1.fly())
print(plane1.fly())
print(plane1.land())