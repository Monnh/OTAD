# importerar Tkinter, PIL och MySQL Connector
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector


#funktioner
def clickButton():
     pass

def fetchMaskiner(self):

    chosen = LbDelagare.get(LbDelagare.curselection())
    chosen2 = str(chosen[0])
    selectedDelagare = "".join(chosen2)
    
    cursor.execute('SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Medlemsnummer = ' + selectedDelagare + ';')
    result = cursor.fetchall()
        
    if LbMaskiner.index("end") != 0:
        LbMaskiner.delete(0, "end")
        for x in result:
                LbMaskiner.insert("end", x)

    else:
        for x in result:
            LbMaskiner.insert("end", x)

# skapar en databasanslutning
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "sennaa66",
     database = "tschakt"
)
cursor = db.cursor()

# skapar och namnger fönster samt bestämmer storlek på fönstret
root = Tk()
root.title("T-schakts delägarregister")
root.geometry("950x900")
 
#skapar en variabel med en logga
photo1 = PhotoImage(file="c:/filer/python/t-schakt1.png")
Label (root, image=photo1) .grid (row=0, column=0)

#skapar textfält och textboxar
#Label (root, text =" Medlemsnummer ") .grid(row=1, column=0, sticky=W)
EntMedlemsnummer = Entry(root, width=20, text = "Medlemsnummer") 
EntMedlemsnummer.grid(row=1, column=1, sticky = "w", pady = 10)
EntMedlemsnummer.insert(0,"Medlemsnummer")
EntMedlemsnummer.bind("<FocusIn>", lambda args: EntMedlemsnummer.delete('0', 'end'))

BtnMedlemsnummerSok = Button(root, text = "Sök", width = 5, height = 1) 
BtnMedlemsnummerSok.grid (row = 1, column = 2, sticky ="w")

#Label (root, text =" Maskinnummer ") .grid(row=1, column=2, sticky=W)
EntMaskinnummer = Entry(root, width=20, text ="Maskinnummer") 
EntMaskinnummer.grid(row=1, column=3, sticky = "w")
EntMaskinnummer.insert(0, "Maskinnummer")
EntMaskinnummer.bind("<FocusIn>", lambda args: EntMaskinnummer.delete('0', 'end'))

#skapar en knapp
BtnMaskinnummerSok = Button (root, text="Sök", width=3, command=clickButton) 
BtnMaskinnummerSok.grid(row=1, column=4, sticky ="w")

BtnNyDelagare = Button (root, text ="Ny delägare", command = clickButton)
BtnNyDelagare.grid(row = 2, column = 5, padx= 10, sticky="n")

BtnRapport = Button (root, text = "Rapport", width = 9, command = clickButton)
BtnRapport.grid(row = 2, column =5)

BtnUppdateraForsakring = Button (root, text="Uppdatera försäkring", command = clickButton)
BtnUppdateraForsakring.grid(row = 4, column = 5)

BtnInstallningar = Button (root, text ="Inställningar", command = clickButton, width=16)
BtnInstallningar.grid(row = 5, column =5, pady=(8,0))

# skapar en listbox
LbDelagare = Listbox(root, width = 50)
LbDelagare.grid(row = 2, column = 1, columnspan = 2, rowspan = 2, padx=(0,10))
LbDelagare.bind('<<ListboxSelect>>', fetchMaskiner)

LbMaskiner = Listbox(root, width = 50)
LbMaskiner.grid(row = 2, column = 3, columnspan = 2, rowspan = 2)

# skapar en scrollbar
ScbDelagare = Scrollbar(root, orient="vertical")
ScbDelagare.grid(row = 2, column = 2, sticky = N+S+E, rowspan = 2)
ScbDelagare.config(command =LbDelagare.yview)

ScbDMaskiner = Scrollbar(root, orient="vertical")
ScbDMaskiner.grid(row = 2, column = 4, sticky = N+S+E, rowspan = 2)
ScbDMaskiner.config(command =LbMaskiner.yview)

LbDelagare.config(yscrollcommand=ScbDelagare.set)
LbMaskiner.config(yscrollcommand=ScbDMaskiner.set)

cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn FROM foretagsregister")
result = cursor.fetchall()

if LbDelagare.index("end") == 0:
     for x in result:
          LbDelagare.insert("end", x)

# kör fönstret
root.mainloop()