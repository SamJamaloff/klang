import random
from googleapiclient.discovery import build
from google.oauth2 import service_account

sheet_name = "class1"

def get_spreadsheet_values(name):
    cred_json_file = "keys.json"
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SAMPLE_SPREADSHEET_ID = '1HL8i0kzza4lZi9UVZjBuA5p6CGh2iLrxkVbbVWgerD4'
    cred = service_account.Credentials.from_service_account_file(cred_json_file, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=cred)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=name).execute()
    return result.get('values', [])

def compare_data(array_data):
    answers = []
    for _ in range(10):
        rand_number = random.randint(0, len(array_data))
        word_array = array_data[rand_number-1]
        answer = input("Enter matching word for " + word_array[0] + ": ")
        if answer.lower() == word_array[1].lower():
            print("Boom you did it!!!")
        else:
            answers.append(word_array)
    return answers

print(compare_data(get_spreadsheet_values(sheet_name)))