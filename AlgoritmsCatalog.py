from MakeArray import MakeArray


def do_factorial(n):
    if n > 0:
        return n * do_factorial(n - 1)
    else:
        return 1


def factorial():
    number_str = input('Введение числодля определения факторила: ')
    try:
        number_int = int(number_str)
        print(f'Значение факториала для числа {number_int}: ' + str(do_factorial(number_int)))

    except ValueError:
        print('Ошибка, введено не число')


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


def liner_search(better):  # Простой линейный поиск и улучшенный линейный поиск
    found_num, mass = MakeArray()
    if found_num != 'stop':
        answer = 'Not found'
        for j in range(len(mass)):
            if mass[j] == found_num:
                answer = str(j + 1)
                if better:
                    answer += ' (Улучшенный поиск)'
                    break
        print('Искомый элемент находится на позиции: ' + answer)


def sentinel_liner_search():  # Строжевой линейный поиск
    found_num, mass = MakeArray()
    if found_num != 'stop':
        answer = 'Not found'
        if mass[len(mass) - 1] == found_num:
            answer = str(len(mass))
        else:
            last = mass[len(mass) - 1]
            mass[len(mass) - 1] = found_num
            i = 0
            while True:
                if mass[i] == found_num:
                    break
                else:
                    i += 1
            if i + 1 != len(mass):
                answer = str(i + 1)
            mass[len(mass) - 1] = last
        print('Искомый элемент находится на позиции: ' + answer)


def get_recursive_leaner_search(array, i, found_item):
    if i == len(array):
        return "Not found"
    elif array[i] == found_item:
        return i + 1
    else:
        i += 1
        return get_recursive_leaner_search(array, i, found_item)


def do_recursive_leaner_search():
    found_item, mass = MakeArray()
    if found_item != 'stop':
        answer = get_recursive_leaner_search(mass, 0, found_item)
        print(f'Искомый элемент находится на позиции: {answer}')
