

class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start >= end:
            raise ValueError('start всегда меньше значения атрибута end')
        self.start = start if start % 2 == 0 else start +1
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end - 1:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

en = EvenNumbers(10, 25)
for i in en:
    print(i)