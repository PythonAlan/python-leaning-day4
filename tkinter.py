#!/usr/bin/env python3
#antuor:Alan
from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(expresstion.get())
        result.set((0.3048 * value * 10000.0 + 0.5)/10000.0)

    except ValueError:
        pass

root = Tk()
root.title("计算器")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

expresstion = StringVar()
result = StringVar()

expresstion_entry = ttk.Entry(mainframe, width=7, textvariable=expresstion)
expresstion_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="公式").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="结果：").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

expresstion_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()

