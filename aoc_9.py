input_file = open('input.txt')
input = input_file.read().splitlines()

total_array = []

for i in input:
    interim_array = []
    for num in i:
        interim_array.append(num)
    total_array.append(interim_array)

total_vert_count = len(total_array)
total_horizontal_count = len(total_array[0])

line_count = 0
answer_one = 0
for line in total_array:
    value_count = 0

    for value in line:
        low_check = 0
        value = int(value)

        try:
            up_value    = int(total_array[line_count-1][value_count])
        except:
            pass

        try:
            down_value  = int(total_array[line_count+1][value_count])
        except:
            pass

        try:
            right_value  = int(line[value_count+1])
        except:
            pass

        try:
            left_value  = int(line[value_count-1])
        except:
            pass

        if line_count -1 == -1:
            low_check +=1
        elif value < up_value:
            low_check +=1

        if line_count +1 == 100:
            low_check +=1
        elif value < down_value:
            low_check +=1

        if value_count - 1 == -1:
            low_check += 1
        elif value < left_value:
            low_check += 1

        if value_count + 1 == 100:
            low_check += 1
        elif value < right_value:
            low_check += 1

        if low_check == 4:
            answer_one +=(value+1)

        value_count += 1
    line_count += 1

print(answer_one)