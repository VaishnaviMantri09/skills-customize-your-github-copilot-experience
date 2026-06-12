"""Starter code for Search & Sort Challenges

Implements basic search and sort functions and a simple benchmarking helper.
"""
from __future__ import annotations
from time import perf_counter
from typing import List, Any


def linear_search(arr: List[Any], target: Any) -> int:
    """Return index of target in arr or -1 if not found. O(n) time."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr: List[Any], target: Any) -> int:
    """Assumes arr is sorted. Return index of target or -1. O(log n) time."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(arr: List[Any]) -> List[Any]:
    """Return a new list sorted using bubble sort. O(n^2) time."""
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def merge_sort(arr: List[Any]) -> List[Any]:
    """Return a new list sorted using merge sort. O(n log n) time."""
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    out: List[Any] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def run_benchmarks():
    import random

    sizes = [100, 1000, 5000]
    for n in sizes:
        arr = [random.randint(0, n) for _ in range(n)]
        target = arr[n // 2]

        # Measure linear search
        t0 = perf_counter()
        linear_search(arr, target)
        t1 = perf_counter()

        # For binary search, sort first
        sorted_arr = merge_sort(arr)
        t2 = perf_counter()
        binary_search(sorted_arr, target)
        t3 = perf_counter()

        print(f"n={n}: linear={(t1-t0):.6f}s, sort={(t2-t1):.6f}s, binary={(t3-t2):.6f}s")


if __name__ == "__main__":
    print("This is starter code for the Search & Sort assignment. Import functions in your solution.")
