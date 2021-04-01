def bubble_sort(n, array):
    x = True
    for i in range(n - 1):
        swap = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                swap = True
                x = False
        if swap:
            print(*array)
    if x:
        print(*array)


if __name__ == '__main__':
    with open(file='input.txt', mode='r') as fl:
        num = int(fl.readline())
        mas = list(int(i) for i in fl.readline().split())

bubble_sort(num, mas)


"""

Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша продолжил изучать разные сортировки. На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком

Её алгоритм следующий (сортируем по неубыванию):

    На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов. Если элемент на позиции i больше элемента на позиции i + 1, меняем их местами. После первой итерации самый большой элемент всплывёт в конце массива.
    Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной итерации не окажется, что обмены больше не нужны, то есть массив уже отсортирован.
    После не более чем n – 1 итераций выполнение алгоритма заканчивается, так как на каждой итерации хотя бы один элемент оказывается на правильной позиции.


Помогите Гоше написать код алгоритма.

Формат ввода

В первой строке на вход подаётся натуральное число n — длина массива, 2 ≤ n ≤ 1000.
Во второй строке через пробел записано n целых чисел.
Каждое из чисел по модулю не превосходит 1000.

Обратите внимание, что считывать нужно только 2 строки: значение n и входной массив.
Формат вывода

После каждого прохода по массиву, на котором какие-то элементы меняются местами, выводите его промежуточное состояние.
Таким образом, если сортировка завершена за k меняющих массив итераций, то надо вывести k строк по n чисел в каждой — элементы массива после каждой из итераций.

Если массив был изначально отсортирован, то просто выведите его.
Пример 1
Ввод
Вывод

5
4 3 9 2 1

	

3 4 2 1 9
3 2 1 4 9
2 1 3 4 9
1 2 3 4 9

Пример 2
Ввод
Вывод

5
12 8 9 10 11

	

8 9 10 11 12
"""