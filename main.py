import openpyxl
import random

file_name = 'englishcards.xlsx'
menu_options = {
    1: 'Random terms',
    2: 'Random definitions',
    3: 'Exit',
}

tmp1 = []
tmp2 = []
SUCCESS = 'Правильно!'
ERROR = 'Неправильно...'


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def read_file():
    wb = openpyxl.load_workbook(file_name)
    ws = wb.active

    # Iterate the loop to read the cell values
    for row in range(0, ws.max_row):
        for col in ws.iter_cols(0, 1):
            tmp1.append(col[row].value)

    for row in range(0, ws.max_row):
        for col in ws.iter_cols(2, 2):
            tmp2.append(col[row].value)


def ask_and_check(mode):
    terms = [i for i in tmp1 if i is not None]
    definitions = [i for i in tmp2 if i is not None]
    size = len(terms) - 1
    answer = ''
    while answer != 'x':
        random_index = random.randint(0, size)
        if mode == 1:
            print('-' * 100)
            print(f'What is: {terms[random_index]}?')
            answer = input('Answer: ')
            if answer in definitions[random_index]:
                print(SUCCESS)
                print()
            else:
                print(ERROR)
                print('Правильно вот так: ' + definitions[random_index])
                print()
        elif mode == 2:
            print('-' * 100)
            print(f'Как называется термин {definitions[random_index]}? ')
            answer = input('Answer: ')
            if answer in terms[random_index]:
                print(SUCCESS)
                print()
            else:
                print(ERROR)
                print('Правильно вот так: ' + terms[random_index])
                print()


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
