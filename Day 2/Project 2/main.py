def checkIfSafe(report):
    print(report)
    adjacent_pairs = list(zip(report, report[1:]))
    
    in_ascening_order = all(li >= ri for li, ri in adjacent_pairs)
    in_descending_order = all(li <= ri for li, ri in adjacent_pairs)

    differences = (abs(li-ri) for li,ri in adjacent_pairs)

    in_valid_range = all(diff in range(1,4) for diff in differences)

    return (in_ascening_order or in_descending_order) and in_valid_range

def checkIfSafeWhenRemoved(report):
    if checkIfSafe(report):
        return True
    reports_one_level_removed = [
        [level for idx, level in enumerate(report) if idx != idx_to_remove]
        for idx_to_remove in range(len(report))
    ]
    return any(checkIfSafe(r) for r in reports_one_level_removed)

file = open(r"C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 2\Project 1\data.txt")
data = file.readlines()

sumSafe = 0
for line in data:
    report = line.split()
    for i in range(len(report)):
        report[i] = int(report[i])
    
    if checkIfSafeWhenRemoved(report):
        sumSafe += 1
        
print(sumSafe)


