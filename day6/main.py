
with open('./data.txt', 'r') as f:
    data = f.read().split('\n\n')

list_data = []

def get_yesses(data=data):
    for d in data:
        d = d.replace("\n", "")
        list_data.append(len(set(d)))

get_yesses()
print(sum(list_data))

matches = []

def get_matches(group):
    l = len(group)
    for i in range(0, len(group)):
        for char in group[i]:
            if (char in group[i]):
                if(i != 0):
                    matches.append(char)
            else:
                matches.remove(char)
    # return matches


# split_data = []

def get_all_yesses(data=data):
    for d in data:
        s = d.split("\n")
        get_matches(s)
        # return len(v)

        # print(s)
        # split_data.append(s)

get_all_yesses()
print(len(matches))

# print(split_data)unique_1 = [w for w in set(word_1) if w in word_2]