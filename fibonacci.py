def fibonacci(n):
    a = 0
    b = 1
    print(0)
    i = 1
    while i < n: 
        print(b)
        c = a+b
        a = b
        b = c
        i = i + 1

def fibonacci_recursive(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        fibonacci = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        return fibonacci

if __name__ == "__main__":
    print("1st element : ")
    fibonacci(1)
    print("2nd element : ")
    fibonacci(2)
    print("10 element : ")
    fibonacci(10)

    print("1st element : ",fibonacci_recursive(1))
    print("2nd element : ",fibonacci_recursive(2))
    print("10 element : ",fibonacci_recursive(10))