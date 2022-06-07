input_file = open('input.txt')
input = input_file.read().splitlines()

output = []
observation = []

for i in input:
    i_split = i.split("|")
    output.append(i_split[1].split(" "))

for i in input:
    i_split = i.split("|")
    observation.append(i_split[0].split(" "))

count = 0
for a in output:
    for b in a:
        if (len(b)) == 2:
            count += 1
        elif (len(b)) == 3:
            count += 1
        elif (len(b)) == 4:
            count += 1
        elif (len(b)) == 7:
            count += 1

print("Answer 1 =", count )






