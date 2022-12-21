import openpyxl
import random

file_name = 'englishcards.xlsx'
menu_options = {
    1: 'Random terms',
    2: 'Random definitions',
    3: 'Exit',
}

terms = []
definitions = []

SUCCESS = 'Правильно!'
ERROR = 'Неправильно...'


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def read_file():
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active

    for row in ws.iter_rows(min_row=1, max_col=1, max_row=ws.max_row):
        for cell in row:
            terms.append(cell.value)
    for row in ws.iter_rows(min_row=1, min_col=2, max_row=ws.max_row):
        for cell in row:
            definitions.append(cell.value)


def ask_and_check(mode):
    while True:
        random_index = random.randint(0, len(terms) - 1)

        if mode == 1:
            print(f'Что такое {terms[random_index]}? ')
            answer = input()
            if answer in definitions[random_index]:
                print(SUCCESS)
            else:
                print(ERROR)
        elif mode == 2:
            print(f'Как называется термин {definitions[random_index]}? ')
            answer = input()
            if answer in terms[random_index]:
                print(SUCCESS)
            else:
                print(ERROR)


def start_test(mode):
    print('Нажми CTRL + C для выхода')
    read_file()
    ask_and_check(mode)


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            start_test(mode=1)
        elif option == 2:
            start_test(mode=2)
        elif option == 3:
            print('Thanks you for using...!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')
