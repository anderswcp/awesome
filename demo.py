def func(n):
    if n < 0:
        return -1

    elif n == 1 or n == 2:
        return 1

    else:
        return func(n-1) + func(n-2)

result = func(20)
if result != -1:
    print(result)