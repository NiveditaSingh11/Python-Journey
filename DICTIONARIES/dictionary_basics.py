'''
friend_group={}
print(friend_group)
print(type(friend_group))
'''
friend_group={
    "Rohit" :"Sonam",
    "Vikash" :"Neha",
    "Satyam":"Shivani"
}

print(friend_group["Rohit"])  #access

#add/modify
friend_group["Dilip"] = "Arya"
friend_group["Satyam"]="Mahi"
print(friend_group)

#print all keys
print(friend_group.keys())
print(friend_group.values())
var1=friend_group.pop("Rohit")
print(var1)
print(friend_group)

print(friend_group.get("Shivam")) #to avoid KeyError
print(friend_group.get("Shivam" ,"Not found"))

print(friend_group.items())

for k,v in friend_group.items():
    print(f"{k} >>> {v}")


print(len(friend_group))


