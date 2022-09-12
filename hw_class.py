# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class SimpleClass:

    def __init__(self):
        self.glasn = ['a', 'e', 'u', 'i', 'o', 'y']
        self.empty_gl = []
        self.empty_sogl = []
        self.sum_chet = 0
        self.count_gl = 0
        self.count_sogl = 0

    @staticmethod
    def func2(arg):
        return int(len(arg))

    def func1(self, some_string):
        if not some_string.isdigit():
            for i in some_string:
                if i == ' ':
                    continue
                elif i not in self.empty_gl and i in self.glasn:
                    self.empty_gl.append(i)
                elif i not in self.empty_sogl and i not in self.glasn:
                    self.empty_sogl.append(i)
                else:
                    continue
            for x in self.empty_gl:
                self.count_gl += some_string.count(x)
            for y in self.empty_sogl:
                self.count_sogl += some_string.count(y)
            result = self.count_gl * self.count_sogl
            if result <= self.func2(some_string):
                return f'Гласные буквы в данной строке: {self.empty_gl}'
            else:
                return f'Согласные буквы в данной строке: {self.empty_sogl}'
        else:
            for i in some_string:
                if int(i) % 2 == 0:
                    self.sum_chet += int(i)
                else:
                    continue
            return f'Произведение суммы нечетных цифр на длину числа: {self.sum_chet * self.func2(some_string)}'


simple = SimpleClass()
inp_arg = input('Введите число либо строку: ')
print(simple.func1(inp_arg))
