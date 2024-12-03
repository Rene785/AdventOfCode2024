import re

file = open(r"C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 3\Project 1\puzzle_input.txt")
data = file.readlines()

pattern = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
result = 0
for line in data:
    for match in pattern.findall(line):
        match = match.split(",")
        print(match)
        result += int(match[0]) * int(match[1])

print(result)