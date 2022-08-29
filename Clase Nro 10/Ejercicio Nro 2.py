from cgitb import text
import tkinter as tk
from tkinter import ttk

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

class App(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Lista")
        self.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack()

    
    def add_item(self, item):
        if type(item) == list:
            for i in item:
                self.listbox.insert(tk.END, i)
        else:
          self.listbox.insert(tk.END, item)


main_window = tk.Tk()
app = App(main_window)
main_window.geometry("800x600")

app.add_item(months)

label = tk.Label(main_window, text="HOLA", textvariable=app.listbox.get(tk.ACTIVE))
label.pack()


app.mainloop()