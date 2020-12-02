import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

pattern = r'(\d+)-(\d+)\s(\S):\s(.+)'
valid_passwords_part_1 = 0
valid_passwords_part_2 = 0

for string in lines:
    result = re.match(pattern, string)
    least = int(result.group(1))
    most = int(result.group(2))
    character = result.group(3)
    password = result.group(4)

    count = password.count(character)
    if least <= count and count <= most:
        valid_passwords_part_1 += 1

    # -1 because index starts from 1, not 0
    if [password[least - 1], password[most - 1]].count(character) == 1:
        valid_passwords_part_2 += 1

print(valid_passwords_part_1)
    
print(valid_passwords_part_2)
