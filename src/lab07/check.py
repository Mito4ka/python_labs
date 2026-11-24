import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials


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


if __name__ == "__main__":
    random.seed(42)
    total_check = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total_check += check_sorting(fn)
    total_check += check_search()
    total_check += check_two_sum()

    print(f"OK, всего проверок {total_check}")
