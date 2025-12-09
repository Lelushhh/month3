import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    
    greeting_text = ft.Text(spans=[])

    greeting_history = []
    history_text = ft.Text(value="История приветствий:")

    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
        
            greeting_text.spans = [
                ft.TextSpan(f"{timestamp} Hello "),
                ft.TextSpan(
                    name,
                    ft.TextStyle(
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE
                    )
                )
            ]
            

            name_input.value = None

            greeting_history.append(f"{timestamp} - {name}")
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)

        else:
            greeting_text.spans = [
                ft.TextSpan(
                    "Введите корректное имя",
                    ft.TextStyle(color=ft.Colors.RED)
                )
            ]

        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(view_greeting_text, ft.Row([name_input, button_elevated, clear_button]), history_text)


ft.app(target=main)