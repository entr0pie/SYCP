import pickle

class Car:
    def __init__(self, color, ano) -> None:
        self.color = color
        self.ano = ano

    def description(self) -> str:
        return f"COLOR: {self.color} | YEAR: {self.ano}"


my_car = Car("RED", "1999")
serialized = pickle.dumps(my_car)

robbed_car = pickle.loads(serialized)
print(robbed_car.description())