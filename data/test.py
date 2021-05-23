import json

with open("train.json") as f1:
    train = json.load(f1)

prev = train['images'][0]['id'] - 1
for e in train['images']:
    if e['id'] != prev + 1:
        print('images error ' + str(e['id']))
    prev = e['id']

prev2 = train['annotations'][0]['id'] - 1
for e in train['annotations']:
    if e['id'] != prev2 + 1:
        print('annotations error ' + str(e['id']))
    prev2 = e['id']
    
