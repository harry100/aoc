from data import data

def get_values(l):
    formula_val, value = l.split(":")
    recipe, match_value = formula_val.split(" ")
    min_occurence, max_occurence = recipe.split("-")
    return [ value, match_value, int(min_occurence), int(max_occurence) ]


#Sol 1
valid_password_count = 0

for d in data:
    value, match_value, min_occurence, max_occurence = get_values(d)
    count = value.count(match_value)
    if(count >= min_occurence):
        if(count <= max_occurence):
            valid_password_count += 1

print(valid_password_count)


# Sol 2
valid_password_count1 = 0

for d in data:
    value, match_value, min_occurence, max_occurence = get_values(d)
    if ((value[min_occurence] == match_value) != (value[max_occurence] == match_value)):
        valid_password_count1 += 1

print(valid_password_count1)