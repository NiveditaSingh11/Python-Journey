my_list=[1,1,2,5,7,8,4,9,3]
my_set= set(my_list)


my_set.add(4000)
print(my_set)
my_set.remove(5)
print(my_set)
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)

my_set.clear()
print(my_set)


a={6,4,0,3}
b={2,0,3,1,8}
#common set operations

print( a | b) #union
print(a & b) #intersection
print(a-b) #difference
print(b-a) 

print(a ^ b) # symmetric difference

print(b^a)
