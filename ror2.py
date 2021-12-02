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
        sublabel = ttk.Label(self, text = "Testing Module", font = ("Verdana", 20))
         
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
        command = lambda : controller.show_frame(Randomize_Run))
     
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

class Randomize_Run(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        artifacts = ["Chaos", "Command", "Death", "Dissonance", "Enigma", "Evolution", "Frailty", "Glass", "Honor", "Kin", "Metamorphosis", "Sacrifice", "Soul", "Spite", "Swarms", "Vengence"]

        gen_but = ttk.Button()
        label = ttk.Label(self, text ="Randomize Run", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        survivorframe = tk.Frame(self, relief = tk.SUNKEN, borderwidth=3)
        survivorframe.grid(row = 1, column = 0)
        survlabel = ttk.Label(survivorframe, font = TINYFONT)
        
        artifactframe = tk.Frame(self, relief = tk.SUNKEN, borderwidth=3)
        artifactframe.grid(row = 1, column= 1)
        num_of_artifacts = 0
        randarts = []
        artlabels = []

        difflabel = ttk.Label(self)

        def gen():
            #delete the generate button
            gen_but.grid_forget()

            # GENERATE A RANDOM SURVIVOR
            randnum = random.randint(0, NUMBER_OF_SURVIVORS-1)
            surv = survivors[randnum]

            #load image of survivor
            canvas = tk.Canvas(survivorframe, width=128, height=128)
            img = ImageTk.PhotoImage(Image.open(f"pictures\survivors\{surv}.png"))
            canvas.create_image(0, 0, anchor = 'nw', image = img)
            canvas.image = img
            canvas.grid(row = 1, column = 1)
            
            #make label for the suvivor
            survlabel.configure(text = surv)
            survlabel.grid(row = 0, column = 1)

            #GENERATE RANDOM ARTIFACTS

            #create array for randomly selected artifacts
            #randarts = []
            #artlabels = []
            num_of_artifacts = random.randint(1, 4) #program will generate between 1 to 4 artifacts
            for i in range(num_of_artifacts):
                artifact = artifacts[random.randint(0, len(artifacts)-1)]
                lbl = ttk.Label(artifactframe, text = f"Artifact of {artifact}")
                artlabels.append(lbl)
                randarts.append(artifact)

            #iterate through randomly chosen artifacts and add them to the frame
            for i in range(len(randarts)):
                label = artlabels[i]
                artname = randarts[i]

                artcanvas = tk.Canvas(artifactframe, width =64, height=64)
                img = ImageTk.PhotoImage(Image.open(f"pictures\\artifacts\{artname}.png"))
                artcanvas.create_image(0, 0, anchor = 'nw', image = img)
                artcanvas.image = img

                artcanvas.grid(row = i, column = 0)
                label.grid(row = i, column = 1)
            
            randarts.clear()
            artlabels.clear()
                
            # GENERATE RANDOM DIFFICULTY
            diffval = random.randint(0, 3)
            if diffval == 0:
                difficulty = "Drizzle"
            elif diffval == 1:
                difficulty = "Rainstorm"
            else:
                difficulty = "Monsoon"

            difflabel.configure(text = difficulty)
            difflabel.grid(row = 1, column=2)

        # generate button that calls the generate player frames function
        gen_but = ttk.Button(self, text = "GENERATE", command= gen)
        gen_but.grid(row = 4, column= 2)

        # function called by the home button
        # clears the frame
        def close_page():            
            # replace the generate button
            gen_but = ttk.Button(self, text = "GENERATE", command= gen)
            gen_but.grid(row = 4, column= 2)

            #delete artifact labels
            artlabels.clear()
            randarts.clear()
            num_of_artifacts = 0
            controller.show_frame(StartPage)

        # create home button to go back to the start page
        homebut = ttk.Button(self, text ="Home", command = close_page) 
        homebut.grid(row = 5, column = 2, padx = 10, pady = 10)


#driver code
app = application()
app.mainloop()