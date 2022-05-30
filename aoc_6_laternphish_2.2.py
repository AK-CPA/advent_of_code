from collections import deque

input_file = open('input.txt')
file_contents = input_file.read()
input = file_contents.split(",")

number_of_starting_fish = len(input)

fish_list = [0] * 9
number_of_days = 256

for i in range(0,number_of_starting_fish):
    fish_list[int(input[i])] += 1

print(fish_list)
for i in range(0,number_of_days):
    print(i)
    fish_list[7] += fish_list[0]
    fish_list = fish_list[1:] + fish_list[:1]
    print(fish_list)

print("total number of fish", sum(fish_list))