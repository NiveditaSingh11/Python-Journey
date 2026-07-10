# method overloading

class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
    
calc= Calculator()
result =calc.add(6,5)
print(result)