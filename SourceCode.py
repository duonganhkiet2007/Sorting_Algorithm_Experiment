import sys
import time
import numpy as np

# Tăng giới hạn đệ quy để không bị lỗi khi chạy 1 triệu phần tử
sys.setrecursionlimit(2000000)

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot: i += 1
        j -= 1
        while arr[j] > pivot: j -= 1
        if i >= j: return j
        arr[i], arr[j] = arr[j], arr[i]

def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[i] < arr[l]: largest = l
    if r < n and arr[largest] < arr[r]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i];
                i += 1
            else:
                arr[k] = R[j];
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i];
            i += 1;
            k += 1
        while j < len(R):
            arr[k] = R[j];
            j += 1;
            k += 1

def numpy_sort(arr):
    np_arr = np.array(arr)
    return np.sort(np_arr)

def load_data_from_inp(filename):
    try:
        with open(filename, 'r') as f:
            # Đọc toàn bộ file, tách từ và chuyển sang float
            return list(map(float, f.read().split()))
    except FileNotFoundError:
        return None


def run_tests():
    filenames = [f"TEST{i}.INP" for i in range(1, 11)]
    algorithms = [
        ("QuickSort", lambda a: quick_sort(a,0, len(a) - 1)),
        ("HeapSort", heap_sort),
        ("MergeSort", merge_sort),
        ("NumpySort", numpy_sort)
    ]

    # In tiêu đề bảng kết quả
    print(f"{'File':<12} | {'Thuật toán':<12} | {'Thời gian (s)'}")
    print("-" * 45)

    for fname in filenames:
        # Nạp dữ liệu gốc từ file
        raw_data = load_data_from_inp(fname)

        if raw_data is None:
            print(f"{fname:<12} | Lỗi: Không thấy file")
            continue

        for algo_name, algo_func in algorithms:
            data_test = list(raw_data)
            # Đo thời gian
            start = time.perf_counter()
            algo_func(data_test)
            end = time.perf_counter()
            print(f"{fname:<12} | {algo_name:<12} | {end - start:>12.5f}")
        print("-" * 45)


if __name__ == "__main__":
    run_tests()


