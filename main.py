import flet as ft
from Machine import Machine

click_first = False


def main(page: ft.Page):

    machine = Machine()

    instructions = []

    def start(e):
        for i in range(0, len(instructions)):
            state1 = instructions[i].controls[0].value
            state2 = instructions[i].controls[3].value
            letter1 = instructions[i].controls[1].value
            letter2 = instructions[i].controls[2].value
            direction = instructions[i].controls[4].value
            machine.add_instruction(state1, letter1, letter2, direction, state2)

        lent = machine.start_machine()
        right_container.content.controls.append(
            ft.Text(
                value=f"{lent}",
                color=ft.colors.BLACK
            )
        )

        page.update()


    def click_word_button(e):
        global click_first
        if not click_first:
            machine.set_word(word.value)
            right_container.content.controls.append(
                ft.Text(
                    value=machine.lent,
                    color=ft.colors.BLACK
                )
            )
            right_container.content.controls.append(
                ft.ElevatedButton(text="Результаты", on_click=start)
            )
            click_first = True
        else:
            instructions.append(left_container.content.controls[-2])

        if len(instructions) != 0:
            state1 = instructions[-1].controls[0].value
            state2 = instructions[-1].controls[3].value
            letter1 = instructions[-1].controls[1].value
            letter2 = instructions[-1].controls[2].value
            direction = instructions[-1].controls[4].value
            right_container.content.controls.append(
                ft.Text(
                    value=f"{state1}->{state2}  {letter1}->{letter2}  {direction}",
                    color=ft.colors.BLACK
                )
            )

        icon_button = left_container.content.controls.pop()
        left_container.content.controls.append(
            ft.Row(
                controls=[
                    ft.TextField(
                        hint_text="Состояние",
                        color=ft.colors.WHITE,
                        width=110,
                        text_size=15
                    ),
                    ft.TextField(
                        hint_text="Буква",
                        color=ft.colors.WHITE,
                        width=110,
                        text_size=15
                    ),
                    ft.TextField(
                        hint_text="Замена буквы",
                        color=ft.colors.WHITE,
                        width=110,
                        text_size=15
                    ),
                    ft.TextField(
                        hint_text="Замена состояния",
                        color=ft.colors.WHITE,
                        width=110,
                        text_size=15
                    ),
                    ft.TextField(
                        hint_text="Направление",
                        color=ft.colors.WHITE,
                        width=110,
                        text_size=15
                    )
                ]
            )
        )
        left_container.content.controls.append(
            ft.Row(
                controls=[
                    icon_button
                ]
            )
        )
        page.update()

    word = ft.TextField(
        hint_text="Введите слово...",
        color=ft.colors.WHITE,
        width=550
    )

    left_column = ft.Column(
            controls=[
                ft.Text(
                    value="Настройка машины",
                    font_family="Lato",
                    color=ft.colors.WHITE,
                    style=ft.TextThemeStyle.TITLE_LARGE
                ),
                word,
                ft.IconButton(
                    icon=ft.icons.ADD,
                    icon_color=ft.colors.BLACK,
                    bgcolor=ft.colors.WHITE,
                    on_click=click_word_button
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    left_container = ft.Container(
        content=left_column,
        bgcolor=ft.colors.GREY_900,
        width=625,
        height=650
    )

    right_column = ft.Column(
        controls=[
            ft.Text(
                value="Показ машины",
                style=ft.TextThemeStyle.TITLE_LARGE,
                font_family="Lato"
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    right_container = ft.Container(
        content=right_column,
        bgcolor=ft.colors.WHITE12,
        width=625,
        height=650
    )

    page.add(ft.Row(controls=[
        left_container,
        right_container
    ]))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
