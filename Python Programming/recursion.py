def for_loop(n):
    if n < 0:
        return 0
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i

        return fact

print(for_loop(5))

def recu(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * recu(n - 1)

print(recu(5))