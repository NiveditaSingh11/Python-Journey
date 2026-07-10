class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance  #encapsulation !!
        
    def deposit(self,amount):
        if amount >0:
            self.__balance =+ amount
            print(f"Deposited Rs.{amount}") 
        
        else:
            print("deposit must be a positive value.")
    
    def withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance -= amount
            print(f"withdrawn Rs. {amount}")
        else:
            print("insufficient balance.")
            
            
    
    def __str__(self):
        return f"Account owner :{self.owner},Balance : Rs. {self.__balance}"
    
    def get_balance(self):
        return self.__balance
    

acc1= BankAccount("nivedita", 20000)
print(acc1)
acc1.deposit(50000)
acc1.withdraw(7000)
print(acc1)
print(f"{acc1.owner} has Rs. {acc1.get_balance()}/- in the bank account.")
acc1.__balance=0  #->this can cause change 
acc1._BankAccount__balance=0 #extremely bad practice !!
print(f"{acc1.owner} has Rs. {acc1.get_balance()}/- in the bank account.")
print(f"{acc1.__balance}")
print(f"ye hai class ke andar ka real protected data -> {acc1._BankAccount__balance}")
