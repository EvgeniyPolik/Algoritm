import AlgoritmsCatalog

algoritms = {1: 'Простое число'}  # Словарь алгоритмов


def doalgoritm(type_of_algoritm):  # Метод запуска соответсвующего алгоритма
    print('Выбран алгоритм \'' + algoritms[type_of_algoritm] + '\'')
    if type_of_algoritm == 1:  # 1 это алгоритм определения простого число
        AlgoritmsCatalog.prime_number()


while True:
    print('Введите название алгоритма:')
    for key in algoritms:  # Выведем список
        print(key, algoritms[key])
    print('Для завершения введите \'exit\'')
    selectAlgoritm = input('#:')
    if selectAlgoritm.lower() == 'exit':
        exit(0)
    elif not int(selectAlgoritm) in algoritms:
        print('Не верный ввод, попробуйте еще раз')
    else:
        doalgoritm(int(selectAlgoritm))
