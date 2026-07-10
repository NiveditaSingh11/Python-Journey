# super() and method overriding 

class Vehicle:
    def __init__(self):
        self.brand="TOYOTA"
        self.year= 2026
        
    def start_engine(self):
        return "Engine started....." 
    
    def description(self):
        return f"{self.year} : {self.brand} - vehicle"
    
class Car(Vehicle):
    def __init__(self,model,doors):
        super().__init__() # call parent constructor !
        self.model=model 
        self.doors=doors
        print(f"Instance of Car class created with brand :{self.brand} and year as :{self.year} !!")
        
    def description(self):
        parent_desc= super().description()
        return f"Parent Description: {parent_desc} | Model: {self.model} | Doors : {self.doors}"
    
    def start_engine(self):
        return "Car engine started with push button !! "

print("----------Parent object-----------\n")
v1 =Vehicle()
print(v1.description())
print(v1.start_engine())
print("----------Child object-----------\n")
c1 =Car("Defender" ,4)
print(c1.description())
print(c1.start_engine())
