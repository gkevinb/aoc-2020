with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

print(lines)


# Bruteforce

first = 0
second = 0
third = 0

for i in lines:
    # print(i)
    for j in lines:
        if i + j == 2020:
            first = i
            second = j
            break
    if i + j == 2020:
        break

print(first)
print(second)
print(first + second)
print(first * second)

for i in lines:
    for j in lines:
        for k in lines:
            if i + j + k == 2020:
                first = i
                second = j
                third = k
                break
        if i + j + k == 2020:
            first = i
            second = j
            third = k
            break
    if i + j + k == 2020:
        first = i
        second = j
        third = k
        break

print(first)
print(second)
print(third)
print(first + second + third)
print(first * second * third)
