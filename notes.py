import json
import os
from datetime import datetime

def load_notes():
    if not os.path.exists('notes.json'):
        return []
    with open('notes.json', 'r') as file:
        notes = json.load(file)
    return notes

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def add_note():
    notes = load_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    
    note = {
        "id": str(maxID() + 1),
        "title": title,
        "body": body,
        "timestamp": str(datetime.now())
    }
    
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def maxID():
    notes = load_notes()
    max_id = 0
    for item in notes:
        if max_id < int(item['id']):
            max_id = int(item['id'])
    return max_id

def read_notes():
    notes = load_notes()
    
    if len(notes) == 0:
        print("Нет доступных заметок.")
        return
    
    for note in notes:
        print(f"Идентификатор: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст заметки: {note['body']}")
        print(f"Дата/время создания или последнего изменения: {note['timestamp']}")
        print("---")

def edit_note():
    notes = load_notes()
    
    id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
    
    for note in notes:
        if note['id'] == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    
    print("Заметка с указанным идентификатором не найдена.")

def delete_note():
    notes = load_notes()
    
    id = input("Введите идентификатор заметки, которую хотите удалить: ")
    
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    
    print("Заметка с указанным идентификатором не найдена.")


while True:
    print("--- Меню ---")
    print("1. Добавить заметку")
    print("2. Прочитать заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("0. Выход")
    
    choice = input("Выберите пункт меню: ")
    
    if choice == '1':
        add_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '0':
        break
    else:
        print("Некорректный ввод")   