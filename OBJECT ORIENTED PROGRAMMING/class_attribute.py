class Car:
    #class attribute
    wheels =4
    
    #instance attribute
    
    def __init__(self,brand):
        self.brand=brand
    
car1 = Car("bmw")
car2 = Car("toyota")

print(f"{car1.brand} --> {car1.wheels}")
print(f"{car2.brand} --> {car2.wheels}")
print(Car.wheels)

# not recommended
Car.wheels=7
print(f"{car1.brand} --> {car1.wheels}")
print(Car.wheels)
# not recommended    
