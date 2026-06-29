fruits= ["apple","mango","kiwi","orange","guava","grapes"]

position =1
for i in fruits:
    print(f"{position} --> {i}")
    position +=1 
    
    
print("\n\n")

for idx ,val in enumerate(fruits,start =1):
    #if len(val) >5:
        print(f"{idx} -> {val}")
        
print("\n\n")
nums = [48,68,34,79,89,54,65]

for idx, val in enumerate(nums ,start=1):
    if val%2 ==0:
        print(f"{idx} -> {val}")