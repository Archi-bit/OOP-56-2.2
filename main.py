import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение на flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    greeting_text = ft.Text('Hello World')
    name_input = ft.TextField(label="Введите имя: ")

    def get_greeting(name: str) -> str:
        hour = datetime.now().hour
        if 6 <= hour < 12:
            return f"Доброе урто, {name}"
        elif 12 <= hour <18:
            return f"Добрый день, {name}"
        elif 18 <= hour <24:
            return f"Добрый вечер, {name}"
        else:
            return f"Доброй ночи, {name}"

    def update_history_view():
        history_controls = [ft.Text("История приветствий: ")]
        for idx, name in enumerate(greeting_history):
            history_controls.append(
                ft.Row([ft.Text(name),
                        ft.IconButton(icon=ft.Icons.CLOSE, on_click=lambda e, i=idx: remove_name_from_history(i))
                        ])
            )
        history_column.controls = history_controls
        page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):
            del greeting_history[index]
            update_history_view()

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            greeting_text.value = get_greeting(name)
            name_input.value = ''
            greet_button.text = 'Поздороваться снова'

            

        else:
            greeting_text.value = "Введите корректное имя"
        page.update()

    greet_button = ft.ElevatedButton("отправить", on_click=on_button_click)
    greet_button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click, icon_color=ft.Colors.AMBER_200)
        
        
    history_column = ft.Column([])
    update_history_view()

    # page.add(greeting_text, name_input, greet_button, history_column)
    page.add(ft.Row([greeting_text, name_input, greet_button_icon], alignment=ft.MainAxisAlignment.CENTER), history_column)



ft.app(target=main) 
