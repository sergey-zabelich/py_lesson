import json
from datetime import datetime

notes = []

def load_notes():
    global notes
    try:
        with open('notes.json', 'r') as file:
            try:
                notes = json.load(file)
            except json.JSONDecodeError:
                notes = []
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def add_note():
    id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        "id": id,
        "title": title,
        "body": body,
        "timestamp": f"{datetime.now().strftime('%d.%m.%Y')} / {datetime.now().strftime('%H:%M:%S')}"
    }
    notes.append(note)
    save_notes()
    print("Заметка добавлена!")

def edit_note():
    if not notes:
        print("Список заметок пуст, создайте хотя бы одну заметку.")
        return

    id = int(input("Введите ID заметки, которую хотите отредактировать: "))
    note = next((note for note in notes if note["id"] == id), None)
    if note:
        print(f"Изменение заметки с ID {id}:")
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новый текст заметки: ")
        note["title"] = title
        note["body"] = body
        note["timestamp"] = f"{datetime.now().strftime('%d.%m.%Y')} / {datetime.now().strftime('%H:%M:%S')}"
        save_notes()
        print("Заметка отредактирована!")
    else:
        print(f"Заметка с ID {id} не найдена!")

def delete_note():
    if not notes:
        print("Список заметок пуст, создайте хотя бы одну заметку.")
        return

    id = int(input("Введите ID заметки, которую хотите удалить: "))
    note = next((note for note in notes if note["id"] == id), None)
    if note:
        notes.remove(note)
        save_notes()
        print("Заметка удалена!")
    else:
        print(f"Заметка с ID {id} не найдена!")

def list_notes():
    if not notes:
        print("Список заметок пуст, создайте хотя бы одну заметку.")
        return

    for note in sorted(notes, key=lambda x: x["timestamp"]):
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата/время создания или последнего изменения: {note['timestamp']}")
        print()

load_notes()

while True:
    print("========================")
    print("Меню:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Показать список заметок")
    print("0. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        list_notes()
    elif choice == "0":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

print("Спасибо за использование программы!")