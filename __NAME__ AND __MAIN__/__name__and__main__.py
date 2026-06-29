fruits= ["apple","mango","kiwi"]

position =1
for i in fruits:
    print(f"{position} --> {i}")
    position +=1 
    
    
print(__name__)
print("hello from __name__and__main__.py ")
if __name__ == "__main__" :
    print("hello i am special !!")
else:
    print("no I am not special !!")