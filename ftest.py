import requests

dburl="https://fship-app-default-rtdb.firebaseio.com/Users/.json"
qryurl='https://fship-app-default-rtdb.firebaseio.com/Users/.json?orderBy="name'
key_url="https://fship-app-default-rtdb.firebaseio.com/Users/%s.json"

kv = 123456

print (key_url % (kv))

sdata = '{"name": "Ayla Cat... Gordon", "phone": "402-914-0334", "email": "kellie.gordon33@gmail.com"}'

# print(requests.post(dburl,data=sdata))

# print(requests.get(dburl))

response = requests.get(dburl).json()

for rec in response:
    row = response[rec]
    print(rec,row['name'])
