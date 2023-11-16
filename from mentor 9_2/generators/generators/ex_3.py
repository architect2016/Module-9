# Свій генератор range
def my_range(limit):
    value = 0
    while value < limit:
        yield value
        value += 1

gen = my_range(5)
# for number in my_range(5):
#     print(number)

while True:
    try:
        r = next(gen)
        print(r)
    except StopIteration:
        break
