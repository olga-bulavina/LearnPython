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


def found_winner(board):
    for i in range(len(board) - 2):
        pass


def play(igrok):
    board = ['-'] * BOARD_SIZE
    turn = "x"
    result = found_winner(board)
    if result == "x":
        print("Победили крестики!")
    elif result == "0":
        print("Победили нолики!")
    else:
        pass




if __name__ == '__main__':
    igrok = question("Крестики ходят первыми. Чем Вы хотите играть? х/о")
    play(igrok)
