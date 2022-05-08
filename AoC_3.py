##Input
with open('input.txt') as f:
    input = []
    input = [x.rstrip() for x in f]


##Part 1
string_length = len(input[0])

gamma = ""
epsilon = ""

for x in range(string_length):
    zero = 0
    one = 0

    for line in input:
        if int(line[x]) == 0:
            zero += 1

        if int(line[x]) == 1:
            one += 1

    if one > zero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma_int =   int(gamma,2)
epsilon_int = int(epsilon,2)
print("The first answer is:")
print(gamma_int * epsilon_int)


##Part 2
oxygen_generator_list = input
string_length = len(input[0])
oxygen_generator_check =''

for x in range(string_length):
    zero = 0
    one = 0

    for line in oxygen_generator_list:
        if int(line[x]) == 0:
            zero += 1

        if int(line[x]) == 1:
            one += 1

    if one >= zero:
        oxygen_generator_check +='1'
    else:
        oxygen_generator_check +='0'


    for line in oxygen_generator_list:
        if (one > zero) or (one == zero):
            if int(line[x]) != 1:
                oxygen_generator_list = list(filter(lambda val: val != line, oxygen_generator_list))
        else:
            if int(line[x]) != 0:
                oxygen_generator_list = list(filter(lambda val: val != line, oxygen_generator_list))


############

co2_scrubber_input = input
string_length = len(input[0])
co2_scrubber_rating = ''

for x in range(string_length):
    zero = 0
    one = 0

    for line in co2_scrubber_input:
        if int(line[x]) == 0:
            zero += 1

        if int(line[x]) == 1:
            one += 1

    if zero <= one:
        co2_scrubber_rating +='0'
    else:
        co2_scrubber_rating +='1'

    for line in co2_scrubber_input:
        if zero <= one:
            if int(line[x]) != 0:
                co2_scrubber_input = list(filter(lambda val: val != line, co2_scrubber_input))
        else:
            if int(line[x]) != 1:
                co2_scrubber_input = list(filter(lambda val: val != line, co2_scrubber_input))

    if len(co2_scrubber_input) == 1:
        break

print(co2_scrubber_input)
print("The Second Answer is")
oxygen_integer = int(oxygen_generator_list[0],2)
co2_integer = int(co2_scrubber_input[0],2)
life_support_rating = oxygen_integer * co2_integer
print(life_support_rating)
