from random import *
import json

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Коллекция фильмов успешно сохранена в файле films.json ")

def load():
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("фильмотека успешно загружена! ")

try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("фильмотека успешно загружена! ")
except:

    films.append("Хакер")
    films.append("Кибер")
    films.append("Кто Я")
    films.append("Сноуден")
    films.append("Пароль Рыба-меч")
    films.append("Хакеры")
    films.append("Военные игры")
    films.append("Сеть")
    films.append("Взлом")
    films.append("Пятая власть")
    films.append("Хакерские войны")
    films.append("Цикада 3301")
    films.append("Искуственный интеллект")

while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот остановлен, заходите еще!")
        break
    elif command == "/show all":
        print("Вот общий список фильмов: ")
        print(films)
    elif command == "/help":
        print("Вот полный список комманд:")
        print("/help - Показывает список комманд")
        print("/start - Запуск Бота-фильмотеки")
        print("/stop - Остановка Бота-фильмотеки")
        print("/show all - Показать весь список фильмов")
        print("/add - Добавить фильм в фильмотеку")
        print("/delete - Удалить фильм из фильмотеки")
        print("/save - Сохраняет созданную коллекцию")
        print("/load - Загружает сохранённую коллекцию")
    elif command == "/add":
        add_film = input("Введите название фильма, который хотите добавить ")
        films.append(add_film)
        print("Фильм успешно добавлен в коллекцию! ")
    elif command == "/delete":
        delete_film = input("Введите название фильма, который хотите удалить ")
        '''
        if delete_film in films:
            films.remove(delete_film)
            print("Фильм успешно удалён из коллекции! ")
        else:
            print("Этого фильма нет в коллекции! ")
        '''
        try:
            films.remove(delete_film)
            print("Фильм успешно удалён из коллекции! ")
        except:
            print("Этого фильма нет в коллекции! ")
    elif command == "/random":
        # rnd = randint(0, len(films)-1)
        # print("Случайный выбор пал на - " + films[rnd])
        print("Случайный выбор пал на - " + choice(films))
    elif command == "/save":
        save()
        # print("Сохранение прошло успешно! ")
    elif command == "/load":
        load()
    else:
        print("неопозннанная коммманда - изучите мануал через /help")