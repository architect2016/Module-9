"""
Генератор повернення, який повертає ціле число між min_val та max_val у нескінченному циклі
"""
from random import randint, seed


def cycle_random(min_val, max_val):
    seed()
    while True:
        yield randint(min_val, max_val)


rand_gen = cycle_random(5, 15)
result = []
for _ in range(100):
    result.append(next(rand_gen))

print(result)
