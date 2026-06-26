#arguements(Args) & keyword Arguements(kwargs)
def my_addition(*num):
    return sum(num)

print(my_addition(5, 8, 3, 7, 8))

def info(**val):
    for k, v in val.items():
        print(f"{k} >> {v}")

info(name="nivedita", age=30, city="patna")


def show_info(name , *marks,age=19,**info):
    print(f"Name :{name}")
    print(f"Marks:{marks}")
    print(f"age :{age}")
    print("extra info:")
    for k,v in info.items():
        print(f"{k}>>{v}")
        
show_info("nivedita",93,92,97,96, age = 20,city ="patna", course="python")
    

