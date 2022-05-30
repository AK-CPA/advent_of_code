import math

input_file = open('input.txt')
file_contents = input_file.read()
input = file_contents.split(",")

number_of_starting_fish = len(input)
fish_list = []

for i in range(0,number_of_starting_fish):
    fish_list.append(int(input[i]))

original_number_of_fish = len(fish_list)
print(len(fish_list))

for i in range(1,81):
    number_of_fish = len(fish_list)
    print(i)

    for x in range(0,number_of_fish):
        if fish_list[x] == 0:
            fish_list.append(9)
            fish_list[x] = 7

    number_of_fish = len(fish_list)
    for x in range(0, number_of_fish):
        fish_list[x] = fish_list[x] - 1

    print("Day:",i, "Number of Fish",len(fish_list))

growth_rate = len(fish_list) / original_number_of_fish
print(growth_rate)

x = math.log(growth_rate)
print(x)
x = x/80
print(x)

final_answer_1 = 300*(math.e)**(x*80)
print(final_answer_1)

final_answer_2 = 300*(math.e)**(x*256)
print(final_answer_2)



