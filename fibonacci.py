fibonacci_cache = {1:1, 2:1}

def fibonacci(n):
    # If we have cached the calue, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    value = fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

def __name__ == '__main__':
    for n in range(1, 101):
        print(n, ":", fibonacci(n))
    