# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from timeit import timeit
from itertools import islice
from itertools import count


def task1():
    # используем традиционный итератор FOR, время выполнения 0.05
    for i in islice(count(1), 15):
        print(i)
task1()
print(timeit("task1()", globals=globals(), number=1000))



# Используем LC, время выполнения 1.47
nums = [n for n in range(1, 16)]
print(nums)
print(timeit("nums", globals=globals(), number=1000))