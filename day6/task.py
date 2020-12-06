with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

groups = []
group = set()
count = 0

characters = "abcdefghijklmnopqrstuvwxyz"


# Part one
for string in lines:
    if string != "":
        group |= set(string)

    else:
        count += len(group)
        groups.append(group)
        group.clear()

count += len(group)
groups.append(group)
group.clear()

print(count)

group = []
count = 0

# Part two
for string in lines:
    if string != "":
        group.append(string)

    else:
        for character in characters:
            count += int(all(character in i for i in group))
        group = []

for character in characters:
    count += int(all(character in i for i in group))


print(count)