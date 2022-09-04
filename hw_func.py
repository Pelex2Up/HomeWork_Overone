# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

from colorama import Fore

print('Добро пожаловать в "Простейший калькулятор" v.3.0!')
print(Fore.RED + 'Чтобы узнать функционал калькулятора введите: help.' + Fore.RESET)


def calc(n1, at, n2):
    if at == '/' and n2 == 0:
        return 'Ошибка! Деление на ноль!'
    if at == '+':
        return n1 + n2
    elif at == '*':
        return n1 * n2
    elif at == '-':
        return n1 - n2
    else:
        return n1 / n2


while True:
    num1 = input('Введите первое число: ')
    if num1 == 'help':
        print(Fore.YELLOW + 'Список доступных операций (вводить в строку операций):\nСложение (+)\nВычитание (-)')
        print('Умножение (*)\nДеление (/)\nПринудительное завершение программы (0)' + Fore.RESET)
        continue
    attr = input('Введите операцию: ')
    if attr == '0':
        print('Работа программы прекращена принудительно.')
        break
    num2 = input('Введите второе число: ')
    print(f'Результат вычисления: {calc(int(num1), attr, int(num2))}')
    whattodo = input('Хотите продолжить? y/n: ')
    if 'y' in whattodo.lower():
        continue
    else:
        break



