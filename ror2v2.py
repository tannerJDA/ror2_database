import tkinter as tk
from tkinter import PhotoImage, StringVar, image_names, ttk
from tkinter.constants import ACTIVE, ANCHOR
from PIL import ImageTk, Image
import random

LARGEFONT =("Arial", 35)
MEDFONT = ("Arial", 20)
TINYFONT = ("Arial", 9)
NUMBER_OF_PLAYERS = 1
NUMBER_OF_SURVIVORS = 12

containerarray = []
labelarray = []

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
        for F in (StartPage, Generate_Loadout, Record_Run, Randomize_Run_p1, Randomize_Run_p2):
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
        button3 = ttk.Button(self, text ="Randomize Run",
        command = lambda : controller.show_frame(Randomize_Run_p1))
     
        # place button 3 in row 3 col 1
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

# window for the generate loadout function
class Generate_Loadout(tk.Frame):   
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Generate Loadout", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        homebut = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))        
        homebut.grid(row = 3, column = 1, padx = 10, pady = 10)

  
  
# window for record run page
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
        button2.grid(row = 5, column = 3, padx = 10, pady = 10)

        lbl1 = ttk.Label(self, text = "Select Survivor", font = MEDFONT)
        lbl1.grid(row = 1, column = 0)
        
        # creating the listbox for the user to select which survivor they played as
        survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        survivs_var = tk.StringVar(value=survivors)
        listbox = tk.Listbox(self, listvariable=survivs_var, height = 7, selectmode='single')
        listbox.grid(row = 3, column=0)

        lbl2 = ttk.Label(self, text = "Input Run Time", font = MEDFONT)
        lbl2.grid(row = 1, column = 1)

        #min_label = ttk.Label(self, text = "Minutes")
        #hour_label = ttk.Label(self, text = "Hours")
        min_entry = ttk.Entry(self, textvariable = min_val)
        hour_entry = ttk.Entry(self, textvariable = hour_val)

        min_entry.grid(row = 2, column=1, padx = 0, pady = 10)
        hour_entry.grid(row = 3, column=1, padx = 0, pady = 10)
        #min_label.grid(row = 2, column = 1, padx = 0)
        #hour_label.grid(row = 3, column = 1, padx = 0)

        lbl3 = ttk.Label(self, text = "Select Difficulty", font = MEDFONT)
        lbl3.grid(row = 1, column = 3)
        
        # create the radiobuttons for selecting difficulty
        radbut1 = ttk.Radiobutton(self, text = "Drizzle", variable= diff_val, value = 0)
        radbut2 = ttk.Radiobutton(self, text = "Rainstorm", variable= diff_val, value = 1)
        radbut3 = ttk.Radiobutton(self, text = "Monsoon", variable= diff_val, value = 2)

        radbut1.grid(row = 2, column=3)
        radbut2.grid(row = 3, column=3)
        radbut3.grid(row = 4, column=3)

        # nested function that will be called by the submit button to add the inputted data into the sql database
        def submit_run(hours, minutes, diff):
            print(f"diff value = {diff}")

            if int(diff) == 2:
                difficulty = 'Monsoon'
            elif int(diff) == 1:
                difficulty = 'Rainstorm'
            else:
                difficulty = 'Drizzle' 

            survivor = listbox.get(ANCHOR)

            print(f"""
            Submitting run with data...\n
            Survivor - {survivor}\n
            Hours - {hours}\n
            Minutes - {minutes}\n
            Difficulty - {difficulty}\n
            """)

            # reset the values in the input sections
            hour_val.set("")
            min_val.set("")
            listbox.activate(0)
         
        # create submit button
        submitbut = ttk.Button(self, text = "Submit", command = lambda: submit_run(hour_val.get(), min_val.get(), diff_val.get()))
        submitbut.grid(row = 5, column=1)

# landing page for the randomize run functions where the user will input how many players will be in the run (up to 4)
class Randomize_Run_p1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        numplayers = tk.StringVar()
        #global NUMBER_OF_PLAYERS

        # nested function to load the next page for the randomize run function
        def load_rrp2():
            global NUMBER_OF_PLAYERS
            NUMBER_OF_PLAYERS = int(numplayers.get())
            numplayers.set("") # empty the entry field after input is recieved
            controller.show_frame(Randomize_Run_p2)

        label = ttk.Label(self, text ="Randomize Run 1", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        homebut = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        homebut.grid(row = 4, column = 1, padx = 10, pady = 10)

        label1 = ttk.Label(self, text = "How many players will there be?", font = MEDFONT)
        label1.grid(row = 1, column = 1)

        user_in = ttk.Entry(self, textvariable=numplayers)
        user_in.grid(row = 2, column= 1)

        submitbut = ttk.Button(self, text = "Submit", command=load_rrp2)
        submitbut.grid(row = 3, column=1)

        


# main page for the randomize run function where the randomized settings will be output to the user
class Randomize_Run_p2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #global NUMBER_OF_PLAYERS

        label = ttk.Label(self, text ="Randomize Run 2", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        homebut = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage)) 
        homebut.grid(row = 4, column = 2, padx = 10, pady = 10)

        # create the frame to store the pictures of survivors
        player_frame = ttk.Frame(self, relief=tk.SUNKEN, borderwidth=3)
        player_frame.grid(row = 3, column=0)

        survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        
        #create a canvas and label for each player in the game
        for i in range(NUMBER_OF_PLAYERS+2):
            # populate container array with empty canvases
            canvas = tk.Canvas(player_frame, width = 128, height = 128)
            containerarray.append(canvas)

                # populate label array with proper labels
            lbl = ttk.Label(player_frame, text = f"Player {i}", font = TINYFONT)
            labelarray.append(lbl)

        size = len(containerarray)
        print (f"There are {size} containers")

        for i in range(NUMBER_OF_PLAYERS+2):
            generated = random.randint(0, NUMBER_OF_SURVIVORS) #generate a random integer in the range of the number of survivors to pick from
            surv = survivors[generated]

            label = labelarray[i]
            cont = containerarray[i]
            img = ImageTk.PhotoImage(Image.open(f"pictures\{surv}.png"))
            cont.create_image(0, 0, anchor = 'nw', image = img)
            cont.image = img

            label.grid(row = 0, column = i, padx = 0, pady = 0)
            cont.grid(row = 1, column = i, padx = 0, pady = 0)
        
        '''
        # test code for loading on image into the player frame
        canvas1 = tk.Canvas(player_frame, width = 128, height = 128)
        canvas1.grid(row = 0, column=0)
        img = ImageTk.PhotoImage(Image.open("pictures\Captain.png"))
        canvas1.create_image(0, 0, anchor = 'nw', image = img)
        canvas1.image = img
        '''


        # debugging function to output the currently held value for number of players
        def show_num():
            print(f"Selected number of players = {NUMBER_OF_PLAYERS}")
        testbut = ttk.Button(self, text = "test", command=show_num)
        testbut.grid(row = 4, column=0)

#driver code
app = application()
app.mainloop()