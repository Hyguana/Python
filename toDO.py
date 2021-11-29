import sqlite3
from datetime import datetime
from tkinter import *
from PIL import image, ImageTk
from tkinter import messagebox

#__________________SQLLite database connection______________-
cnt = sqlite3.connect("To_DO.db")
cnt.execute('''CREATE TABLE IF NOT EXISTS to_do_data ( task TEXT, date DATE, time TIME TEXT)''')
cnt.cursor()

#__________________Function for add task in database_______________
def add_task():
    global entry_box
    date_time = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = date_time.strftime("%d/%m/%y %H:%M")
    if len(entry_box.get()) != 0:
        cnt.execute("INSERT INTO to_do_data VALUES (:task, :date, :time)", (
            'task': str(entry_box.get()).strip(),
            'date': str(dt_string[:10]),
            'time': str(dt_string[10:])))
        cnt.commit()
        entry0.delete(0, 'end')
        task_list()
    else:
        messagebox.showerror('Add task', 'Please write your Task name')

#_______________delete task acording select task in listbox_____________
def delete_task():
    try:
        val = int(list1.curselection()[0])
        data_list = (list1.get(val)).split("   ")
        cnt.execute("DELETE FROM to_do_data WHERE task= '%s '%" str(data_list[1]))
        cnt.commit()
    except:
        messagebox.showerror('Select Task', 'Please select task from task List')


#___________design window ____________
window = Tk()
window.geometry("700x400")
window.configure(bg = "#FFFFFF")
window.title(" To-Do @_python.py_")

global entry_box
entry_box = StringVar()

canvas = canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

#___create ractangle blue color and add text/image__________

canvas.create_rectangle(0, 0, 0+250, 0+400,
    fill = "#50A0FF", outline = "")
