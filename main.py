
# from models import Book
from job_with_json import read_from_json, get_id, write_to_json
import unittest
from pprint import pprint
from test import TestGetId


def add_book():
    select = str(input('хотите добавить? Y/N: ')).upper()
    # читаем данные из файла
    data = read_from_json()
    status = 'в наличии'
    while select == 'Y':
        # вводим данные
        author = str(input('Введите автора: '))
        title = str(input('Введите название: '))
        year = int(input('Введите год: '))
        # получаем max id из списка(json)
        id = get_id(data)
        # дополняем список словарем
        data.append({
            'author': author,
            'title': title,
            'year': year,
            'status': status,
            'id':  id
        })
        select = str(input('добавить еще? Y/N: ')).upper()
    # пишем данные обратно в файл
    write_to_json(data)


def del_book():
    while True:
        id = input('введи id для удаления/N чтобы пропустить: ')
        if id.isdigit():
            break
        else:
            if id.upper() == 'N':
                return None
            print('введи число или N')

    data = read_from_json()
    # получаем все книги с id неравным нашему
    books = [obj for obj in data if obj.get('id') != id]
    # если длина изменилась пишем новые данные
    if len(data) != len(books):
        write_to_json(books)
    else:
        print('нет книги с таким id ')


def search_book():
    answ = str(input('ищем? Y/N '))
    while answ.upper() == 'Y':
        author = str(input('Введите автора: '))
        title = str(input('Введите название: '))
        year = input('Введите год: ')
        year = int(year) if year.isdigit() else None
        # получаем все книги и фильтруем список
        books = read_from_json()
        if author:
            books = [obj for obj in books if obj.get('author') == author]
        if title:
            books = [obj for obj in books if obj.get('title') == title]
        if year:
            books = [obj for obj in books if obj.get('year') == year]
        pprint(books)
        answ = str(input('ищем еще? Y/N '))


def all_books():
    books = read_from_json()
    print('все книжки: ')
    for book in books:
        pprint(book)


def change_book_status():
    while True:
        id = input('введи id для удаления/N чтобы пропустить: ')
        if id.isdigit():
            id = int(id)
            break
        else:
            if id.upper() == 'N':
                return None
            print('введи число или N')
    # получаем все книжки, флаг поиска в false
    data = read_from_json()
    flag_book = False
    # проходим по списку и ищем книгу с нашим id, меняем флаг поиска
    for book in data:
        if book.get('id') == id:
            flag_book = True
            status = input('введите статус:"1. в наличии"/"2. выдана": ')
            # проверям кореектность и меняем статус найденной книги
            if status.isdigit() and int(status) in [1, 2]:
                match int(status):
                    case 1:
                        book['status'] = 'в наличии'
                    case 2:
                        book['status'] = 'выдана'
                write_to_json(data)
            print(f'статус книги с {id} изменен')
    if not flag_book:
        print('книга не найдена')


if __name__ == '__main__':
    unittest.main(exit=False)
    while True:
        print('1) добавить книги')
        if read_from_json():
            print('2) удалить книги')
            print('3) найти книги')
            print('4) все книги')
            print('5) сменить статус книги')
        print('выход exit')
        my_select = input('выберите действие: ')
        if my_select.isdigit() and int(my_select) in [1, 2, 3, 4, 5]:
            match int(my_select):
                case 1:
                    add_book()
                case 2:
                    del_book()
                case 3:
                    search_book()
                case 4:
                    all_books()
                case 5:
                    change_book_status()

        if my_select == 'exit':
            break
