file = open(r"C:\Users\René\Documents\GitHub\AdventOfCode\AdventOfCode2024\Day 2\Project 1\data.txt")
data = file.readlines()

sumSafe = 0
for line in data:
    report = line.split()
    for i in range(len(report)):
        report[i] = int(report[i])
    increase = True
    index = 0
    safe = True

    print(report)

    while index < len(report)-1 and safe == True:
        if index == 0: 
            if report[index] == report[index+1]:
                safe = False
                print("Not safe because first two level are the same")
            else:
                if report[index] < report[index+1]:
                    increase = True
                    if (report[index] + 3) < report[index+1]:
                        safe = False
                        print("Not safe because first two level increase by too much")
                else:
                    increase = False
                    if (report[index] - 3) > report[index+1]:
                        safe = False
                        print("Not safe because first two level decrease by too much")
        else:
            if increase:
                if report[index] >= report[index+1]:
                    safe = False
                    print("Level "+str(index)+" is bigger than level "+str(index+1)+". Should be smaller")
                else:
                    if (report[index] + 3) < report[index+1]:
                        safe = False
                        print("Not safe because level " +str(i)+" and level "+str(i+1)+ " increase by too much")
            else:
                if report[index] <= report[index+1]:
                    safe = False
                    print("Level "+str(index)+" is smaller than level "+str(index+1)+". Should be bigger")
                else:
                    if (report[index] - 3) > report[index+1]:
                        safe = False
                        print("Not safe because level " +str(i)+" and level "+str(i+1)+ " decrease by too much")
        index += 1
    if safe:
        sumSafe += 1
        print("Report was safe")

print(sumSafe)
    
