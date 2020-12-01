import itertools
import math


def get_combinations(sequence, times):
    for combination in itertools.combinations(numbers, times):
        if sum(combination) == 2020:
            return combination


with open('input.txt') as f:
    numbers = [int(line.rstrip()) for line in f]

answer = math.prod(get_combinations(numbers, 2))
print(f"Task 1 first part answer: {answer}")

answer = math.prod(get_combinations(numbers, 3))
print(f"Task 1 second part answer: {answer}")
