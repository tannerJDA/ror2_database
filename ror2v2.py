import tkinter as tk
from tkinter import StringVar, ttk
from tkinter.constants import ANCHOR


LARGEFONT =("Arial", 35)
MEDFONT = ("Arial", 20)

class application(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ fucntion for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        #create a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)

        #initializing frames to an empty array
        self.frames = {}

        #iterate throught a tuple consisting of the different page layouts
        for F in (StartPage, Generate_Loadout, Record_Run, Randomize_Run):
            frame = F(container, self)

            #initialize fram of that object from page tuple
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)

    #display current frame passed as a parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

         # label of frame Layout 2
        label = ttk.Label(self, text ="Risk of Rain 2", font = LARGEFONT)
        sublabel = ttk.Label(self, text = "Database", font = ("Verdana", 20))
         
        # place the head label in row 0 col 4
        # place the sub label in row 1 col 4
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        sublabel.grid(row = 1, column = 4, padx = 5, pady = 0)
  
        button1 = ttk.Button(self, text ="Generate Loadout",
        command = lambda : controller.show_frame(Generate_Loadout))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Record Run",
        command = lambda : controller.show_frame(Record_Run))
     
        # place button 2 in row 2 col 1
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        ## create button for the randomize run function
        button3 = ttk.Button(self, text ="Randomize_Run",
        command = lambda : controller.show_frame(Randomize_Run))
     
        # place button 3 in row 3 col 1
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

# second window frame page1
class Generate_Loadout(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Generate Loadout", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
    
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
     
        
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

  
  
# third window frame page2
class Record_Run(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        min_val = tk.StringVar()
        hour_val = tk.StringVar()
        diff_val = tk.StringVar()
        surv_val = tk.StringVar()

        headlabel = ttk.Label(self, text ="Record Run", font = LARGEFONT)
        headlabel.grid(row = 0, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = 5, column = 2, padx = 10, pady = 10)

        lbl1 = ttk.Label(self, text = "Select Survivor", font = MEDFONT)
        lbl1.grid(row = 1, column = 0)

        survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        survivs_var = tk.StringVar(value=survivors)
        listbox = tk.Listbox(self, listvariable=survivs_var, height = 7, selectmode='single')
        listbox.grid(row = 3, column=0)

        lbl2 = ttk.Label(self, text = "Input Run Time", font = MEDFONT)
        lbl2.grid(row = 1, column = 1)

        min_entry = ttk.Entry(self, textvariable = min_val)
        hour_entry = ttk.Entry(self, textvariable = hour_val)

        min_entry.grid(row = 2, column=1, padx = 10, pady = 10)
        hour_entry.grid(row = 3, column=1, padx = 10, pady = 10)


        lbl3 = ttk.Label(self, text = "Select Difficulty", font = MEDFONT)
        lbl3.grid(row = 1, column = 2)
        
        # create the radiobuttons for selecting difficulty
        radbut1 = ttk.Radiobutton(self, text = "Drizzle", variable= diff_val, value = 0)
        radbut2 = ttk.Radiobutton(self, text = "Rainstorm", variable= diff_val, value = 1)
        radbut3 = ttk.Radiobutton(self, text = "Monsoon", variable= diff_val, value = 2)

        radbut1.grid(row = 2, column=2)
        radbut2.grid(row = 3, column=2)
        radbut3.grid(row = 4, column=2)

        # nested function that will be called by the submit button to add the inputted data into the sql database
        def submit_run(survivor, hours, minutes, diff):
            if diff == 2:
                difficulty = 'Monsoon'
            elif diff == 1:
                difficulty = 'Rainstorm'
            else:
                difficulty = 'Drizzle' 

            print(f"""
            Submitting run with data...\n
            Survivor - {survivor}\n
            Hours - {hours}\n
            Minutes - {minutes}\n
            Difficulty - {difficulty}\n
            """)

            hour_val.set("")
            min_val.set("")

        surv_val = listbox.get(ANCHOR)
         

        # create submit button
        submitbut = ttk.Button(self, text = "Submit", command = lambda: submit_run(surv_val, hour_val.get(), min_val.get(), diff_val))
        submitbut.grid(row = 5, column=1)


# third window frame page2
class Randomize_Run(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Record Run", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(StartPage))
    
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


#driver code
app = application()
app.mainloop()