with open('data.txt', 'r') as f:
    paths = f.read()
    data = paths.split('\n')

tree = "#"

def trees_encounter(left_moves, down_moves):
    trees_count, index, list_len = 0, 0, len(data)

    for i in range(0, list_len, down_moves):
        p = data[i]
        while True:
            try:
                tree_or_space = p[index]
                if(tree_or_space == tree):
                    print(tree_or_space, tree)
                    trees_count += 1
                index += left_moves
                break
            except IndexError:
                p += p
    
    return trees_count

trees = trees_encounter(3, 1)

print(trees)

print(trees_encounter(1, 1) * trees_encounter(3, 1) * trees_encounter(5, 1) * trees_encounter(7, 1) * trees_encounter(1, 2))