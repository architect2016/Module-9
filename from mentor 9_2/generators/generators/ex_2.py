# Самостійний виклик через next

def simple_generator():
    yield 'Test'
    yield 'Hello'
    yield 'world'


gen = simple_generator()
print(gen)

r_next = next(gen)
print(r_next)
r_next = next(gen)
print(r_next)
r_next = next(gen)
print(r_next)
r_next = next(gen)
print(r_next)