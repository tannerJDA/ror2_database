import tkinter as tk

drkblue = "#3254a8"

def clear_widg(win):
    for i in win.winfo_children():
        i.destroy()
    
    canvas = tk.Canvas(root, height = 700, width = 700, bg="#3254a8")
    canvas.pack()

    backbtn = tk.Button(win, text="Back", command = lambda: home(win))
    backbtn.place(x=600, y=600)

def generate_loadout(win):
    print("generate loadout clicked")
    clear_widg(win)

    gl_lbl = tk.Label(win, text="Generate Loadout", font = ("Arial Bold", 45), bg = drkblue)
    gl_lbl.place(x=100, y=70)
    

def record_run(win):
    print('record run clicked')
    clear_widg(win)

    rr_lbl = tk.Label(win, text="Record Run", font = ("Arial Bold", 45), bg = drkblue)
    rr_lbl.place(x=150, y=70)

def randomize_settings(win):
    print('randomize settings clicked')
    clear_widg(win)

    rs_lbl = tk.Label(win, text="Randomize Settings", font = ("Arial Bold", 45), bg = drkblue)
    rs_lbl.place(x=70, y=70)


def home(win):
    frm = tk.Frame(win)

    try:
        for i in win.winfo_children():
            print(i)
            if i.winfo_class() == "Button":
                i.destroy()

    except:
        pass

    head_lbl = tk.Label(win, text="Risk of Rain 2 Database", font = ("Arial Bold", 45), bg = "#3254a8")
    head_lbl.place(x=10, y=70)

    btn1 = tk.Button(win, text="Generate Loadout", font = ("Arial", 20), bg = "lightgray", command = lambda: generate_loadout(win))
    btn1.place(x=200, y = 150)

    btn2 = tk.Button(win, text="Record Run", font = ("Arial", 20), bg = "lightgray", command = lambda: record_run(win))
    btn2.place(x=230, y = 220)

    btn3 = tk.Button(win, text="Randomize Settings", font = ("Arial", 20), bg = "lightgray", command = lambda: randomize_settings(win))
    btn3.place(x=200, y = 290)

    btn4 = tk.Button(win, text="Browse Items", font = ("Arial", 20), bg = "lightgray")
    btn4.place(x=230, y = 360)

    frm.pack()

# --- Main Function ---
if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, height = 700, width = 700, bg="#3254a8")
    canvas.pack()
    home(root)

    
root.mainloop()