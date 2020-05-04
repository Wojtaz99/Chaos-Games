from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import tkinter.font as font


def menu_gui():
    # Gui menu programu
    root = Tk() # puste okno
    root.wm_title("Chaos Games Menu")
    root.resizable(False, False)

    colours = ['yellow','orange','red','green','blue','purple']
    title_label = Label(text="Chaos Game", \
                        font=font.Font(family="Segoe UI bold", size=25))
    title_label.grid(row=0, columnspan=2, pady=3)
    info_label = Label(text="Wybierz kolor do rysowania", \
                        font=font.Font(family="Segoe UI", size=17))
    info_label.grid(row=1)

    for i in range(len(colours) // 2):
        Button(bg=colours[i], relief=RIDGE, width=40, height=3, cursor="hand2") \
                .grid(row=i+2, column=0, pady=2)
    for i in range(len(colours) // 2, len(colours)):
        Button(bg=colours[i], relief=RIDGE, width=40, height=3, cursor="hand2") \
                .grid(row=i-1, column=1, pady=2)
    # Zdjęcie kostek
    path = str(Path(__file__).parent.absolute())
    load = Image.open(path + "\\kostki.png")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.grid(row=1, column=1)

    root.mainloop() # sprawia, że okno się nie zamyka


menu_gui()