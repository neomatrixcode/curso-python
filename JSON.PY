import json
 
from pprint import pprint
 
with open("C:\prueba.json") as data_file:    
    data = json.load(data_file)
 
print (data) 
pprint(data["peras"])

