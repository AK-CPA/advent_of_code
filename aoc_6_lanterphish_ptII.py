from collections import Counter

input_file = open('input.txt')
file_contents = input_file.read()
input = file_contents.split(",")

number_of_starting_fish = len(input)
fish_list = []

for i in range(0,number_of_starting_fish):
   fish_list.append(int(input[i]))


items = Counter(fish_list)
print(items)

fish_list = [1,2,3,4,5]

total_number_of_days = 256
total_number_of_fish = 0


def fish_count(days_remaining):
    global total_number_of_fish
    first_fish = 0
    day_count = 0

    while days_remaining > 0:
        if first_fish == 0:
            if day_count == 9:
                total_number_of_fish += 1
                fish_count(days_remaining)
                first_fish = 1

        else:
            if (day_count - 9) % 7 == 0:
                total_number_of_fish += 1
                fish_count(days_remaining)

        days_remaining -= 1
        day_count += 1


i=0
for fish in fish_list:
    print(i)
    i+=1
    total_number_of_fish += 1
    day_count = total_number_of_days
    fish_life = fish

    while day_count > 0:

        if fish_life > 0:
            fish_life -= 1

        else:
            fish_life = 6
            total_number_of_fish += 1
            fish_count(day_count)
        day_count -= 1


print("The total number of fish is", total_number_of_fish)





