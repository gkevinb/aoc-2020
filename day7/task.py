import re

sentence = "1 bright white bag, 2 muted yellow bags."

pattern = r",?\s?\d\s(.*?)\sbags?"

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

bags_dictionary = {}

for line in lines:
    outer_bag, sentence = line.split(" bags contain ")
    inner_bags = re.findall(pattern, sentence)
    print(outer_bag)
    print(inner_bags)
    bags_dictionary[outer_bag] = inner_bags

print(bags_dictionary)


# Part 1
def recursion(this_bag):
    if "shiny gold" == this_bag:
        return 1
    else:
        for bag in bags_dictionary[this_bag]:
            if 1 == recursion(bag):
                return 1
        return 0

x = 0
for bag in bags_dictionary:
    x += recursion(bag)

print(x-1) # -1 because shiny gold bag can't be the outer bag

print("======================================")

pattern = r",?\s?(\d)\s(.*?)\sbags?"

bags_dictionary2 = {}

for line in lines:
    outer_bag, sentence = line.split(" bags contain ")
    inner_bags = re.findall(pattern, sentence)
    bags_dictionary2[outer_bag] = { i[1]: i[0] for i in inner_bags }
    print(outer_bag + " - " + str(bags_dictionary2[outer_bag]))

# print(bags_dictionary2)

print("------")
# Part 2

print(bags_dictionary2["shiny gold"])
# print(bags_dictionary2["dark olive"])
# print(bags_dictionary2["vibrant plum"])
print("------")

def recursion_num(this_bag, number):
    # if bags_dictionary2[this_bag] == {}:
    #     return 0
    count = 0
    for bag, num in bags_dictionary2[this_bag].items():
        count += recursion_num(bag, num) * int(num) + int(num)
    return count

    # if bags_dictionary2[this_bag] == {}:
    #     return 1
    # else:
    #     count = 0
    #     print(this_bag+" bruh")
    #     for bag, num in bags_dictionary2[this_bag].items():
    #         print(bag)
    #         print(num)
    #         print(count)
    #         count += int(num) * recursion_num(bag, num)

    #     return count * int(number) + int(number)

c = 0
print(recursion_num("shiny gold", 1))

# for b, n in bags_dictionary2["shiny gold"].items():
#     print(f"bag: {b}")
#     print(f"num: {n}")
#     c += recursion_num(b, n) * int(n)
# print(c)