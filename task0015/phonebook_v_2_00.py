import csv
import os

def load_contacts():
    if not os.path.exists('contacts.csv'):
        return []
    contacts = []
    with open('contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def save_contacts(contacts):
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def view_contacts(contacts):
    if len(contacts) == 0:
        print("Телефонный справочник пуст.")
    else:
        print("Контакты:")
        for contact in contacts:
            print(f"Имя: {contact[0]}, Телефон: {contact[1]}")

def add_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    contacts.append([name, phone])
    print("Контакт добавлен.")

def search_contact(contacts):
    keyword = input("Введите ключевое слово для поиска: ")
    results = []
    for contact in contacts:
        if keyword.lower() in contact[0].lower() or keyword.lower() in contact[1].lower():
            results.append(contact)
    if len(results) == 0:
        print("Контакты не найдены.")
    else:
        print("Результаты поиска:")
        for contact in results:
            print(f"Имя: {contact[0]}, Телефон: {contact[1]}")

def delete_contact(contacts):
    keyword = input("Введите имя или фамилию контакта для удаления: ")
    removed = False
    for contact in contacts:
        if keyword.lower() in contact[0].lower() or keyword.lower() in contact[1].lower():
            contacts.remove(contact)
            removed = True
            print("Контакт удален.")
    if not removed:
        print("Контакт не найден.")

def update_contact(contacts):
    keyword = input("Введите имя или фамилию контакта для изменения: ")
    updated = False
    for contact in contacts:
        if keyword.lower() in contact[0].lower() or keyword.lower() in contact[1].lower():
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый номер телефона: ")
            contact[0] = new_name
            contact[1] = new_phone
            updated = True
            print("Контакт обновлен.")
    if not updated:
        print("Контакт не найден.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nТелефонный справочник")
        print("1. Просмотр контактов")
        print("2. Добавление контакта")
        print("3. Поиск контакта")
        print("4. Удаление контакта")
        print("5. Изменение контакта")
        print("6. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            update_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == '__main__':
    main()