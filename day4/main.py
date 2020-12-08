keys = ["ecl", "eyr", "hcl", "byr", "iyr", "hgt", "pid"]

correct_passwords_length = 0
with open ('./data.txt', 'r') as f:
    data = f.read().split("\n\n")

list_data = []

for d in data:
    cleaned = d.replace("\n", " ")
    cleaned = cleaned.split(" ")
    if(len(cleaned) > 6):
        list_data.append(cleaned)

passes = []
correct = 0

for data in list_data:
    obj = {}
    for d in data:
        key, value = d.split(":")
        obj[key] = value
    passes.append(obj)

for p in passes:
    if all(key in p for key in keys):
        correct += 1
print(correct)