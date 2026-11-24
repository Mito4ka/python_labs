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


if __name__ == "__main__":
    print(bubble_sort([3, 1, 2]))
    print(bubble_sort([2, 2, 1]))
    print(bubble_sort([]))

    print(insertion_sort([3, 1, 2]))
    print(insertion_sort([2, 2, 1]))
    print(insertion_sort([]))

    print(selection_sort([3, 1, 2]))
    print(selection_sort([2, 2, 1]))
    print(selection_sort([]))
