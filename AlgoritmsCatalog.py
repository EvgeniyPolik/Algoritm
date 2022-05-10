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
