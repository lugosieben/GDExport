import gd
import asyncio
import customtkinter
from tkinter import filedialog

client = gd.Client()


def find_level_from_server(id):
    return client.get_level(id)


async def get_level(input):
    if input == "":
        return
    level = await find_level_from_server(int(input))
    file = filedialog.asksaveasfilename(
        defaultextension='.txt',
        filetypes=(
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ),
        initialfile=level.name + '.txt'
    )
    if not file:
        return
    file.write(level.download())
    file.close()
    print(level.name + " - " + level.creator.name)
    info.configure(text="Level " + level.name + " was saved as " + file.name)
    return level


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("GDExport")
app.resizable(False, False)

title = customtkinter.CTkLabel(app, text="GDExport", font=("Arial", 35))
title.pack(padx=20, pady=30)

entry = customtkinter.CTkEntry(app, width=80, height=25, placeholder_text="Level ID", justify="center")
entry.pack(padx=20, pady=10)


def button_function():
    id = entry.get()
    downloaded = asyncio.run(get_level(id))
    return downloaded


button = customtkinter.CTkButton(app, width=100, height=25, text="Export to Files", command=button_function)
button.pack(padx=20, pady=0)

info = customtkinter.CTkLabel(app, text="", font=("Arial", 11), text_color="lightblue")
info.pack()

app.mainloop()
