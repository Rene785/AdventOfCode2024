def FindPattern(matrix, pattern, coord, step):
    maxY = len(matrix)-1
    maxX = len(matrix[0])-1
    
    for p in list(pattern):
        if coord[0] < 0 or coord[0] > maxY:
            return False
        if coord[1] < 0 or coord[1] > maxX:
            return False
        if p != matrix[coord[0]][coord[1]]:
            return False
        
        coord[0] += step[0]
        coord[1] += step[1]
    
    return True


file = open(r'C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 4\input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read().splitlines()
file.close()

matrix = []

for i, line in enumerate(lines):
    matrix.append(list(line))
    
occurrences = 0

# part 1
for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        # go right
        if FindPattern(matrix, "XMAS", [y,x], (0,1)):
            occurrences += 1
        # go left
        if FindPattern(matrix, "XMAS", [y,x], (0,-1)):
            occurrences += 1
        # go up
        if FindPattern(matrix, "XMAS", [y,x], (-1,0)):
            occurrences += 1
        # go down
        if FindPattern(matrix, "XMAS", [y,x], (1,0)):
            occurrences += 1
        
        # go up right
        if FindPattern(matrix, "XMAS", [y,x], (-1,1)):
            occurrences += 1
        # go up left
        if FindPattern(matrix, "XMAS", [y,x], (-1,-1)):
            occurrences += 1
        # go down right
        if FindPattern(matrix, "XMAS", [y,x], (1,1)):
            occurrences += 1
        # go down left
        if FindPattern(matrix, "XMAS", [y,x], (1,-1)):
            occurrences += 1
            
print(occurrences)

#part 2
occurrences = 0

for y, row in enumerate(matrix):
    for x, col in enumerate(row):
        # check both diagonals
        if FindPattern(matrix, "MAS", [y,x], (1,1)) or FindPattern(matrix, "SAM", [y,x], (1,1)):
            if FindPattern(matrix, "MAS", [y+2,x], (-1,1)) or FindPattern(matrix, "SAM", [y+2,x], (-1,1)):
                occurrences += 1
    
    
print(occurrences)