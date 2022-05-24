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

original_bingo_card_array = bingo_card_array
bingo_number_count = 1
bingo_check_row = 0
bingo_check_column = 0

last_winning_card = []
last_winning_number = 0
winning_card_array = []
last_card = []



for bingo_rounds in range(1,number_of_bingo_rounds):
    card_count = 0
    column_row_check = []
    row_check = []
    card = bingo_card_array[32]
    print(card)

    for row in card:
        bingo_check_row =0
        row_check = []
        for number in row:
            for i in range(0, bingo_rounds):
                bingo_number = bingo_numbers_int[i]
                if int(number) == bingo_number:
                    bingo_check_row +=1
                    row_check.append(bingo_number)
                    if bingo_check_row == 5:
                        print("row bingo")
                        print(bingo_number)

    for column_count in range(0,5):
        bingo_check_column = 0
        for row_count in range(0,5):
            for i in range(0, bingo_rounds):
                bingo_number = bingo_numbers_int[i]
                if int(bingo_card_array[card_count][row_count][column_count]) == bingo_number:
                    bingo_check_column +=1
                    column_row_check.append(bingo_number)

                    if bingo_check_column == 5:
                        print("column bingo")
                        print(bingo_number)


        bingo_check_row = 0
        bingo_check_column =0
        winning_row = []
        row_check = []
        column_row_check = []

    card_count += 1

##bingo card 32

print(bingo_card_array[32])











