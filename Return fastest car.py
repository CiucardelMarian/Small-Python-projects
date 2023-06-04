class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


# WRITE YOUR SOLUTION HERE:

def fastest_car(cars: list):
    fastest = cars[1]
    for item in cars:
        if item.top_speed > fastest.top_speed:
            fastest = item
    return fastest.make


car1 = Car("Saab", 195)
car2 = Car("Lada", 110)
car3 = Car("Ferrari", 280)
car4 = Car("Trabant", 85)
carlist = [car1, car2, car3, car4]
print(fastest_car(carlist))
