import json
with open("2)Coders_Of_Delhi/data.json","r") as file:
    data=json.load(file)


for key in data['users']:
    print (key['name'])
