# Найпростіший генератор

def simple_generator():
    yield 'Test'
    yield 'Hello'
    yield 'world'


for item in simple_generator():
    print(item)