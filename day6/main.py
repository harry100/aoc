
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
set_list, c = [], 0

def get_matches(group):
    set_group = []
    for g in group:
        set_group.append(set(g))
    set_list.append(set_group)

# split_data = []

def get_all_yesses(data=data):
    for d in data:
        s = d.split("\n",)
        get_matches(s)

get_all_yesses()

for s in set_list:
    ic = set.intersection(*s)
    print(ic)
    c = c + len(ic)
print(c)

# print(split_data)unique_1 = [w for w in set(word_1) if w in word_2]1