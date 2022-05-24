##Input
input_file = open('input.txt')
file_contents = input_file.read()

content_split = file_contents.splitlines()
input_length = len(content_split)


white_space_count = 0
bingo_numbers = []

bingo_card_array = []
bingo_card = []

for i in range(0,input_length):

    if content_split[i] == "":
        white_space_count += 1

    if white_space_count == 0:
        bingo_numbers.append(content_split[i])

    if white_space_count > 1 and content_split[i] == "":
        bingo_card_array.append(bingo_card)
        bingo_card = []

    if (white_space_count > 0) and (content_split[i] != ""):
        bingo_card.append(content_split[i].split(" "))

bingo_card_length = len(bingo_card_array)

for card in bingo_card_array:
    for row in card:
        for number in row:
            if number == '':
                row.remove(number)

bingo_numbers = bingo_numbers[0].split(",")

bingo_numbers_int = []
for i in bingo_numbers:
    bingo_numbers_int.append(int(i))

number_of_bingo_rounds = len(bingo_numbers_int)


# original_bingo_card_array_length = len(bingo_card_array)
# bingo_number_count = 1
# bingo_check_row = 0
# bingo_check_column = 0
#
# last_winning_card = []
# last_winning_number = 0
# winning_card_array = []
# last_card = []
#
# win_counter = 0

#last_winning_card = [['66', '43', '12', '10', '70'], ['79', '57', '54', '41', '6'], ['46', '73', '40', '3', '52'], ['36', '21', '38', '8', '62'], ['7', '26', '42', '32', '0']]


def bingo_check(card_array):
    for i in range(0, number_of_bingo_rounds):
        for card in card_array:
            for row in card:
                bingo_check_row = 0
                for number in row:
                    for x in range(0,i):
                        bingo_number = bingo_numbers_int[x]
                        if int(number) == bingo_number:
                            bingo_check_row +=1
                            if bingo_check_row == 5 and len(card_array)>1:
                                card_array.remove(card)
                                bingo_check(card_array)
                            elif bingo_check_row == 5 and len(card_array)==1:
                                print("row bingo")
                                print(card)
                                print(bingo_number)
                                print(i)


            for column_count in range(0,5):
                bingo_check_column = 0
                for row_count in range(0,5):
                    for x in range(0,i):
                        bingo_number = bingo_numbers_int[x]
                        if int(card[row_count][column_count]) == bingo_number:
                            bingo_check_column +=1
                            if bingo_check_column == 5 and len(card_array)>1:
                                card_array.remove(card)
                                bingo_check(card_array)

                            elif bingo_check_column == 5 and len(card_array)==1:
                                print("column bingo")
                                print("winning card")
                                print(card)
                                print("winning number")
                                print(bingo_number)
                                print("bingo round")
                                print(i)
                                return

bingo_check(bingo_card_array)


print('indices')
print(bingo_numbers_int.index(52))
print(bingo_numbers_int.index(35))
print(bingo_numbers_int.index(43))
print(bingo_numbers_int.index(77))
print(bingo_numbers_int.index(79))

last_winning_card = [['52', '35', '43', '77', '79'], ['53', '56', '93', '92', '12'], ['15', '23', '16', '10', '66'], ['63', '96', '58', '60', '94'], ['6', '55', '76', '21', '89']]

sum = 0
for row in last_winning_card:
    for number in row:
        sum = sum + int(number)

negative_sum =0

for row in last_winning_card:
    for number in row:
        for i in range(0,85):
            if int(number) == bingo_numbers_int[i]:
                negative_sum = negative_sum + int(number)

print("sum")
print(sum)
print("negative sum")
print(negative_sum)

first_number = sum-negative_sum
second_number = 52

print(first_number*second_number)
















