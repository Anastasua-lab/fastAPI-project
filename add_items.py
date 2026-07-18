import requests

BASE_URL = "http://127.0.0.1:8000"

items = [
    {"id": 1, "name": "Конструктор LEGO City", "description": "Набор из 500 деталей", "price": 4500.00, "tax": 450.00},
    {"id": 2, "name": "Кукла Barbie Dreamhouse", "description": "Кукла с аксессуарами", "price": 3200.00, "tax": 320.00},
    {"id": 3, "name": "Велосипед STELS 14 дюймов", "description": "Для детей от 4 лет", "price": 8500.00, "tax": 850.00},
    {"id": 4, "name": "Набор для рисования 150 предметов", "description": "Фломастеры, карандаши, краски", "price": 1200.00, "tax": 120.00},
    {"id": 5, "name": "Плюшевый мишка 50 см", "description": "Гипоаллергенный материал", "price": 1500.00, "tax": 150.00},
    {"id": 6, "name": "Монополия Детская", "description": "Экономическая игра от 6 лет", "price": 1800.00, "tax": 180.00},
    {"id": 7, "name": "Планшет Dexp для обучения", "description": "Обучающие игры", "price": 6200.00, "tax": 620.00},
    {"id": 8, "name": "Пазлы Мир динозавров", "description": "1000 деталей", "price": 900.00, "tax": 90.00},
    {"id": 9, "name": "Самокат Micro Mini", "description": "Трёхколёсный от 2 лет", "price": 4800.00, "tax": 480.00},
    {"id": 10, "name": "Набор Юный химик", "description": "20 безопасных опытов", "price": 2300.00, "tax": 230.00}
]

for item in items:
    response = requests.post(f"{BASE_URL}/items/", json=item)
    if response.status_code == 200:
        print(f" {item['name']} - добавлен!")
    else:
        print(f" {item['name']} - ошибка: {response.status_code}")

print("\n Все товары добавлены!")

