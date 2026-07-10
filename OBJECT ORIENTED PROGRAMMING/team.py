class Team:
    def __init__(self,member):
        self.member=member
    
    def __len__(self):
        return len(self.member)
    
    def __repr__(self):
        return f"Team -> {self.member}"
    
    
my_list =["nishi","sansu","laddu","misti"]
t1= Team(['nivi','sansu','aadi','ash','deepu'])

print(len(t1))
print(len(my_list))
print(t1)
print(my_list)

