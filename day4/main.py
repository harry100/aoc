import re

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

def check_byr(year):
    return 1920 <= int(year) <= 2002

def check_iyr(year):
    return  2010 <= int(year) <= 2021

def check_eyr(year):
    return 2020 <= int(year) <= 2030

def check_hgt(height) :
    m = re.search("^[0-9]{3}cm$|^[0-9]{2}in$", height)
    if(m):
        return True
    else:
        return False

def check_ecl(color):
    m = re.search("^amb|blu|gry|brn|grn|hzl|oth$", color)
    if(m):
        return True
    else:
        return False

def check_pid(id):
    m = re.search("^[0-9]{9}$", id)
    if(m):
        return True
    else:
        return False

def check_hcl(color):
    m = re.search("^#[0-9, a-f]{6}$", color)
    if(m):
        return True
    else:
        return False

def check_cid(id):
    return True

validators = {
    'byr': check_byr,
    'iyr': check_iyr,
    'eyr': check_eyr,
    'hgt': check_hgt,
    'hcl': check_hcl,
    'ecl': check_ecl,
    'pid': check_pid,
    'cid': check_cid
}

valid = 0

def validate(p):
    for field, func in validators.items():
        if field not in p.keys() and field != 'cid':
            return 0
        if field != 'cid':
            if not func(p[field]):
                return 0
    print(p[field], func(p[field]), field)
    return 1

print('sum', sum(validate(p) for p in passes))
