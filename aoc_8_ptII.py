input_file = open('input.txt')
input = input_file.read().splitlines()

output = []
observation = []
observation_sorted = []
output_sorted = []

for i in input:
    i_split = i.split("|")
    output.append(i_split[1].split(" "))

for i in input:
    i_split = i.split("|")
    observation.append(i_split[0].split(" "))

for line in observation:
    append = []
    for digit in line:
        append.append("".join(sorted(digit)))
    observation_sorted.append(append)



for line in output:
    append = []
    line.remove('')
    for digit in line:
        append.append("".join(sorted(digit)))
    output_sorted.append(append)



answer_sum = 0
line_track = 0

for line in observation_sorted:
    dict = {}
    for digit in line:
        if (len(digit)) == 2:
            dict[1] = digit
        elif (len(digit)) == 3:
            dict[7] = digit
        elif (len(digit)) == 4:
            dict[4] = digit
        elif (len(digit)) == 7:
            dict[8] = digit

    for digit in line:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            continue

        elif len(digit) == 5:

            a = min(digit.find(dict[4][0]), 0)
            b = min(digit.find(dict[4][1]), 0)
            c = min(digit.find(dict[4][2]), 0)
            d = min(digit.find(dict[4][3]), 0)

            if (digit.find(dict[7][0]) >= 0) and (digit.find(dict[7][1]) >= 0) and (digit.find(dict[7][2]) >= 0):
                dict[3] = digit

            elif (a+b+c+d) == -1:
                dict[5] = digit

            elif (a + b + c + d) == -2:
                dict[2] = digit

        elif len(digit) == 6:

            a = min(digit.find(dict[4][0]), 0)
            b = min(digit.find(dict[4][1]), 0)
            c = min(digit.find(dict[4][2]), 0)
            d = min(digit.find(dict[4][3]), 0)
            e = min(digit.find(dict[7][0]), 0)
            f = min(digit.find(dict[7][1]), 0)
            g = min(digit.find(dict[7][2]), 0)

            if (a+b+c+d) == 0:
                dict[9] = digit

            elif (e+f+g) == 0:
                dict[0] = digit

            else:
                dict[6] = digit

    print("##")
    print(line_track)
    answer_string = ''
    for digit in output_sorted[line_track]:
        for number,string in dict.items():
            if string == digit:
                print(number)
                answer_string += str(number)

    print(answer_string)
    answer_sum += int(answer_string)
    line_track += 1

print(answer_sum)












