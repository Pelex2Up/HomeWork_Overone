# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

def some_func(args):
    if type(args) == list:
        count_alpha = 0
        count_num = 0
        for i in args:
            if str(i).isdigit():
                count_num += 1
            else:
                for alpha in i:
                    if alpha.isalpha():
                        count_alpha += 1
                    else:
                        continue
        print(f'That list has {count_alpha} letter(s) and {count_num} number(s)')
    elif type(args) == tuple:
        count_len = 0
        for i in args:
            if type(i) == str:
                count_len += len(i)
            else:
                continue
        print(f'Length of all words of that tuple is {count_len}')
    elif type(args) == int:
        count_nums = 0
        for i in str(args):
            if int(i) % 2 != 0:
                count_nums += 1
            else:
                continue
        print(f'Count of odd numbers in that number is {count_nums}')
    elif type(args) == str:
        len_str = 0
        for i in args:
            if i != ' ':
                len_str += len(i)
            else:
                continue
        print(f'Count of letters in that string is {len_str}')


some_func('super sam')