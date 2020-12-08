with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

operations = []

for line in lines:
    operation, number = line.split(" ")
    dictionary = {
        "code": operation,
        "number": int(number),
        "times": 0
    }
    operations.append(dictionary)


index = 0
operation = operations[index]
accumulator = 0

# Part 1
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


def loop():
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
            return accumulator
    return 0

# for i in operations:
#     if i["code"] == "nop":
#         i["code"] = "jmp"
#     elif i["code"] == "jmp":
#         i["code"] = "nop"
#     print(operations)

    