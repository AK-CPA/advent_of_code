from collections import Counter

##Input
input_file = open('input.txt')
file_contents = input_file.read()

input_list = file_contents.replace(" -> ",",")
input_list = input_list.splitlines()



line_list = []

for line in input_list:
    x = line.split(",")
    line_list.append(x)

board_dict = {

}

for line in line_list:
    for i in range(0,4):
        line[i] = int(line[i])

point_list = []

##Vertical Lines
for line in line_list:

    if line[0] == line[2]:

        top_point = int(max(line[1],line[3]))
        bottom_point = int(min(line[1],line[3]))
        loop_count = top_point - bottom_point + 1

        for i in range(0,loop_count):
            point = str(line[0])+","+str(bottom_point+i)
            point_list.append(point)


##Horizontal Lines

    elif line[1] == line[3]:

        right_point = int(max(line[0],line[2]))
        left_point = int(min(line[0],line[2]))
        loop_count = right_point - left_point + 1

        for i in range(0,loop_count):
            point = str(left_point+i)+","+str(line[3])
            point_list.append(point)

##Diagonal Line
    else:
        print(line)
        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]
        loop_count = abs(x2 - x1) + 1

        for i in range(0,loop_count):
            if x1 < x2:
                if y1 < y2:
                    point = str(x1 + i) + "," + str(y1 + i)
                    point_list.append(point)
                    print(point)
                else:
                    point = str(x1 + i) + "," + str(y1 - i)
                    point_list.append(point)
                    print(point)
            else:
                if y1 < y2:
                    point = str(x1 - i) + "," + str(y1 + i)
                    point_list.append(point)
                    print(point)
                else:
                    point = str(x1 - i) + "," + str(y1 - i)
                    point_list.append(point)
                    print(point)


counter = Counter(point_list)

point_count = 0
for value in counter.values():
    if value >1:
        point_count = point_count + 1

print ("Number of points with overlap")
print (point_count)







