#Dictionory
dic={
    "name":"prasad",
    "Age":"20",
    "Roll":"50"
}

print(dic["Age"])
#print(dic["class"]) #error bcz key not found
print(dic.get("class")) #give NONE not error

print(dic.keys())
print(dic.values())

dic.update({"name":"sneha","gender":"female"}) #update name and add new pair
dic.pop("name")
print(dic.items())
dic.clear()
print(dic)