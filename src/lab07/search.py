def linear_search(nums, x):
     """Индекс первого вхождения x в списке nums или -1, если элемента нет."""
    for i, val in enumerate(nums):
        if val == x:
            return i
    return -1

def   binary_search(sorted_nums, x) : #мы не идём по всем элементам подряд, а «прыгаем» по серединам отрезков
     """Индекс любого вхождения x в отсортированном списке или -1.
    
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while  lo <= hi: #пока границы не пересеклись, ищем мндекс сер текущ отрезка
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x: # значит, нужное число правее середины. Сдвигаем левую границу
             lo = mid + 1
        else:
              hi = mid - 1
    return -1 # гр пересек


def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def  two_sum_fast(nums, target):
    seen = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in seen:
            return (seen[need], j)
        seen[x] = j
    return None

    if __name__=="__main__":
    print(linear_search([4, 2, 7, 2], 2))
    print(linear_search([4, 2, 7, 2], 9))
    print(linear_search([], 1))

    print(binary_search([1, 3, 5, 7], 5))
    print(binary_search([1, 3, 5, 7], 4))
    print(binary_search([5], 5))
    print(binary_search([], 5))

    print(two_sum_brute([2, 7, 11, 15], 9))
    print(two_sum_brute([1, 2], 10))
    
    print(two_sum_fast([2, 7, 11, 15], 9))
    print(two_sum_fast([1, 2], 10))