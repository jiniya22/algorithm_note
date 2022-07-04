# 반복문으로 구현한 factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀 함수로 구현한 factorial
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_iterative(6))  # 720
print(factorial_recursive(6))  # 720
