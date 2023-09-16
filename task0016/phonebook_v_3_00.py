import csv
import tkinter as tk
from tkinter import messagebox
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

def view_contacts():
    contacts = load_contacts()
    if len(contacts) == 0:
        messagebox.showinfo("Телефонный справочник", "Телефонный справочник пуст.")
    else:
        contact_list = ""
        for contact in contacts:
            contact_list += f"Имя: {contact[0]}, Телефон: {contact[1]}\n"
        messagebox.showinfo("Телефонный справочник", contact_list)

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        contacts = load_contacts()
        contacts.append([name, phone])
        save_contacts(contacts)
        messagebox.showinfo("Телефонный справочник", "Контакт добавлен.")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("Телефонный справочник", "Введите имя и номер телефона.")

def search_contact():
    keyword = entry_search.get()
    if keyword:
        contacts = load_contacts()
        results = []
        for contact in contacts:
            if keyword.lower() in contact[0].lower() or keyword.lower() in contact[1].lower():
                results.append(contact)
        if len(results) == 0:
            messagebox.showinfo("Телефонный справочник", "Контакты не найдены.")
        else:
            contact_list = ""
            for contact in results:
                contact_list += f"Имя: {contact[0]}, Телефон: {contact[1]}\n"
            messagebox.showinfo("Телефонный справочник", contact_list)
    else:
        messagebox.showwarning("Телефонный справочник", "Введите ключевое слово для поиска.")

def delete_contact():
    keyword = entry_delete.get()
    if keyword:
        contacts = load_contacts()
        removed = False
        for contact in contacts:
            if keyword.lower() in contact[0].lower() or keyword.lower() in contact[1].lower():
                contacts.remove(contact)
                removed = True
        if removed:
            save_contacts(contacts)
            messagebox.showinfo("Телефонный справочник", "Контакт удален.")
        else:
            messagebox.showinfo("Телефонный справочник", "Контакт не найден.")
    else:
        messagebox.showwarning("Телефонный справочник", "Введите имя или фамилию контакта для удаления.")

def create_gui():
    global entry_name, entry_phone, entry_search, entry_delete
    window = tk.Tk()
    window.title("Телефонный справочник")

    label_name = tk.Label(window, text="Имя:")
    label_name.pack()
    entry_name = tk.Entry(window)
    entry_name.pack()

    label_phone = tk.Label(window, text="Телефон:")
    label_phone.pack()
    entry_phone = tk.Entry(window)
    entry_phone.pack()

    button_add = tk.Button(window, text="Добавить", command=add_contact)
    button_add.pack()

    button_view = tk.Button(window, text="Просмотреть", command=view_contacts)
    button_view.pack()

    label_search = tk.Label(window, text="Поиск:")
    label_search.pack()
    entry_search = tk.Entry(window)
    entry_search.pack()

    button_search = tk.Button(window, text="Найти", command=search_contact)
    button_search.pack()

    label_delete = tk.Label(window, text="Удаление:")
    label_delete.pack()
    entry_delete = tk.Entry(window)
    entry_delete.pack()

    button_delete = tk.Button(window, text="Удалить", command=delete_contact)
    button_delete.pack()

    window.mainloop()

if __name__ == '__main__':
    create_gui()