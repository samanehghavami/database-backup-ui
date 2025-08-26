import flet as ft
import os
from datetime import datetime

def backup(db_type, host, user, password, database, path):
    os.makedirs(path, exist_ok=True)
    date = datetime.now().strftime("%Y%m%d")
    filename = os.path.join(path, f"{database}_{date}.sql")

    if db_type == "mysql":
        cmd = f"mysqldump -h{host} -u{user} -p{password} {database} > {filename}"
    elif db_type == "postgresql":
        cmd = f"pg_dump -h {host} -U {user} -d {database} -f {filename}"
    else:
        return False, " Invalid database type"

    if os.system(cmd) == 0:
        return True, f" Backup successfully saved at:\n{filename}"
    else:
        return False, " Backup failed"


def main(page: ft.Page):
    page.title = "Backup Database"

    type = ft.Dropdown(
        label="Select database type",
        options=[
            ft.dropdown.Option("mysql"),
            ft.dropdown.Option("postgresql")
        ],
        width=800
    )
    host_field = ft.TextField(label="Host")
    user_field = ft.TextField(label="User")
    pass_field = ft.TextField(label="Password", password=True, can_reveal_password=True)
    db_field = ft.TextField(label="Database")

    folder_path = ft.TextField(label="Selected Folder", read_only=True, width=400)
    result_label = ft.Text(value="", color="green")

    def on_result(e: ft.FilePickerResultEvent):
        if e.path:
            folder_path.value = e.path
            page.update()

    file_picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(file_picker)

    browse_btn = ft.ElevatedButton(
        "Browse",
        on_click=lambda _: file_picker.get_directory_path(),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10))
    )

    def on_click(e):
        ok, msg = backup(
            type.value,
            host_field.value,
            user_field.value,
            pass_field.value,
            db_field.value,
            folder_path.value
        )
        result_label.value = msg
        result_label.color = "green" if ok else "red"
        page.update()

    path_btn = ft.Row(controls=[folder_path, browse_btn])
    host_user = ft.Row(controls=[host_field, user_field])
    pass_db = ft.Row(controls=[pass_field, db_field])
    button = ft.ElevatedButton(
        text="Backup",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(5)),
        on_click=on_click
    )

    page.add(type, path_btn, host_user, pass_db, button, result_label)


ft.app(target=main)
