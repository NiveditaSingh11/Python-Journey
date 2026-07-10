# Single Inheritance

class Animal:
    def speak(self):
        print("Animal Speaks!!")
        
class Lion(Animal):
    def roar(self):
        print("Lion roars !!")
  
  
#l1= Lion()
#l1.speak()
#l1.roar()      

# Multiple Inheritance

class Father:
    def skills(self):
        print("Leadership!!")
        
class Mother:
    def hobbies(self):
        print("Gardening , Poetry  !!")
        

class Child(Father,Mother):
    def play(self):
        print("playing football !!")
        
#c = Child()
#c.play()
#c.hobbies()
#c.skills()


# Multilevel inheritance

class Grandfather:
    def house(self):
        print("Grandparents' house")
        
class Father(Grandfather):
    def car(self):
        print("parents' car")
        
class Child(Father):
    def bike(self):
        print("child's bike")
        
#c =Child()
#c.bike()
#c.car()
#c.house()


#Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("vehicle satrted.....")
        
class Car(Vehicle):
    def drive(self):
        print("Driving a car !!")
 
class Bike(Vehicle):
    def ride(self):
        print("Riding a car !!")   
    
car1 =Car()
bike1= Bike()

#car1.start()
#bike1.start()

# hybrid inheritance

class A:
    def show_A(self):
        print("Class A")
        
class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")
        

class D(B,C):
    def show_D(self):
        print("Class D")
        
d= D()
d.show_A() #inherited from A
d.show_B() #from B
d.show_C() #from C
d.show_D() #from D (own)