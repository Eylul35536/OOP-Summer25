class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car1 = Car("blue", "sedan")

print("My", car1.model, "car is", car1.color)
