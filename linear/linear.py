import random

BOARD_SIZE = 10
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def question(s):
    while True:
        result = input(s)
        if result in ["х", "Х", "1", "x", "X"]:
            return "x"
        if result in ["о", "О", "O", "o", "0", "2"]:
            return "o"
        print("Я не понимаю")


def print_board(board):
    print('  ', end='')
    for letter in LETTERS[:BOARD_SIZE]:
        print(letter, end=' ')
    print()

    print('[ ', end='')
    for symbol in board:
        print(symbol, end=' ')
    print(']')


xxx = ['x', 'x', 'x']
ooo = ['o', 'o', 'o']


def found_winner(board):
    for i in range(len(board) - 2):
        if board[i:i+3] == xxx:
            return 'x'
        if board[i:i+3] == ooo:
            return 'o'
    if '-' not in board:
        return '*'
    return None


def play(igrok):
    board = ['-'] * BOARD_SIZE
    turn = "x"
    while True:
        print_board(board)
        result = found_winner(board)
        if result == "x":
            print("Победили крестики!")
            return
        elif result == "o":
            print("Победили нолики!")
            return
        elif result == "*":
            print("Ничья!")
            return
        else:
            print("Пока никто не победил")
            if turn == igrok:
                play_igrok(board, turn)
            else:
                play_computer(board, turn)
            turn = 'o' if turn == 'x' else 'x'


def play_igrok(board, turn):
    while True:
        letter = input("Ваш ход, выберите клетку A-{}:".format(LETTERS[BOARD_SIZE-1]))
        letter = letter.upper()
        try:
            pos = LETTERS[:BOARD_SIZE].index(letter)
        except ValueError:
            print("Неправильное значение")
        else:
            if board[pos] == '-':
                board[pos] = turn
                return
            else:
                print("Это поле занято!")


def play_computer(board, turn):
    free = [i for i, v in enumerate(board) if v == '-']
    pos = random.choice(free)
    board[pos] = turn


if __name__ == '__main__':
    igrok = question("Крестики ходят первыми. Чем Вы хотите играть? х/о")
    play(igrok)
