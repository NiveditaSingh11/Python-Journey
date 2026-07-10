class Money:
    def __init__(self,amount):
        self.amount=amount
    
    def __add__(self,other):
        return Money(self.amount+other.amount)
    
    def __str__(self):
        return f"$ {self.amount}"
    
wallet1=Money(40000)
wallet2=Money(50000)

total =wallet1+wallet2
print(type(total))
print(total)

