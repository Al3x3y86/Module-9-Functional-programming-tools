def all_variants(s):
    n = len(s)
    for i in range(1, 2**n):
        subset = ""
        for j in range(n):
            if (i >> j) % 2:
                subset += s[j]
        yield subset

# Пример использования
a = all_variants("abc")
for i in a:
    print(i)