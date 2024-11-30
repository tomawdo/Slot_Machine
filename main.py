import random
from icecream import ic

NR_MAX_QUOTE = 3
MAX_SCOMMESSA = 100
MIN_SCOMMESSA = 5

# struttura ruota slotmachine 3 righe * 3 colonne
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_counts in symbols.items():
        for _ in range(symbol_counts):
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

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Quanto vuoi caricare? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                ic("L'importo deve essere maggiore di 0 (zero).")
        else:
            ic("Inserisci un importo corretto.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Quante quote vuoi scommettere (1 - " + str(NR_MAX_QUOTE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= NR_MAX_QUOTE:
                break
            else:
                ic("Inserisci un numero valido di quote.")
        else:
            ic("Attenzione! Inserisci un numero.")
    return lines

def get_bet():
    while True:
        amount = input("Quanto vuoi scommettere per ogni riga? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_SCOMMESSA <= amount <= MAX_SCOMMESSA:
                break
            else:
                ic(f"L'importo per ogni riga dev'essere tra €{MIN_SCOMMESSA} - €{MAX_SCOMMESSA}.")
        else:
            ic("Inserisci un importo.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    bet = float(get_bet())
    total_bet = float(bet * lines)

    if total_bet > balance:
        print(f"Non hai sufficiente credito. Il tuo saldo è: €{balance}")
    else:
        print(f"Hai scommesso €{bet} su {lines} quote. Totale: €{total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Hai vinto €{winnings}!")
    print(f"Quote vinte: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Il tuo saldo: €{balance}")
        answer = input("Premi INVIO per giocare (u per uscire).")
        if answer == "u":
            break
        balance += spin(balance)

    print(f"Alla prossima! Il saldo residuo è €{balance}")


main()