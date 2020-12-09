import copy

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

original_operations = []

for line in lines:
    operation, number = line.split(" ")
    dictionary = {
        "code": operation,
        "number": int(number),
        "times": 0
    }
    original_operations.append(dictionary)

# Part 1
operations = copy.deepcopy(original_operations)
index = 0
operation = operations[index]
accumulator = 0

while(operation["times"] < 1):
    operation["times"] += 1
    if operation["code"] == "nop":
        index += 1
    if operation["code"] == "acc":
        accumulator += operation["number"]
        index += 1
    if operation["code"] == "jmp":
        index += operation["number"]
    try:
        operation = operations[index]
    except:
        print("out of range")
        break

print(accumulator)

print("============")

# Part two
def loop(operations):
    index = 0
    operation = operations[index]
    accumulator = 0

    while(operation["times"] < 1):
        operation["times"] += 1
        if operation["code"] == "nop":
            index += 1
        if operation["code"] == "acc":
            accumulator += operation["number"]
            index += 1
        if operation["code"] == "jmp":
            index += operation["number"]
        try:
            operation = operations[index]
        except:
            return accumulator
    return 0


for i, operation in enumerate(original_operations):
    operations = copy.deepcopy(original_operations)
    if operation["code"] == "nop":
        operations[i]["code"] = "jmp"
    elif operation["code"] == "jmp":
        operations[i]["code"] = "nop"
    acc = loop(operations)
    if acc > 0:
        print(acc)
        break
