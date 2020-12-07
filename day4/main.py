keys = ["ecl:", "eyr:", "hcl:", "byr:", "iyr:", "hgt:", "pid:"]

correct_passwords_length = 0
with open ('./data.txt', 'r') as f:
    list_data = f.read().split("\n\n")
    for d in list_data:
        matches = [key for key in keys if key in d]
        if(len(matches) == 7):
            correct_passwords_length += 1
    # for d in list_data:
    #     cleaned = d.replace(" ", ", ").replace("\n", ", ")
    #     data.append(cleaned)
    
print(correct_passwords_length)
