from __future__ import annotations


def hello() -> None:
    name = "Developer"
    print(f"Hello, {name}! Welcome to learnpy.")


def collections_demo() -> None:
    nums = [1, 2, 3, 4]
    squares = [n * n for n in nums]
    uniq = {n % 3 for n in nums}
    counts = {n: nums.count(n) for n in nums}

    print("nums:", nums)
    print("squares:", squares)
    print("uniq mod 3:", uniq)
    print("counts:", counts)
