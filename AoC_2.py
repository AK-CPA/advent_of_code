##Input
with open('input.txt') as f:
    input = []
    input = [x.rstrip() for x in f]


##Part 1
horizontal = 0
vertical = 0

for line in input:
    if line[0] == 'f':
        horizontal += int(line[-1])

    if line[0] == 'u':
        vertical -= int(line[-1])

    if line[0] == 'd':
        vertical += int(line[-1])

print("The Answer is:x")
print(horizontal * vertical)

##Part 2
horizontal = 0
vertical = 0
aim= 0

for line in input:
    if line[0] == 'f':
        horizontal += int(line[-1])
        vertical += (int(line[-1])) * aim

    if line[0] == 'u':
        aim -= int(line[-1])

    if line[0] == 'd':
        aim += int(line[-1])

print("The Answer is:x")
print(horizontal * vertical)
