import json

data={
    "Name":"Mahi",
    "Training":"Python with DS"
}

with open("c:/Python312/Data Science Class -Placement/jsonData.json","w") as f:
    json.dump(data, f, indent=2)