'''
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("Список пуст") #Если список пустой — склад исключение в ValueError, потому что искать минимум/максимум не в чем.
    mini = nums[0]
    maxi = nums[0]
    for i in nums:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    return (mini, maxi)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = list(set(nums))
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
'''
def flatten(mat: list[list | tuple]) -> list:
    ans = []
    for i in mat:
        if type(i) == list or type(i) == tuple:
            ans += i
        else:
            raise ValueError("Строка вместо ряда")
    return ans
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]] ))
print(flatten([[1, 2], "ab"]))