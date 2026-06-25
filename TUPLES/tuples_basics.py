#my_tuple = tuple()
my_tuple =("blue","green" ,"red","yellow","blue","blue","blue")
my_tuple2=("teal","orange","blue","green")
print(my_tuple)
print(my_tuple[0],my_tuple[1])
print(my_tuple[-1],my_tuple[-2])
print(type(my_tuple))
print(my_tuple[0:4:2])
print(my_tuple.count("blue"))
print(my_tuple.index("blue"))
print(my_tuple+my_tuple2)  #concatenation

print(my_tuple2*2)


info= ("Nivedita Singh","19 yrs","Patna")
#unpacking a tuple

name,age,city= info
print(f"Hello {name}, nice to know that you're from {city} and you are {age} years old.")




