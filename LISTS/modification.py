my_list=["Nivi" ,"Sansu","Ash","Aadi"]
Aadi_friends=["umang","manish","deepu","harshit"]
var1="Ashmit" #avoid this 
print(my_list)
print(f"initial location : {id(my_list)}")
my_list[0]="Nivedita"
print(my_list)
print(f"final location : {id(my_list)}")

my_list.append("Aakarsh")
print(my_list)
popped_member=my_list.pop()
print(popped_member)
print(my_list)
my_list.insert(0,"Ayush")
print(my_list)

copy_list=my_list.copy()#gives a shallow copy 

# if copy_list = my_list .......though it is not recommended but it creates a replica 
my_list.clear()#clears he whole list 
print(copy_list)
print(my_list)


my_list.extend(Aadi_friends)
print(my_list)
my_list.clear()

my_list.extend(var1)
print(my_list)

my_list.pop(3)
print(my_list)

my_list.remove('s')
print(my_list)