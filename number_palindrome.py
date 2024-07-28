def reverse(n):
    rev = 0
    while n > 0:
        rem = n % 10
        n = n //10
        rev = rev*10 + rem
    return rev

num = 121
rev = reverse(num)
if rev == num:
    print(True)
else:
    print(False)