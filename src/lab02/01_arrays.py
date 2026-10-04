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
#print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
