def fibonacci(n):
    """This function returns the first n Fibonacci numbers."""

    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(100))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]