#The __str__ method
class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f'A {self.color} car with mileage {self.mileage}'
car=Car('RED',20)
print(car)
