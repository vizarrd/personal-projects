def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage:
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for num in fibonacci_generator(n):
    print(num)
