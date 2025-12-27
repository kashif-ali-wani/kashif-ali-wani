def fibonacci_series(n):
    """Generate Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    series = [0, 1]
    for i in range(2, n):
        next_value = series[-1] + series[-2]
        series.append(next_value)

    return series

# Example usage:
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_series(num_terms)
print(f"Fibonacci series with {num_terms} terms: {result}")
