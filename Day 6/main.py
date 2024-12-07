def get_input():
    file = open(r'C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 6\input.txt', mode = 'r', encoding = 'utf-8-sig')
    lines = file.read().splitlines()
    map = {}
    height = len(lines)
    width = len(lines[0])
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            map[(i, j)] = char
            if char == "^":
                guard_pos = (i, j)
                map[(i, j)] = "."
    return map, guard_pos,width,height

def calculate_path():
    map,guard_pos,_,_ = get_input()
    direction = "up"
    guard_valid = True
    distinct_positions = []
    distinct_positions.append(guard_pos)
    
    while True:
        distinct_positions.append(guard_pos)
        if direction == "up":
            if (guard_pos[0]-1,guard_pos[1]) not in map:
                break
            elif map[(guard_pos[0]-1,guard_pos[1])] == "#":
                direction = "right"
            else:
                guard_pos = (guard_pos[0]-1,guard_pos[1])
        elif direction == "right":
            if (guard_pos[0],guard_pos[1]+1) not in map:
                break
            elif map[(guard_pos[0],guard_pos[1]+1)] == "#":
                direction = "down"
            else:
                guard_pos = (guard_pos[0],guard_pos[1]+1)
        elif direction == "down":
            if (guard_pos[0]+1,guard_pos[1]) not in map:
                break
            elif map[(guard_pos[0]+1,guard_pos[1])] == "#":
                direction = "left"
            else:
                guard_pos = (guard_pos[0]+1,guard_pos[1])
        elif direction == "left":
            if (guard_pos[0],guard_pos[1]-1) not in map:
                break
            elif map[(guard_pos[0],guard_pos[1]-1)] == "#":
                direction = "up"
            else:
                guard_pos = (guard_pos[0],guard_pos[1]-1)
    
    print(len(set(distinct_positions)))

def checkCountOfObstructions():
    map,guard_pos,width,height = get_input()
    answer = 0

    for m in map.keys():
        if map[m] != ".":
            continue

        map[m] = "#"

        curr = guard_pos
        direction = "up"
        visited = set()
        visited.add((curr, direction))
        while True:
            if direction == "up":
                if curr[0] - 1 < 0:
                    break
                elif map[(curr[0] - 1, curr[1])] == "#":
                    direction = "right"
                else:
                    map[curr] = "."
                    curr = (curr[0] - 1, curr[1])
                    map[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "down":
                if curr[0] + 1 >= height:
                    break
                elif map[(curr[0] + 1, curr[1])] == "#":
                    direction = "left"
                else:
                    map[curr] = "."
                    curr = (curr[0] + 1, curr[1])
                    map[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "right":
                if curr[1] + 1 >= width:
                    break
                elif map[(curr[0], curr[1] + 1)] == "#":
                    direction = "down"
                else:
                    map[curr] = "."
                    curr = (curr[0], curr[1] + 1)
                    map[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))
            elif direction == "left":
                if curr[1] - 1 < 0:
                    break
                elif map[(curr[0], curr[1] - 1)] == "#":
                    direction = "up"
                else:
                    map[curr] = "."
                    curr = (curr[0], curr[1] - 1)
                    map[curr] = "^"
                    if (curr, direction) in visited:
                        answer += 1
                        break
                    else:
                        visited.add((curr, direction))

        map[curr] = "."
        map[guard_pos] = "^"
        map[m] = "."

    print(f"Part 2: {answer}")

calculate_path()
checkCountOfObstructions()