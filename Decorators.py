def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")
        print(result)

    def is_prime_number(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            return True
        else:
            return False

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
