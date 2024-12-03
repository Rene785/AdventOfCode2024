import re

def findMatchWithDoAndDont():
    calc_enabled = True
    result = 0
    pattern = re.compile(r"mul\((\d{1,3},\d{1,3})\)|(do\(\))|(don\'t\(\))")
    for line in data:
        for match in pattern.findall(line):
            print(match)
            if match[1]:
                calc_enabled = True
            elif match[2]:
                calc_enabled = False
            else:
                if calc_enabled == True:
                    match = match[0].split(",")
                    result += int(match[0]) * int(match[1])
    return result

file = open(r"C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 3\Project 2\puzzle_input.txt")
data = file.readlines()

print(findMatchWithDoAndDont())