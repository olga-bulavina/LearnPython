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


def jean1(otvety):
    assert len(otvety) == 1
    vopros = otvety.keys()[0]
    da = otvety[vopros]['да']
    net = otvety[vopros]['нет']
    print(vopros)
    print(da)
    print(net)


if __name__ == '__main__':
    jean1(voprosy1)
