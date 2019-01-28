def calc(s, x, y):

    operations = ('+', '-', '/', '*')
    z = 0

    try:
        assert s in operations
        print('Операция "{}" в списке есть.'.format(s))
    except AssertionError:
        print('Внимание!!! Неверный знак операции!!')

    try:
        x = int(x)
        y = int(y)
        if s == '+':
            z = x+y
        elif s == '-':
            z = x-y
        elif s == '*':
            z = x*y
        elif s == '/':
            z = x/y
        print("Результат:", z)
    except ZeroDivisionError:
            print('Внимание!!! Деление на ноль!')
    except ValueError:
        print('Внимание!!! Ошибка в типе значения')

calc(input('Введите Знак операции (+,-,*,/):'), input('Введите x= '), input('Введите y= '))