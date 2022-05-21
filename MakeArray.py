def MakeArray():
    while True:
        count_array_str = input('Введите длинну массива или stop для выхода: ')
        if count_array_str == 'stop':
            return 'stop', None
            break
        found_num = input('Введите искомое значение: ')
        try:
            count_array_int = int(count_array_str)
            mass = []
            for i in range(count_array_int):
                mass.append(input('Введите элемент массива № ' + str(i + 1) + ': '))
        except ValueError:
            print('Не верно введена длинна массива')
        return found_num, mass

