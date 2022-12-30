from messages.messages import *


def validate_answer(answer, correct_answer):
    all_checks_good = False
    if validate_length(len(answer), len(correct_answer)):
        all_checks_good = True
    else:
        all_checks_good = False
        print(ERROR_LENGTH_MESSAGE)

    return all_checks_good


def validate_length(user_length, correct_length):
    is_checked = False
    if correct_length // user_length > 2:
        is_checked = False
    else:
        is_checked = True
    return is_checked
