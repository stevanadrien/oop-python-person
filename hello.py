import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
    return winnings


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please insert amount greater than zero")
        else:
            print("Enter a number")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            elif 1 >= lines <= MAX_LINES:
                print("Number is too small")
            else:
                print("Number is too large")
        else:
            print("Enter a number")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if bet >= 1 and bet <= 100:
                print("YOUR BET IS VALID")
                break
            elif bet >= 100:
                print("Sorry, maximum bet is 100$")
            else:
                print("Sorry, the minimum bet is 1$ and max is 100$")
        else:
            print("Enter a number")
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total = bet * lines
    while True:
        if total > balance:
            kurang = total - balance
            print(
                f"Your balance is not enough, your current balance is: {balance}, you need to add ${kurang} more balance"
            )
        else:
            lebih = balance - total
            print(f"your balance is enough, now your balance is: {lebih}")
        break
    print(f"Your bet is: {bet} on {lines} line, Total bet is equal to : {total}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won {winnings}")


main()
