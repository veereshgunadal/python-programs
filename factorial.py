def factorial(n):
    fact = 1
    if n == 0:
        return fact
    while n > 0:
        fact = fact * n 
        n = n - 1
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

def unit_test():
    assert factorial(0) == 1, "test failed"
    assert factorial(1) == 1, "test failed"
    assert factorial(5) == 120, "test failed"

    assert factorial_recursive(0) == 1, "test failed"
    assert factorial_recursive(1) == 1, "test failed"
    assert factorial_recursive(5) == 120, "test failed"
    print(" all cases are passed for factorial ")

if __name__ == "__main__":
    unit_test()