import json

obj={
    "name":"pd",
    "roll":"08"
}

a=json.dumps(obj) #convert obj to string
print(type(a)) #str

a=json.loads(a)  #convert string to dict
print(type(a))

#file 
file=open("b.json","w")

json.dump(obj,file) #add obj into b.json