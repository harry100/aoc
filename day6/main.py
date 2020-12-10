
with open('./data.txt', 'r') as f:
    data = f.read().split('\n\n')

list_data = []

def get_yesses(data=data):
    for d in data:
        d = d.replace("\n", "")
        list_data.append(len(set(d)))

get_yesses()
print(sum(list_data))