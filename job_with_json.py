import json
import os

filename = 'db.json'


def write_to_json(data: json):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def read_from_json() -> list:
    # проверяем существует ли файл, если есть пишем данные иначе вернем пустой список
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def get_id(data: list) -> int:
    # если список не пустой ищем максимальный id иначе вернем 1
    if data:
        return max(book['id'] for book in data) + 1
    return 1
