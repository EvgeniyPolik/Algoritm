import AlgoritmsCatalog

algoritms = {
            1: 'Простое число',
            2: 'Линейный поиск',
            3: 'Улучшенный линейный поиск',
            4: 'Сторожевой линейный поиск'
            }  # Словарь алгоритмов


def doalgoritm(type_of_algoritm):  # Метод запуска соответсвующего алгоритма
    print('Выбран алгоритм \'' + algoritms[type_of_algoritm] + '\'')
    if type_of_algoritm == 1:  # 1 это алгоритм определения простого число
        AlgoritmsCatalog.prime_number()
    elif type_of_algoritm == 2:
        AlgoritmsCatalog.liner_search(False)
    elif type_of_algoritm == 3:
        AlgoritmsCatalog.liner_search(True)
    elif type_of_algoritm == 4:
        AlgoritmsCatalog.sentinel_liner_search()

while True:
    print('Введите название алгоритма:')
    for key in algoritms:  # Выведем список
        print(key, algoritms[key])
    print('Для выхода введите \'exit\'')
    selectAlgoritm = input('#:')
    if selectAlgoritm.lower() == 'exit':
        exit(0)
    elif not int(selectAlgoritm) in algoritms:
        print('Не верный ввод, попробуйте еще раз')
    else:
        doalgoritm(int(selectAlgoritm))
