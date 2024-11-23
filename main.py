import json
import uuid
from typing import Any


def add_new_book():
    """Добавление новой книги"""
    with open('db.json', 'r') as json_file:
        data: list[dict[str, Any]] = json.load(json_file)

    new_title = input("Название книги: ")
    new_author = input("Автор книги: ")
    new_year = input("Дата издания: ")

    new_book = {
        "id": str(uuid.uuid4()),
        "title": new_title,
        "author": new_author,
        "year": new_year,
        "status": "в наличии",
    }

    data.append(new_book)

    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(
        f"Книга с названием {new_title}, автором которой является {new_author}, написанная в {new_year} году, добавлена.")


def delete_book():
    """Удаление книги"""
    with open('db.json', 'r') as json_file:
        data: list[dict[str, Any]] = json.load(json_file)

    book_id = input('Введите идентификатор книги: ')
    book = list(filter(lambda b: b['id'] == book_id, data))

    if not book:
        print("Книги с таким идентификатором нет.")
        return

    book = book[0]

    data.remove(book)

    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Книга {book_id} удалена.")


def search_book():
    """Поиск книги"""
    with open('db.json', 'r') as json_file:
        data: list[dict[str, Any]] = json.load(json_file)

    book = input("Введите название автора или год издания, чтобы найти книгу: ")
    search = list(filter(lambda b: b['title'] == book or b['author'] == book or b['year'] == book, data))

    if not search:
        print("Ни одного совпадения не найдено.")
        return

    for book in search:
        print(
            f"Идентификатор: {book['id']}, "
            f"\nНазвание: {book['title']}, "
            f"\nАвтор: {book['author']}, "
            f"\nГод издания: {book['year']}, "
            f"\nСтатус: {book['status']}."
        )

    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


def all_books():
    """Отображение всех книг"""
    with open('db.json', 'r') as json_file:
        data: list[dict[str, Any]] = json.load(json_file)

    print(f"{'ID':<45} {'Название':<30} {'Автор':<20} {'Год издания':<20} {'Статус':<15}")

    if not data:
        print("Нет книг.")
        return

    for book in data:
        print(f"{book['id']:<45} {book['title']:<30} {book['author']:<20} {book['year']:<20} {book['status']:<15}")

    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


def update_status():
    """Изменение статуса книги"""
    with open('db.json', 'r') as json_file:
        data: list[dict[str, Any]] = json.load(json_file)

    book_id = input('Введите идентификатор книги: ')

    book = list(filter(lambda b: b['id'] == book_id, data))
    if not book:
        print("Книги с таким идентификатором нет.")
        return

    book = book[0]
    book_status = input('Введите статус книги "в наличии" или "выдана": ')
    book['status'] = book_status

    with open('db.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Статус книги изменен на: {book_status}.")


while True:
    try:
        number = int(input(
            """
Введите цифру, чтобы выполнить одно из действий:
1. Добавить книгу.
2. Удалить книгу.
3. Найти книгу.
4. Вывести список всех книг.
5. Изменить статус книги.
0. Выйти из программы.

"""
        ))
    except ValueError:
        continue

    if number == 1:
        add_new_book()
    elif number == 2:
        delete_book()
    elif number == 3:
        search_book()
    elif number == 4:
        all_books()
    elif number == 5:
        update_status()
    elif number == 0:
        break
    else:
        print("Такого варианта нет.")
