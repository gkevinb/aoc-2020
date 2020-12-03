with open('input.txt') as f:
    terrain = [line.rstrip() for line in f]

# print(terrain)

def slope_run(terrain, right, down):
    tree_count = 0
    y_coordinate = 0

    for i in range(down, len(terrain), down):
        y_coordinate += right
        spot = terrain[i][y_coordinate % 31]
        print(terrain[i])
        print(y_coordinate % 31)
        print(spot)
        if spot == "#":
            tree_count += 1
    return tree_count


first = slope_run(terrain, 1, 1)
second = slope_run(terrain, 3, 1) # first part, 187 that's correct
third = slope_run(terrain, 5, 1)
fourth = slope_run(terrain, 7, 1)
fifth = slope_run(terrain, 1, 2)

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(first * second * third * fourth * fifth)