input_file = open('input.txt')
input = input_file.read().splitlines()

output = []

for i in input:
    i_split = i.split("|")
    output.append(i_split[1].split(" "))

count = 0
for a in output:
    for b in a:
        if (len(b)) == 1:
            count += 1
        elif (len(b)) == 4:
            count += 1
        elif (len(b)) == 7:
            count += 1
        elif (len(b)) == 8:
            count += 1

print("Answer 1 =", count )






