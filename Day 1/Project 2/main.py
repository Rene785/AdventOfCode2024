leftInput = []
rightInput = []

file = open("data.txt","r")
data = file.readlines()
for line in data:
    word = line.split()
    leftInput.append(int(word[0]))
    rightInput.append(int(word[1]))

leftInput.sort()
rightInput.sort()

i = 0
similarityScore = 0

for currentLeftInput in leftInput:
    factor = 0
    for currentRightInput in rightInput:
        if currentLeftInput==currentRightInput:
            factor +=1
    similarityScore += currentLeftInput*factor

print(similarityScore)