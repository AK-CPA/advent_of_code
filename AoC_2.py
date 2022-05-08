lines = []
with open('input.txt') as f:
    lines = f.readlines()

input =[]

for line in lines:
    input.append(int(line))

x=0
input_length = len(input)
sum_count = 0

#First Problem
for num in range(0,input_length-1):
    if input[x] < input[x+1]:
        sum_count +=1
    x+=1

print("First Answer:" + str(sum_count))

x=0
input_length = len(input)
sum_count = 0

#Second Problem
for num in range(0,input_length-3):
    first_sum = input[x] + input[x+1] + input[x+2]
    second_sum = input[x+1] + input[x+2] + input[x+3]
    if first_sum < second_sum:
        sum_count +=1
    x+=1

print("Second Answer:" + str(sum_count))
fff

