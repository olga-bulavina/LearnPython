voprosy1 = {
    'Корова': ['Рога', 'Живое'],
    'Самолёт': ['Летает', 'Не живое'],
    'Пылесос': ['Не летает', 'Не живое'],
    'Карась': ['Не Рога', 'Живое']
}

voprosy2 = {
    'question': 'Живое?',
    'yes': {
        'question': 'Есть рога?',
        'yes': 'Корова',
        'no': 'Карась',
    },
    'no': {
        'question': 'Летает?',
        'yes': 'Самолет',
        'no': 'Пылесос',
    }
}

voprosy3 = [
    'Живое?', [
        [
            'Есть рога?',
            'Корова',
            'Карась'
        ]
    ], [
            'Летает?',
            'Самолет',
            'Пылесос',
    ]
]

def yes_no(s):
    while True:
        result = input(s)
        if result in ["да", "д", "yes", "y", "1", "lf"]:
            return True
        if result in ["нет", "н", "no", "n", "0", "2", "ytn"]:
            return False
        print("Я не понимаю")

def jean1(vopros):
    while True:
        q = vopros['question']
        if yes_no(q+'да/нет'):
            otvet = vopros["yes"]
        else:
            otvet = vopros['no']
        if type(otvet)==str:
            print ('ответ:' + otvet)
            break
        else:
            vopros = otvet


if __name__ == '__main__':
    jean1(voprosy2)
