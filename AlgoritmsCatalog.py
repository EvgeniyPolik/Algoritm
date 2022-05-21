def prime_number():  # определение простого числа
    test_number_str = input('Введите проверяемое число: ')
    try:
        test_number_int = int(test_number_str)
        prime = True
        # Проверяем если число меньше 10 проверяем все числа, иначе до квадратного корня числа
        # Так как все делители должны как правило находятся до этого числа
        number_of_repit = round(test_number_int ** 0.5) if test_number_int > 10 else test_number_int
        for i in range(2, number_of_repit):
            if test_number_int % i == 0:
                prime = False
        if prime:
            print('Введенное число ' + test_number_str + ' - простое')
        else:
            print('Введенное число ' + test_number_str + ' - составное')
    except ValueError:
        print('Ошибка, введенно не число')


def liner_search(better):
    while True:
        count_array_str = input('Введите длинну массива или stop для выхода: ')
        if count_array_str == 'stop':
            break
        found_num = input('Введите искомое значение: ')
        try:
            count_array_int = int(count_array_str)
            mass = []
            for i in range(count_array_int):
                mass.append(input('Введите элемент массива № ' + str(i + 1) + ': '))
            answer = 'Not found'
            for j in range(count_array_int):
                if mass[j] == found_num:
                    answer = str(j + 1)
                    if better:
                        answer += ' (Улучшенный поиск)';
                        break
            print('Искомый элемент находится на позиции: ' + answer)
        except ValueError:
            print('Не верно введена длинна массива')

def sentinel_liner_search():
    while True:
        count_array_str = input('Введите длину массива или stop для выхода: ')
        if count_array_str == 'stop':
            break
        found_num = input('Введите искомое значение: ')
        try:
            count_array_int = int(count_array_str)
            mass = []
            for i in range(count_array_int):
                mass.append(input('Введите элемент массива № ' + str(i + 1) + ':'))
            answer = 'Not found'
            if mass[len(mass) - 1] == found_num:
                answer = count_array_str
            else:
                last = mass[len(mass) - 1]
                mass[len(mass) - 1] = found_num
                i = 0
                while True:
                    if mass[i] == found_num:
                        if i + 1 != count_array_int:
                            answer = str(i + 1)
                        break
                    else:
                        i += 1
                mass[len(mass) - 1] = last
            print('Искомый элемент находится на позиции: ' + answer)
        except ValueError:
            print('Неверно ведена длинна массива')