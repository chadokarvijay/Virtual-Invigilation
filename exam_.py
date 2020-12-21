import tkinter as tk
import tkinter.ttk as ttk
py3 = True
def set_Tk_var():
    global che135
    che135 = tk.IntVar()
    global che136
    che136 = tk.IntVar()
    global che137
    che137 = tk.IntVar()
    global che138
    che138 = tk.IntVar()
    global tch145
    tch145 = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None






