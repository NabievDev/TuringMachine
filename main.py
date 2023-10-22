import flet as ft
from Machine import Machine

machine: Machine
click_first = False


def main(page: ft.Page):
    def clicked_word(e):
        global click_first
        if not click_first:
            click_first = True
            global machine
            machine.set_word(word.value)
            lent = ft.Text(value=machine.lent)
            instructions_view.controls.append(lent)
            instructions_view.controls.append(state)
            instructions_view.controls.append(letter)
            instructions_view.controls.append(replace_letter)
            instructions_view.controls.append(replace_state)
            instructions_view.controls.append(direction)
            instructions_view.controls.append(ft.Row(
                controls=[
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_instr),
                    ft.FilledButton(text="Результаты нахуй", on_click=start)
                ],
            ))
            page.update()

    def add_instr(e):
        global machine
        machine.add_instruction(state.value, letter.value, replace_letter.value, direction.value, replace_state.value)
        state.value = ""
        letter.value = ""
        replace_letter.value = ""
        replace_state.value = ""
        direction.value = ""
        page.update()

    def start(e):
        global machine
        instructions_view.controls.append(ft.Text(value=machine.start_machine()))
        page.update()

    state = ft.TextField(hint_text="Состояние")
    letter = ft.TextField(hint_text="Буква")
    replace_letter = ft.TextField(hint_text="Заменяемая буква")
    replace_state = ft.TextField(hint_text="Заменяемое состояние")
    direction = ft.TextField(hint_text="Направление")

    machine = Machine()
    click_first = False

    word = ft.TextField(hint_text="Какое слово ебать?")
    instructions_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    word,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=clicked_word),
                ],
            ),
            instructions_view,
        ],
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)


ft.app(target=main)
