import json
info = {
    'name': 'boyang',
    'age': 22
}

f = open("test.txt",'r')
# f.write(str(info))
print(json.dumps(info))
# f.write(json.dumps(info))
data = json.loads(f.read())
print(data)
f.close()
