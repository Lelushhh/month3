import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    def on_button_click(e):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

        if name:
            greeting_text.value = f"{timestamp} Hello {name}"
            greeting_text.color = None
            name_input.value = ''
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED

        page.update()

    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    theme_button = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_7,
        on_click=toggle_theme
    )

    page.add(
        greeting_text,
        name_input,
        button_text,
        button_elevated,
        button_icon,
        theme_button
    )

ft.app(target=main, view=ft.WEB_BROWSER)

