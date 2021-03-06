import tkinter as tk
from tkinter import PhotoImage, StringVar, image_names, ttk
from tkinter.constants import ACTIVE, ANCHOR
from PIL import ImageTk, Image
import random
import mysql.connector
import os
from pathlib import Path

LARGEFONT =("Arial Bold", 35)
MEDFONT = ("Arial", 20)
BOLDMEDFONT = ("Arial", 15)
TINYFONT = ("Arial", 9)
NUMBER_OF_PLAYERS = 1
NUMBER_OF_SURVIVORS = 12

survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]

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

        self.title("ROR2 Database")
        cwd = os.getcwd()
        logoimg = PhotoImage(file = os.path.join(cwd, "ror2_database\pictures\logo.png"))
        self.iconphoto(False, logoimg)
        self.state('zoomed')


        #initializing frames to an empty array
        self.frames = {}

        #iterate throught a tuple consisting of the different page layouts
        for F in (StartPage, Generate_Loadout, Record_Run, Randomize_Run, Browse_DB,
        View_Survivors, View_Challenges, View_Items, View_Skills, View_Artifacts, View_Monsters, View_Runs):

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

        #self.config(bg= 'Blue')

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
        command = lambda : controller.show_frame(Randomize_Run))
     
        # place button 3 in row 3 col 1
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

        button4 = ttk.Button(self, text = "Browse Database",
        command= lambda : controller.show_frame(Browse_DB))
        button4.grid(row = 4, column=1)

class Browse_DB(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "Browse Database", font = LARGEFONT)
        lbl.grid(row = 0, column=0)

        survsbut = ttk.Button(self, text = "View Survivors",
        command= lambda : controller.show_frame(View_Survivors))
        survsbut.grid(row = 1, column=0)

        challbut = ttk.Button(self, text = "View Challenges",
        command = lambda : controller.show_frame(View_Challenges))
        challbut.grid(row = 2, column=0)

        itembut = ttk.Button(self, text = "View Items",
        command = lambda : controller.show_frame(View_Items))
        itembut.grid(row = 3, column=0)

        skillbut = ttk.Button(self, text = "View Skills",
        command = lambda : controller.show_frame(View_Skills))
        skillbut.grid(row = 4, column=0)

        artbut = ttk.Button(self, text = "View Artifacts",
        command = lambda : controller.show_frame(View_Artifacts))
        artbut.grid(row = 5, column=0)

        monbut = ttk.Button(self, text = "View Monsters",
        command = lambda : controller.show_frame(View_Monsters))
        monbut.grid(row = 6, column=0)

        runbut = ttk.Button(self, text = "View Run History",
        command = lambda : controller.show_frame(View_Runs))
        runbut.grid(row = 7, column=0)

         # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = 5, column = 3, padx = 10, pady = 10)


class View_Survivors(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Survivors", font = MEDFONT)
        lbl.grid(row = 0, column=1)
        
        ### ADD COLUMN HEADERS ###
        lbl = ttk.Label(self, text = "Unlock", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Name", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Health", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Regen", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)
        lbl = ttk.Label(self, text = "Damage", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 4)
        lbl = ttk.Label(self, text = "Armor", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 5)
        lbl = ttk.Label(self, text = "Speed", anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 6)

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM Survivor ORDER BY surv_name")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, width = 20, text = elem[j], anchor = 'center')
                e.grid(row = i, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()


class View_Items(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "ACTIVE ITEMS", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        ### ADD COLUMN HEADERS ###
        lbl = ttk.Label(self, text = "Name", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Cooldown", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = 1, column = 1)

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM ActiveItems")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, width = 20, text = elem[j], anchor = 'center')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        i = i + 4
        lbl = ttk.Label(self, text = "PASSIVE ITEMS", font = MEDFONT)
        lbl.grid(row = i, column = 1, pady = 10)

        lbl = ttk.Label(self, text = "Name", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 0)
        lbl = ttk.Label(self, text = "Stack Type", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 1)
        lbl = ttk.Label(self, text = "Item Type", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 2)
        lbl = ttk.Label(self, text = "Stat Stack", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 3)
        lbl = ttk.Label(self, text = "Start Value", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 4)
        lbl = ttk.Label(self, text = "Value Gain", width = 20, font = BOLDMEDFONT, anchor = 'center')
        lbl.grid(row = i + 1, column = 5)

        i = i + 1
        curs.execute("SELECT * FROM PassiveItems")
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, width = 20, text = elem[j], anchor = 'center')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()


class View_Challenges(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Challenges", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        ### ADD COLUMN HEADERS ###
        lbl = ttk.Label(self, text = "Name", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Category", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Description", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Unlocks", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM Challenge")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, text = elem[j], anchor = 'center')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = 0, column = 4, padx = 10, pady = 10)

        my_connect.close()

class View_Skills(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Skills", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        ### ADD COLUMN HEADERS ###
        lbl = ttk.Label(self, text = "Survivor", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Name", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Type", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)
        lbl = ttk.Label(self, text = "Description", width = 15, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 4)
        lbl = ttk.Label(self, text = "Cooldown", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 5)
        lbl = ttk.Label(self, text = "Proc Coeff", width = 20, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 6)


        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM Skill")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, text = elem[j], anchor = 'center')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()

class View_Artifacts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Artifacts", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        lbl = ttk.Label(self, text = "Name", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Enviroment", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Description", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Unlock Pattern", width = 11, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM Artifact")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, text = elem[j], anchor = 'w')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()

class View_Monsters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Monsters", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        lbl = ttk.Label(self, text = "Name", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Health", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Regen", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Damage", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)
        lbl = ttk.Label(self, text = "Armor", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 4)
        lbl = ttk.Label(self, text = "Speed", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 5)
        lbl = ttk.Label(self, text = "Type", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 6)

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM Monster")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, text = elem[j], anchor = 'w')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()

class View_Runs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = ttk.Label(self, text = "View Run History", font = MEDFONT)
        lbl.grid(row = 0, column=1)

        lbl = ttk.Label(self, text = "Survivor", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 0)
        lbl = ttk.Label(self, text = "Hours", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 1)
        lbl = ttk.Label(self, text = "Minutes", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 2)
        lbl = ttk.Label(self, text = "Difficulty", width = 10, anchor = 'center', font = BOLDMEDFONT)
        lbl.grid(row = 1, column = 3)
        

        ### ESTABLISH CONNECTION TO DATABASE ###
        my_connect = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'password',
            database = 'ror2'
        )

        curs = my_connect.cursor()
        curs.execute("SELECT * FROM RunHistory")

        i = 2
        for elem in curs:
            for j in range(len(elem)):
                e = ttk.Label(self, text = elem[j], anchor = 'center')
                e.grid(row = i + 2, column = j)
                #e.insert(0, elem[j])
            i = i+1

        # button to show frame 3 with text layout3
        button2 = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))
        # putting the button in its place by using grid
        button2.grid(row = i + 2, column = 3, padx = 10, pady = 10)

        my_connect.close()

# window for the generate loadout function
class Generate_Loadout(tk.Frame):   
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        # Dictionary containing the recommended items for each survivor the user can select
        recitems = {
            "Acrid": ["Backup_Magazine", "Bison_Steak", "Energy_Drink", "Warbanner", "Topaz_Brooch", "Bandolier", "Death_Mark", "Leeching_Seed"],
            "Artificer": ["Bustling_Fungus", "Gasoline", "Focus_Crystal", "Personal_Shield_Generator", "Stun_Grenade", "Warbanner", "Death_Mark", "Old_War_Stealthkit"],
            "Bandit": ["Armor-Piercing_Rounds", "Backup_Magazine", "Energy_Drink", "Pauls_Goat_Hoof", "Predatory_Instincts", "Shattering_Justice", "Molten_Perforator"],
            "Captain": ["Bison_Steak", "Energy_Drink", "Monster_Tooth", "Repulsion_Armor_Plate", "Sticky_Bomb", "AtG_Missile_Mk_1", "Chronobauble", "Defensive_Microbots"],
            "Commando": ["Energy_Drink", "Pauls_Goat_Hoof", "Medkit", "Soldiers_Syringe", "Tri-Tip_Dagger", "Harvesters_Scythe", "Leeching_Seed", "Old_Guillotine"],
            "Engineer": ["Bustling_Fungus", "Cautious_Slug", "Crowbar", "Backup_Magazine", "Stun_Grenade", "Sticky_Bomb", "Infusion", "Squid_Polyp"],
            "Heretic": ["Backup_Magazine", "Bison_Steak", "Energy_Drink", "Warbanner", "Topaz_Brooch", "Razorwire", "Brainstalks", "Titanic_Knurl"],
            "Huntress": ["Lens-Makers_Glasses", "Crowbar", "Pauls_Goat_Hoof", "Hopoo_Feather", "Ukulele", "Will-o-the-wisp", "Brilliant_Behemoth"],
            "Loader": ["Energy_Drink", "Pauls_Goat_Hoof", "Energy_Drink", "Pauls_Goat_Hoof", "Focus_Crystal", "Predatory_Instincts", "Ceremonial_Dagger", "Molten_Perforator"],
            "Mercenary": ["Energy_Drink", "Pauls_Goat_Hoof", "Tri-Tip_Dagger", "Crowbar", "Focus_Crystal", "Hopoo_Feather", "Wax_Quail", "Unstable_Tesla_Coil"],
            "MUL-T": ["Gasoline", "Medkit", "Monster_Tooth", "Topaz_Brooch", "Rose_Buckler", "War_Horn", "Will-o-the-wisp", "Dios_Best_Friend"],
            "REX": ["Backup_Magazine", "Bison_Steak", "Energy_Drink", "Warbanner", "Topaz_Brooch", "Bandolier", "Death_Mark", "Leeching_Seed"]
        }
        
        label = ttk.Label(self, text ="Generate Loadout", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
  
        homebut = ttk.Button(self, text ="Home", command = lambda : controller.show_frame(StartPage))        
        homebut.grid(row = 3, column = 1, padx = 10, pady = 10)

        listlabel = ttk.Label(self, text = "Select a survivor", font = MEDFONT)
        listlabel.grid(row =1, column=0)

        # creating the listbox for the user to select which survivor they played as
        #survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        survivs_var = tk.StringVar(value=survivors)
        listbox = tk.Listbox(self, listvariable=survivs_var, height = 7, selectmode='single')
        listbox.grid(row = 2, column=0)


        # create inner frame for items to be displayed in
        itemlabel = ttk.Label(self, text = "Reccomended Items", font = MEDFONT)
        itemlabel.grid(row = 1, column=1)
        itemframe = tk.Frame(self, relief=tk.SUNKEN, borderwidth=3)
        itemframe.grid(row = 2, column=1)

        # generate reccomended items for selected survivor and display them in the itemframe
        def gen():
            survivor = listbox.get(ANCHOR)
            print(f"selected - {survivor}")
            itemlist = recitems[survivor]

            canvaslist = []
            #clear anything currently in the frame
            #destroy all the labels and pictures in the artifact frame
            for elem in itemframe.winfo_children():
                elem.destroy()

            #load pictures for items
            for i in range(len(itemlist)):
                temp = itemlist[i]
                canvas = tk.Canvas(itemframe, width=64, height=64)
                cwd = os.getcwd()
                img = ImageTk.PhotoImage(Image.open(os.path.join(cwd, f"ror2_database\pictures\items\{temp}.png")))
                canvas.create_image(0, 0, anchor = 'nw', image = img)
                canvas.image = img
                canvaslist.append(canvas)
                canvas.grid(row=0, column=i)

        # generate button that calls the generate player frames function
        gen_but = ttk.Button(self, text = "Generate", command= gen)
        gen_but.grid(row = 3, column= 0)

  
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
        #survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
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

            ### ESTABLISH CONNECTION TO DATABASE ###
            my_connect = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'password',
                database = 'ror2'
            )

            # add run data to table
            curs = my_connect.cursor()
            #cmnd = "INSERT INTO RunHistory (surv_name, hours, minutes, diff) VALUES (%s, %f, %f, %s)"
            #vals = (survivor, int(hours), int(minutes), difficulty)
            curs.execute(f"INSERT INTO RunHistory (surv_name, hours, minutes, diff) VALUES ('{survivor}', {hours}, {minutes}, '{difficulty}')")
            my_connect.commit()
            my_connect.close()


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
        #survivors = ["Acrid", "Artificer", "Bandit", "Captain", "Commando", "Engineer", "Heretic", "Huntress", "Loader", "Mercenary", "MUL-T", "REX"]
        artifacts = ["Chaos", "Command", "Death", "Dissonance", "Enigma", "Evolution", "Frailty", "Glass", "Honor", "Kin", "Metamorphosis", "Sacrifice", "Soul", "Spite", "Swarms", "Vengence"]

        gen_but = ttk.Button()
        label = ttk.Label(self, text ="Randomize Run", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        survivorframe = tk.Frame(self, relief = tk.SUNKEN, borderwidth=3)
        survlabel = ttk.Label(survivorframe, font = TINYFONT)
        
        artifactframe = tk.Frame(self, relief = tk.SUNKEN, borderwidth=3)
        num_of_artifacts = 0
        randarts = []
        artlabels = []

        difflabel = ttk.Label(self)

        def gen():
            #delete the generate button
            #gen_but.grid_forget()
            survivorframe.grid(row = 1, column = 0)
            artifactframe.grid(row = 1, column= 1)

            #destroy all the labels and pictures in the artifact frame
            for elem in artifactframe.winfo_children():
                elem.destroy()

            # GENERATE A RANDOM SURVIVOR
            randnum = random.randint(0, NUMBER_OF_SURVIVORS-1)
            surv = survivors[randnum]

            #load image of survivor
            canvas = tk.Canvas(survivorframe, width=128, height=128)
            img = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), f"ror2_database\pictures\survivors\{surv}.png")))
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
                img = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), f"ror2_database\pictures\\artifacts\{artname}.png")))
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
        gen_but = ttk.Button(self, text = "Generate", command= gen)
        gen_but.grid(row = 4, column= 2)

        # function called by the home button
        # clears the frame
        def close_page():            
            # replace the generate button
            #gen_but = ttk.Button(self, text = "GENERATE", command= gen)
            #gen_but.grid(row = 4, column= 2)
            
            #destroy all the labels and pictures in the artifact frame
            for elem in artifactframe.winfo_children():
                elem.destroy()
            
            survivorframe.grid_forget()
            artifactframe.grid_forget()
            difflabel.grid_forget()
            
            controller.show_frame(StartPage)

        # create home button to go back to the start page
        homebut = ttk.Button(self, text ="Home", command = close_page) 
        homebut.grid(row = 5, column = 2, padx = 10, pady = 10)


#driver code

#connect to sql database


app = application()
app.mainloop()