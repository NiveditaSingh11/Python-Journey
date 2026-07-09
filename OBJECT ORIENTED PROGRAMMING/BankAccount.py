class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
        
    def deposit(self,amount):
         self.balance += amount
         print(f"{amount} deposited. new balance :{self.balance}\n")
         
         
    def withdraw (self, amount):
        if amount> self.balance:
            print("you don't have sufficient balance.\n")
            
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. new balance :{self.balance}\n")

            
account1 = BankAccount("nivedita",4000000)
account1.deposit(700000)
account1.withdraw(40000)