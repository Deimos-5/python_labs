import time
import random
import csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

def measure_time(func, *args):
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start

def bench_sorting():
    sizes = [1000, 10000, 100000]
    algorithms = {"bubble": bubble_sort,"insertion": insertion_sort,"selection": selection_sort,"sorted": sorted}
    results = []
    for n in sizes:
        nums = [random.randint(-10000, 10000) for _ in range(n)]
        for name, func in algorithms.items():
            if n == 100000 and name != "sorted":
                results.append((name, n, ">60"))
                continue    
            t = measure_time(func, nums)
            results.append((name, n, round(t, 6)))
    return results

def bench_search():
    n = 100000
    nums = [random.randint(-100000, 100000) for _ in range(n)]
    targets = [random.randint(-100000, 100000) for _ in range(10000)]
    results = []

    start = time.perf_counter()
    for x in targets:
        linear_search(nums, x)
    linear_time = time.perf_counter() - start
    results.append(("linear_search", n, round(linear_time, 6)))

    start = time.perf_counter()
    sorted_nums = sorted(nums)
    sort_time = time.perf_counter() - start
    results.append(("sorted_for_binary", n, round(sort_time, 6)))
    
    start = time.perf_counter()
    for x in targets:
        binary_search(sorted_nums, x)
    binary_time = time.perf_counter() - start
    results.append(("binary_search", n, round(binary_time, 6)))
    
    return results

def bench_two_sum():
    sizes = [1000, 10000]
    results = []
    for n in sizes:
        nums = [random.randint(-10000, 10000) for _ in range(n)]
        i, j = random.sample(range(n), 2)
        target = nums[i] + nums[j]
        t_brute = measure_time(two_sum_brute, nums, target)
        t_fast = measure_time(two_sum_fast, nums, target)
        results.append(("two_sum_brute", n, round(t_brute, 6)))
        results.append(("two_sum_fast", n, round(t_fast, 6)))  
    return results

def main():
    all_results = []
    
    sort_results = bench_sorting()
    for name, n, t in sort_results:
        all_results.append(("sorting", n, name, t))
        
    search_results = bench_search()
    for name, n, t in search_results:
        all_results.append(("search", n, name, t))
        
    two_sum_results = bench_two_sum()
    for name, n, t in two_sum_results:
        all_results.append(("two_sum", n, name, t))

    with open("src/lab07/bench.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["task", "n", "impl", "seconds"])
        for row in all_results:
            writer.writerow(row)
            
if __name__ == "__main__":
    main()