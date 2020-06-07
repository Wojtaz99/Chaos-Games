# -*- coding: utf-8 -*-
from tkinter import *
from pathlib import Path
from PIL import ImageTk, Image
import tkinter.font as font
import foremne
import paprotka
import sniezynka
import anti_clock
import zbiory_julii


class Menu(Frame):
    """Klasa menu symulatora Chaos Games"""
    def __init__(self):
        super().__init__()
        self.menu_gui()

    def menu_gui(self):
        self.master.title("Chaos Games Menu")
        colours = ['yellow', 'green', 'white', 'red', 'pink']
        greetings = "Witaj w symulatorze Chaos Games"
        title_label = Label(text=greetings,
                            font=font.Font(family="Segoe UI bold", size=25))
        title_label.grid(row=0, columnspan=2, pady=10, padx=10)
        info_text = "Wybierz jeden z dostepnych trybow symulacji"
        info_label = Label(text=info_text,
                           font=font.Font(family="Segoe UI", size=17))
        info_label.grid(row=1, columnspan=2, pady=10, padx=10)
        button_font = font.Font(family="Segoe UI", size=12, weight="bold")
        Button(bg=colours[0],
               relief=RIDGE,
               width=40,
               height=3,
               cursor="hand2",
               text="Figury foremne",
               font=button_font,
               command=foremne.Foremne).grid(row=3, column=0, pady=2, padx=2)
        Button(bg=colours[1],
               relief=RIDGE,
               width=40,
               height=3,
               cursor="hand2",
               text="Paprotka",
               font=button_font,
               command=paprotka.Fern).grid(row=4,
                                           column=0,
                                           pady=2,
                                           padx=2)
        Button(bg=colours[2],
               relief=RIDGE,
               width=40,
               height=3,
               cursor="hand2",
               text="Sniezynka",
               font=button_font,
               command=sniezynka.Pentaflake).grid(row=5,
                                                  column=0,
                                                  pady=2,
                                                  padx=2)
        Button(bg=colours[3],
               relief=RIDGE,
               width=40,
               height=3,
               cursor="hand2",
               text="Smieszny kwadrat",
               font=button_font,
               command=anti_clock.Anti_clock).grid(row=6,
                                                   column=0,
                                                   pady=2,
                                                   padx=2)
        Button(bg=colours[4],
               relief=RIDGE,
               width=40,
               height=3,
               cursor="hand2",
               text="Zbiory Julii",
               font=button_font,
               command=lambda: self.julia_set_launch(e1)).grid(row=7,
                                                               column=0,
                                                               pady=2,
                                                               padx=2)
        e1 = Entry(self.master)
        e1.grid(row=7, column=1)
        # Zdjecie kostek
        path = str(Path(__file__).parent.absolute())
        load = Image.open(path + "/kostki.png")
        render = ImageTk.PhotoImage(load)
        img = Label(image=render)
        img.grid(row=3, column=1, rowspan=4)
        self.mainloop()  # Sprawia, że okno sie nie zamyka

    def julia_set_launch(self, e1):
        try:
            tab = e1.get().split(" ")
            zbiory_julii.Julia_set([float(tab[0]), float(tab[1])])
        except(IndexError, AttributeError, ValueError):
            zbiory_julii.Julia_set()


if __name__ == "__main__":
    Menu()
