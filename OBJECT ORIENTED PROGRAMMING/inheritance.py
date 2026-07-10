class Animal:
    def __init__(self,name):
        self.name=name
        
    
    def __speak(self): #this will not get inherited !!
        print(f"{self.name} makes a sound.")
        
class Dog(Animal):
    def speak1(self):
        print(f"{self.name} barks!!")
        
class Lion(Animal):
    def speak(self):
        print(f"{self.name} roars!!")
    
    
puppy1= Dog("Simbba")
puppy1.speak1()




    

 
        
        