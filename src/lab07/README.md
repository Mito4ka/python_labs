# ЛР7 — Поиск, сортировка и измерение времени
# Задание A: Поиск
Модуль src/lab07/search.py
Функции linear_search, binary_search, two_sum_brute, two_sum_fast

# linear_search
Проходит список и сравнивает элемент с числом, которое нужно найти.

Возвращает индекс первого вхождения или -1 (если элемента нет).

Сложность: О(n) (один раз проходит список).

``` python
def linear_search(nums, x):
    """Индекс первого вхождения x в списке nums или -1, если элемента нет."""
    for i in range(len(nums)):
        if x == nums[i]:
            return i
    return -1
``` 

# binary_search
Ищет число в отсортированном списке, задает верхнюю и нижнюю границы, сравнивая середину текущей области с искомым числом, затем уменьшает область, пока середина не совпадет с числом, которое ищем.

Возвращает индекс числа или -1 (если элемента нет).

Сложность: О(log n) (на каждом шаге цикла область поиска уменьшается примерно вдвое).

``` python
def   binary_search(sorted_nums, x) : #мы не идём по всем элементам подряд, а «прыгаем» по серединам отрезков
    """Индекс любого вхождения x в отсортированном списке или -1.
    
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while  lo <= hi: 
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x: 
            lo = mid + 1
        else:
            hi = mid - 1
    return -1 
``` 
# two_sum_brute
Для каждого элемента списка ищет среди оставшихся такой элемент, который в сумме будет давать target.

Возвращает кортеж из пары индексов или None (если подходящих элементов нет).

Сложность: О(n^2) (цикл в цикле).

``` python
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

``` 

# two_sum_fast
Для каждого элемента списка ищет, сколько не хватает до target, и проверят, есть ли такое число в уже просмотренной части списка (словарь seen, в котором хранится число и его индекс).

Возвращает кортеж из пары индексов или None (если подходящих элементов нет).

Сложность: О(n) (один проход цикла).

``` python
def  two_sum_fast(nums, target):
    seen = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], j)
        seen[x] = j
    return None

``` 

# Задание B: Сортировки
Модуль src/lab07/sorting.py
Функции bubble_sort, insertion_sort, selection_sort
# bubble_sort
Сортировка "пузырьком": проходит по списку необходимое количество раз, меняя соседние элементы, если они стоят в неправильном порядке, пока весь список не будет стоять в порядке возрастания.

! ранний выход за счет флага swapped: на отсортированных данных он даёт один проход вместо n

Возвращает новый отсортированный список.

Сложность: О(n^2) (цикл в цикле) или О(n) (если список сразу отсортирован).

``` python
def bubble_sort(nums):
    nums = list(nums)
    n = len(nums)
    for i in range(n):
        p = False
        for j in range(n - 1 - i):  # идёт по индексам соседей
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                p = True
        if not p:  # Если за весь проход по списку не произошло ни одного обмена
            break
    return nums
``` 

# insertion_sort
Сортировка вставками: сдвигает элементы, которые больше текущего вправо, и вставляет в подходящее место.

Возвращает новый отсортированный список.

Сложность: О(n^2) (while в цикле) или О(n) (если список сразу отсортирован).

``` python
def insertion_sort(nums):
    nums = list(nums)
    n = len(nums)
    for i in range(1, n):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums
``` 

# selection_sort
Сортировка выбором: ищет минимальное число хвоста и вставляет его на границу отсортированной части.

Возвращает новый отсортированный список.

Сложность: О(n^2) (внутренний цикл всегда проходит весь остаток, независимо от данных).

``` python
def selection_sort(nums):
    nums = list(nums)
    for i in range(len(nums) - 1):
        min_ind = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        if min_ind != i:
            nums[i], nums[min_ind] = nums[min_ind], nums[i]
    return nums
``` 

# Задание C: Проверка против эталона
Модуль src/lab07/check.py
Функции check_sorting, check_search, check_two_sum
Необходимые импорты:

``` 
import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

``` 
# check_sorting
Проверяет функцию сортировки на случайных списках: результат должен совпадать с sorted(), а исходный список - не меняться. При несовпадении поднимается AssertionError с указанием проблемного входа.

``` python
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials
``` 
# check_search
Проверяет функции поиска на случайных списках: результат linear_search должен совпадать с nums.index(), а для binary_search элемент по индексу должен совпадать с x (могут быть повторы, поэтому важно просто наличие элемента). При несовпадении поднимается AssertionError с указанием проблемного входа.

``` python
def check_search(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        s_nums = sorted(nums)

        targets = nums + [-999, 999]

        for x in targets:
            res_lin = linear_search(nums, x)
            try:
                expected = nums.index(x)
            except ValueError:
                expected = -1
            assert res_lin == expected, f"linear_search ошибся на {nums}, x={x}: {res_lin} != {expected}"

            res_bin = binary_search(s_nums, x)
            if x in s_nums:
                assert 0 <= res_bin < len(s_nums) and s_nums[res_bin] == x, (
                    f"binary_search ошибся на {s_nums}, x={x}: вернул индекс {res_bin}"
                )
            else:
                assert res_bin == -1, f"binary_search ошибся на {s_nums}, x={x}: {res_bin} != -1"
    return trials
``` 

# check_two_sum
Проверяет функции поиска пары чисел на случайных списках: результат должен совпадать с эталоном. При несовпадении поднимается AssertionError с указанием проблемного входа.

``` python
def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 40)
        nums = [random.randint(-50, 50) for _ in range(n)]

        targets = [random.randint(-100, 100)]
        if n >= 2:
            i, j = random.sample(range(n), 2)
            targets.append(nums[i] + nums[j])

        for target in targets:
            res_brute = two_sum_brute(nums, target)
            res_fast = two_sum_fast(nums, target)

            if res_brute is None:
                assert res_fast is None, f"two_sum разошлись на {nums}, target={target}: brute=None, fast={res_fast}"
            else:
                assert res_fast is not None, f"two_sum разошлись на {nums}, target={target}: brute={res_brute}, fast=None"
                i1, j1 = res_brute
                i2, j2 = res_fast
                assert i1 < j1 and nums[i1] + nums[j1] == target, f"Неверный ответ brute: {res_brute}"
                assert i2 < j2 and nums[i2] + nums[j2] == target, f"Неверный ответ fast: {res_fast}"
    return trials
```

Запуск проверок
Прогоняет все проверки и печатает их суммарное число.

``` python
if __name__ == "__main__":
    random.seed(42)
    total_check = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total_check += check_sorting(fn)
    total_check += check_search()
    total_check += check_two_sum()

    print(f"OK, всего проверок {total_check}")
```
Запуск: python -m src.lab07.check 

Вывод в терминал:

![](../../images/lab06/фото1.png)

# Задание D: Бенчмарк
Модуль src/lab07/bench.py
Функции bench_sorts, bench_search, bench_2sum
Необходимые импорты:

``` python
``` 
# bench_sorts
Замеряет время sorted() и трёх написанных сортировок на списках размером 1_000, 10_000 и 100_000 элементов и возвращает результаты списком кортежей. Для 100_000 написанные сортировки не запускает (слишком долго) — пишет ">60".

``` python
``` 
# bench_search
Замеряет время функций на 10 000 запросах. Возвращает список кортежей.

``` python
```
# bench_2sum
Замеряет время функций на 1_000 и 10_000 запросах. Функции получают одни и те же данные. Возвращает список кортежей.

``` python
```
# main
Собирает результаты всех трёх бенчмарков, сохраняет их в CSV и печатает выровненную таблицу в консоль.

``` python
```


Запуск: python -m src.lab07.bench

Вывод в терминале:

![](../../images/lab06/фото2.png)

В CSV:

![](../../images/lab06/фото3.png)

Выводы
При росте объёма данных в 10 раз (с 1 000 до 10 000 элементов) время работы пузырьковой сортировки увеличилось в 114 раз (с 0.070 с до 8.030 с), что подтверждает её квадратичную сложность \(O(n^2)\). Встроенная функция sorted при том же увеличении данных замедлилась всего в 13.5 раз (с 0.000116 с до 0.001569 с), так как её сложность \(O(n \log n)\) растёт намного медленнее.
На неотсортированных списках бинарный поиск бесполезен, поскольку на каждом шаге отбрасывает не те половины массива и возвращает неверный результат. Предварительная сортировка за \(O(n \log n)\) невыгодна для одного поиска (быстрее пройтись линейным за \(O(n)\)), но полностью окупается на серии запросов: на 10 000 запросов по списку из 100 000 элементов бинарный поиск отработал за 0.033 с против 17.901 с у линейного. С помощью check.py (500 случайных проверок) удалось вовремя выявить и исправить ошибки с отступами и перепутанными переменными при замерах, после чего все функции прошли тесты без расхождений.