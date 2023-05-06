# Задача 1. Представлен список из значений
# "Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro".
# Необходимо создать новый список, содержащий модели бренда Apple.

mobiles = ["Xiaomi Redmi Note 10S", "Смартфон Xiaomi Redmi Note 10 Pro", "Apple iPhone 13", "Apple iPhone 11", "Huawei nova Y70", "Смартфон Apple iPhone 13 Pro"]
apple = [mobiles for mobiles in mobiles if "Apple" in mobiles]

print(apple)