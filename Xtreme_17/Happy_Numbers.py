def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

def count_happy_numbers(a, b):
    return sum(is_happy(i) for i in range(a, b + 1))


a, b = map(int, input().split())
print(count_happy_numbers(a,b))