my_lst =["apple","kiwi","orange","banana","jackfruit"]
my_dict ={"name":"Nivedita", "city":"Patna"}
my_set ={5,3,7,2,9,0,1}
name="Nivedita"
for i in name:
    print(i.capitalize())
    
    
for fruit in my_lst:
    if len(fruit)<= 4:
        print(f"Short item --> {fruit}")
    else:
        print(f"Long item --> {fruit}")

print(my_dict.items())
for k ,v in my_dict.items():
    print(f"{k} -> {v}")
    
for i in my_set:
    print(i)
    
    