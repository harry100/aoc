from data import data

def get_values(l):
    case = {}
    case['matchVal'] = l[0].split(" ")[1]
    case['password'] = l[1]
    case['minOccurence'] = int(l[0].split(" ")[0].split("-")[0])
    case['maxOccurence'] = int(l[0].split(" ")[0].split("-")[1])
    return case

#Sol 1
validPasswords = 0
for d in data:
    c = get_values(d.split(":"))
    count = c['password'].count(c['matchVal'])
    min = c['minOccurence']
    max = c['maxOccurence']
    if(count >= min):
        if(count <= max):
            validPasswords += 1

print(validPasswords)


# Sol 2
validPasswordLength = 0
for d in data:
    c = get_values(d.split(":"))
    min = c['minOccurence']
    max = c['maxOccurence']
    matchChar = c['matchVal']
    if ((c['password'][min] == matchChar) != (c['password'][max] == matchChar)):
        validPasswordLength += 1

print(validPasswordLength)