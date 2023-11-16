# Filter
payment = [100, -3, 400, 35, -100]

def is_negative_number(num) -> bool:
    if num < 0:
        return True
    return False

result = filter(is_negative_number, payment)
print(list(result))


def is_positive_number(num):
    if num > 0:
        return True
    return False

result = filter(is_positive_number, payment)
print(list(result))

result = list(filter(lambda num: num > 0, payment))
print(result)

result = list(filter(lambda num: num < 0, payment))
print(result)
