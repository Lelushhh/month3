import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value="История приветствий:")

    last_name = None
    favourite_name = []
    name_text = ft.Text(value="ListView")

    # greeting_text.value = 'Привет'
    # greeting_text.color = ft.Colors.GREEN
    
    def on_button_click(_):
        # print(name_input.value)
        nonlocal last_name

        name = name_input.value.strip()

        
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(f"{timestamp} - {name}")

            if len(greeting_history) == 5:
                greeting_history.clear()

            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)

            last_name = name

        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        # print(greeting_text)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()
        print(greeting_history)
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    def add_to_favorites(_):
        nonlocal last_name, favourite_name, name_text
        if last_name:
            favourite_name.append(last_name)
            name_text.value = 'ListView:\n' + '\n'.join(favourite_name)
        else:
            name_text.value = 'ListView:\n(Нет имени для добавления)'

        page.update()
        print(favourite_name)

    favourites_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_to_favorites)
    

    # page.add(greeting_text, name_input, button_text, history_text )

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(view_greeting_text, ft.Row([name_input, button_elevated, clear_button, favourites_button]), history_text, name_text)


ft.app(target=main)