from itertools import combinations

file = open(r'C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 5\input.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read().splitlines()

index = 0
rules = []
updates = []

for line in lines:
    if index < 1176:
        rules.append(line)
    elif index > 1176:
        updates.append(line)
    index += 1

rules = [rule.split("|") for rule in rules]
for rule in rules:
    rule[0] = int(rule[0])
    rule[1] = int(rule[1])
    
updates = [update.split(",") for update in updates]
for update in updates:
    for i in range(len(update)):
        update[i] = int(update[i])

def getPairs(list):
    length = len(list)
    pairs = []
    for i in range(length):
        for j in range(length-i):
            if list[i]==list[j+i]:
                continue
            pairs.append((list[i],list[j+i]))
    return pairs

def checkUpdate():
    res = []
    for update in updates:
        fail = False
        pairs = getPairs(update)
        for pair in pairs:
            for rule in rules:
                if pair[0]==rule[1] and pair[1]==rule[0]:
                    fail = True
                    break
        if fail == False:
            res.append(update[len(update)//2])    
    x = 0
    for r in res:
        x += r
    print(x)

checkUpdate()

def checkOneUpdate(update):
    fail = False
    fail_rule = None
    pairs = getPairs(update)
    for pair in pairs:
        for rule in rules:
            if pair[0]==rule[1] and pair[1]==rule[0]:
                fail = True
                fail_rule = rule
    return fail,fail_rule
        

def correctWrongUpdates():
    total = 0
    for update in updates:
        ever_invalid = False
        valid = False
        while not valid:
            print("Current update: "+str(update))
            valid = True
            fail, fail_rule = checkOneUpdate(update)
            if fail == False:
                break
            else:
                ever_invalid = True
                valid = False
                idx1 = update.index(fail_rule[0])
                idx2 = update.index(fail_rule[1])
                tmp = update[idx1]
                update[idx1] = update[idx2]
                update[idx2] = tmp
        if ever_invalid == True:
            total += update[len(update)//2]
    print(total)
correctWrongUpdates()