import json

data = {"name":"Joy","id":"011151242"}

data = json.dumps(data)

print(type(data))

with open('json.txt','w') as f:
    f.write(f"Hey is the data: {data}")

#serialization means converting python complex objects to json 