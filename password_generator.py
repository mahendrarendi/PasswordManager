# inisiasi libarary
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate(nr_letters, nr_symbols, nr_numbers):
    if nr_letters < 0:
        nr_letters = 0

    if nr_letters > len(letters):
        nr_letters = len(letters)

    if nr_symbols < 0:
        nr_symbols = 0

    if nr_symbols > len(symbols):
        nr_symbols = len(symbols)

    if nr_numbers < 0:
        nr_numbers = 0

    if nr_numbers > len(numbers):
        nr_numbers = len(numbers)

    list_letter = []
    while len(list_letter) < nr_letters:
        letter = random.choice(letters)

        if letter not in list_letter:
            list_letter.append(letter)

    list_symbol = []
    while len(list_symbol) < nr_symbols:
        symbol = random.choice(symbols)

        if symbol not in list_symbol:
            list_symbol.append(symbol)

    list_numbers = []
    while len(list_numbers) < nr_numbers:
        number = random.choice(numbers)

        if number not in list_numbers:
            list_numbers.append(number)

    password = []
    password.extend(list_letter)
    password.extend(list_symbol)
    password.extend(list_numbers)

    final_password = random.sample(password, len(password))

    return "".join(final_password)