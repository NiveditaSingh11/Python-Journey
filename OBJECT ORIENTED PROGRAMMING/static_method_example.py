class BankAccount:
    
    #class variables
    bank_name= "State Bank Of India"
    interest_rate=5.0
    
    #constructor
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    #instance method
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")
        print(f"updated balance : Rs. {self.balance}/-")
        
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-= amount
            print(f"{amount} withdrawn successfully!")
            
        else:
            print("not enough balance !")
        print(f"Current balance : Rs. {self.balance}/-")
        
        
    #class method !!
    @classmethod
    def change_interest_rate(cls,new_rate):
        cls.interest_rate=new_rate
        print(f"Interest rate updated to : {cls.interest_rate}%\n")
    
        
    #static method
    @staticmethod
    def calculate_simple_interest(principal,years,rate):
        interest= (principal*years*rate)/100
        return interest
        
acc1 =BankAccount("nivedita" ,1000000)
acc2 =BankAccount("sanskriti" ,4000000)

#instance method use 
acc1.deposit(50000)
acc2.withdraw(70000)

#class method use
BankAccount.change_interest_rate(7.5)

#static method use
interest =BankAccount.calculate_simple_interest(100000,3,6.7)
print(f"simple interest will be Rs. {interest} ")


