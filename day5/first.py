input = "FFFBBBFRRR"

def binary_to_decimal(binary):
    decimal = 0
    order = 1
    for b in binary[::-1]:
        decimal += order * int(b)
        order *= 2
    return decimal


def find_seat_id(boarding_pass):
    row_binary = boarding_pass[:7].replace("B", "1").replace("F", "0")
    column_binary = boarding_pass[7:].replace("R", "1").replace("L", "0")

    row = binary_to_decimal(row_binary)
    column = binary_to_decimal(column_binary)

    seat_id = row * 8 + column
    return seat_id


with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


# Part 1
print(max([find_seat_id(line) for line in lines]))


# Part 2
taken_seats = [find_seat_id(line) for line in lines]
taken_seats.sort()
taken_seats = set(taken_seats)

all_seats = set([i for i in range(min(taken_seats), max(taken_seats))])

print(all_seats - taken_seats)