def fruit_list():
    print("mango,apple,kiwi")

    
def my_addition (a=9,b=7):
    if type(a)== int and type(b)==int:
         print(a+b)
         return (a+b)
     
    else:
        print("invalid input,enter valid numbers !!")

   

fruit_list()
fruit_list()


c= my_addition(6,7)
print(c)

print(my_addition(5,4))

print(my_addition())
print(my_addition(7,0))
