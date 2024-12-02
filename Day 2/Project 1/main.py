file = open("data.txt","r")
data = file.readlines()

sumSafe = 0
for line in data:
    report = line.split()
    increase = True
    index = 0
    safe = True
    while index < len(report) and safe == True:
        if index == 0: 
            if report[index] == report[index+1]:
                safe = False
            else:
                if report[index] < report[index+1]:
                    increase = True
                    if (report[index] + 3) < report[index+1]:
                        safe = False
                else:
                    increase = False
                    if (report[index] - 3) > report[index+1]:
                        safe = False
        else:
            if increase:
                if report[index] <= report[index+1] or (report[index] + 3) < report[index+1]:
                    safe = False
            else:
                if report[index] >= report[index+1] or (report[index] - 3) > report[index+1]:
                    safe = False
        index += 1
    if safe:
        sumSafe += 1

print(sumSafe)
    
