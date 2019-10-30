import random

def question(s):
    while True:
        result = input(s)
        if result in ["да", "д", "yes", "y", "1", "lf"]:
            return True
        if result in ["нет", "н", "no", "n", "0", "2", "ytn"]:
            return False
        print("Я не понимаю")

def privet(x, y):
    print("Привет!")

    while True:
        print("Если вы хотите загадывать число, введите 1")
        print("Если вы хотите отгадывать число, введите 2")
        variant = input("Ваш вариант:")

        if variant == "2":
            otgadat(x, y)
        else:
            zagadat(x, y)

        if not question("Хотите сыграть ещё? (да/нет)"):
            break

    print("Пока!")


def zagadat(x, y):
    input("Загадайте число от {} до {} и нажмите Enter".format(x, y))
    x -= 1
    y += 1
    while True:
        z = (x + y) // 2

        if question("Загаданное число {}? (да/нет)".format(z)):
            break

        if question("Загаданное число меньше? (да/нет)"):
            y = z
        else:
            x = z

        if y - x < 2:
            print("Вы что-то напутали")
            return

    print("Ура, я угадал!")


def otgadat(x, y):
    number = random.randint(x, y+1)

    while True:
        a = input("Угадайте число:")
        a = int(a)

        if a == number:
            break
        elif number < a:
            print("Загаданное число меньше")
        else:
            print("Загаданное число больше")

    print("Поздравляю, Вы угадали!")


if __name__ == "__main__":
    privet(1, 100)
