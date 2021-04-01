def sort_str(a, b):
    check_a = int(a + b)
    check_b = int(b + a)
    if check_a > check_b:
        return a
    else:
        return b


def number(mas):
    n = len(mas)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sort_str(mas[j], mas[j + 1]) == mas[j]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
    return ''.join(mas[::-1])


if __name__ == '__main__':
    with open(file='input.txt', mode='r') as fl:
        num = fl.readline()
        lst = fl.readline().split()

print(number(lst))



"""

Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.
Формат ввода

В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
Формат вывода

Нужно вывести самое большое число, которое можно составить из данных чисел.
Пример 1
Ввод
Вывод

3
15 56 2

	

56215

Пример 2
Ввод
Вывод

3
1 783 2

	

78321

Пример 3
Ввод
Вывод

5
2 4 5 2 10

	

542210

"""