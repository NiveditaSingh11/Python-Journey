class student:
    #instance attributes 
    def __init__(self ,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        print("object created successfully !!")
        print(f"here is the memmory location of self : {id(self)}")
    #methods
    def introduce(self):
        print(f"hi, i am {self.name} and my cgpa is : {self.cgpa}.")
        print(f"here is the memmory location of introduce  : {id(self)}")
        
        
my_student = student("nivedita" , 9.41)
print(my_student.name)
print(my_student.cgpa)
my_student.introduce()
print(f"here is the memmory location of the object : {id(my_student)}")      