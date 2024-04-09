import flet as ft
import os
 
def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        savedpath.value = e.files[0].path
        with open (str(e.files[0].path), "r") as file:
            tb.value = file.read()
        tb.update()

        if not os.path.exists(savedpath.value):
                with open (savedpath.value, "w") as file:
                    file.write(tb.value)
                
                tb.update()
        tb.update()

    def savethefile(e):
        with open (savedpath.value, "w")as file:
            file.write(tb.value)

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
 
    page.overlay.append(pick_files_dialog)
 
    def textbox_changed(e):
 
        palabras.value = f"Word Count: {len(tb.value.split())}"
        page.update()

    savedpath = ft.Text("")
    palabras = ft.Text(value="Word Count: ")
    tb = ft.TextField(
        label="Textbox: ", on_change=textbox_changed, multiline=True
    )


    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Open",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )
 
    page.add(
        ft.Row(controls=
            [
                ft.ElevatedButton(
                    "Create",
                ),
                ft.ElevatedButton(
                    "Save", on_click=savethefile
                ),
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )
    page.add(tb)
    page.add(
        ft.Row(controls=
            [
                palabras,
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )
 
 
ft.app(target=main)