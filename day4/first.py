import re


def validate_byr(byr):
    yr = int(byr)
    return 1920 <= yr and yr <= 2002

def validate_iyr(iyr):
    yr = int(iyr)
    return 2010 <= yr and yr <= 2020

def validate_eyr(eyr):
    yr = int(eyr)
    return 2020 <= yr and yr <= 2030

def validate_hgt(hgt):
    if "cm" == hgt[-2:]:
        height = int(hgt.replace("cm", ""))
        return 150 <= height and height <= 193
    if "in" == hgt[-2:]:
        height = int(hgt.replace("in", ""))
        return 59 <= height and height <= 76 

def validate_hcl(hcl):
    return bool(re.match(r"^#[0-9a-f]{6}$", hcl))

def validate_ecl(ecl):
    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validate_pid(pid):
    return bool(re.match(r"^[0-9]{9}$", pid))

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


pattern = r'[a-z]+:\S+'

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

passports = []
passport = {}

for string in lines:
    if string != "":
        results = re.findall(pattern, string)
        for result in results:
            key, value = result.split(":")
            passport[key] = value
    else:
        passports.append(passport)
        passport = {}

passports.append(passport)

valid_passports_count = 0
valid_passports = []

# first part
for passport in passports:
    if set(required_fields).issubset(set(passport)):
        valid_passports_count += 1
        valid_passports.append(passport)

print(valid_passports_count)

valid_passports_count = 0

for passport in valid_passports:
    valid = True

    valid *= bool(validate_byr(passport["byr"]))
    valid *= bool(validate_iyr(passport["iyr"]))
    valid *= bool(validate_eyr(passport["eyr"]))
    valid *= bool(validate_hgt(passport["hgt"]))
    valid *= bool(validate_hcl(passport["hcl"]))
    valid *= bool(validate_ecl(passport["ecl"]))
    valid *= bool(validate_pid(passport["pid"]))

    if valid:
        valid_passports_count += 1

print(valid_passports_count)