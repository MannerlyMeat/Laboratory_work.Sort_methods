import random
import numpy as np
import time
from datetime import datetime
import timeit


def shell_sort(arra):
    gap = len(arra) // 2

    while gap > 0:
        for i in range(gap, len(arra)):
            temp = arra[i]
            pos = i

            while pos >= gap and arra[pos - gap] > temp:
                arra[pos] = arra[pos - gap]
                pos -= gap
                arra[pos] = temp

        gap //= 2
    return arra


def quick_sort(arra):
    if len(arra) <= 1:
        return arra
    else:
        q = random.choice(arra)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in arra:
            if n < q:
                s_nums.append(n)
            elif n>q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)

#arra = [3,5,2,8,5,2,1,2,5,1,3,8,0,4,2,16,8,2,1,9]
size = input("Введите размер массива - ")
arra = np.random.randint(0,100, int(size))



print("Исходный массив", arra)


start_time = datetime.now()
result_quick_sort = quick_sort(arra)
print("Время сортировки quick sort",  datetime.now() - start_time)
start_time = datetime.now()
result_Shell_sort = shell_sort(arra)
print("Вермя сортировки методом Шелла",   datetime.now() - start_time)
start_time = datetime.now()
arra.sort()
print("Время сортировки встроенным методом",   datetime.now() - start_time)
input("Нажмите для продолжения...")

