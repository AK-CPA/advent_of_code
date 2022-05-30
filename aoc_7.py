from statistics import mean, median

input_file = open('input.txt')
input = input_file.read().split(",")
input = [int(i) for i in input]
num_of_crabs = len(input)

answer_list = []

for i in range(1,max(input)):

    total_fuel = 0
    for c in range(0,num_of_crabs):
        fuel_distance = abs(i - input[c])

        for x in range(1,fuel_distance+1):
            total_fuel += (1*x)

    answer_list.append(total_fuel)

answer_list.sort()
print("The answer to part II is")
print(answer_list[0])











