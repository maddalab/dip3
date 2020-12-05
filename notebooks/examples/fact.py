def fact(n: int) -> int:
    if (n < 0):
        raise ValueError("Cannot compute factorial of values less than 0: {n}")
    return 1 if (n == 0) else n * fact(n - 1)
