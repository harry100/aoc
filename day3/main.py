with open('data.txt', 'r') as f:
    paths = f.read()
    data = paths.split('\n')

tree = "#"
trees_count, index = 0, 0

for p in data:
    str(p)
    while True:
        try:
            tree_or_space = p[index]
            if(tree_or_space == tree):
                print(tree_or_space, tree)
                trees_count += 1
            index += 3
            break
        except IndexError:
            p = p + p

print(trees_count)