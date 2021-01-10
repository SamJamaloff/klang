import gspread

FILENAME = 'keys.json'
ONLINE_FILENAME = 'klang'

def get_spreadsheet_values():
    gspread_obj = gspread.service_account(filename=FILENAME)
    usingsheet = gspread_obj.open(ONLINE_FILENAME)
    worksheet = usingsheet.sheet1
    return worksheet.get_all_values()

import random # because we will need it

def compare_data(array_data):
    wrong_answers = []
    counter4rights = 0

    for _ in range(10):
        random_number = random.randint(1, len(array_data))
        word_array = array_data[random_number-1]
        answer = input(f"Enter matching word for: {word_array[0]} -> ")
        if answer.lower() == word_array[1].lower():
            print("Boom you did it!!!")
            counter4rights += 1
        else:
            wrong_answers.append(word_array)
    wrong_answers.append(counter4rights)
    return(wrong_answers)

print(compare_data(get_spreadsheet_values()))
