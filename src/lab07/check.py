import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0,50)
        nums = [random.randint(-100,100) for _ in range(n)]
        orig = nums.copy()
        res = fn(nums)
        exp = sorted(orig)
        assert res == exp, f'Ошибка в {fn.__name__} на данных {orig}'
        assert nums == orig, f'Функция {fn.__name__} изменила исходный список'
import random
from src.lab07.search import linear_search, binary_search

def check_search():
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        if nums:
            target = random.randint(-150, 150)
        try:
            expected_index = nums.index(target)
        except ValueError:
            expected_index = -1
        result_linear = linear_search(nums, target)
        assert result_linear == expected_index, (f"Ошибка linear_search! Список: {nums}, target: {target}. Ожидалось: {expected_index}, получено: {result_linear}")
        sorted_nums = sorted(nums)
        try:
            expected_sorted_index = sorted_nums.index(target)
        except ValueError:
            expected_sorted_index = -1
        result_binary = binary_search(sorted_nums, target)
        assert result_binary == expected_sorted_index, (f"Ошибка binary_search! Список: {sorted_nums}, target: {target}. Ожидалось: {expected_sorted_index}, получено: {result_binary}")

def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        if nums and random.random() < 0.5:
            i, j = random.sample(range(n), 2) if n >= 2 else (0, 0)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-200, 200)
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        if res_brute is None:
            assert res_fast is None, (f"Ошибка: two_sum_brute вернул None, а two_sum_fast вернул {res_fast}. Список: {nums}, target: {target}")
        else:
            assert res_fast is not None, (f"Ошибка: two_sum_brute нашел пару {res_brute}, а two_sum_fast вернул None. Список: {nums}, target: {target}")
            idx1, idx2 = res_brute
            assert nums[idx1] + nums[idx2] == target, (f"Ошибка: two_sum_brute вернул неверные индексы {res_brute}. Сумма элементов по этим индексам не равна {target}. Список: {nums}") 
            idx1, idx2 = res_fast
            assert nums[idx1] + nums[idx2] == target, (f"Ошибка: two_sum_fast вернул неверные индексы {res_fast}. Сумма элементов по этим индексам не равна {target}. Список: {nums}")

if __name__=="__main__":
    print('Проверка сортировок...')
    check_sorting(bubble_sort)
    check_sorting(insertion_sort)
    check_sorting(selection_sort)
    print('Проверка поиска...')
    check_search()
    print('Проверка Two Sum...')
    check_two_sum()
    print('OK')