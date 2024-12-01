input1 = []
input2 = []

file = open("data.txt","r")
data = file.readlines()
for line in data:
    word = line.split()
    input1.append(int(word[0]))
    input2.append(int(word[1]))

input1.sort()
input2.sort()

sumDistance = 0
i=0
while i < 1000:
    sumDistance += abs(input1[i] - input2[i])
    i += 1

print(sumDistance)
