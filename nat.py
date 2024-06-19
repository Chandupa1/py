def sum_of_first_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Example usage:
n = 10
result = sum_of_first_n(n)
print(f"The sum of the first {n} natural numbers is: {result}")
