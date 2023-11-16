# Map
names = ["dan", "jane", "steve", "mike"]   # Потрібно щоб кожне ім'я було з великої літери

# 1
def normalize(name):
    return name.title()

new_name = []
for name in names:
    new_name.append(name.title())
print(new_name)

new_name_map = map(normalize, names)
print(new_name_map)
print(list(new_name_map))

# 2
new_name_map = map(str.title, names)
print(list(new_name_map))

# 3
# new_name_map = map(lambda name: name.title(), names)
new_name_map = list(map(lambda name: name.title(), names))
print(new_name_map)

# 4
new_name_map = [name.title() for name in names]
print(new_name_map)