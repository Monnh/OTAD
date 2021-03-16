# importerar Tkinter, PIL och MySQL Connector
from tkinter import *
from tkinter import ttk
import PIL
import mysql.connector


#funktioner

def bytFlik():
     tabControl.select(delagare)

def clickButton():
     pass

def nyDelagare():
     
     nyDelagare = Toplevel(root)

     nyDelagare.title("Lägg till ny delägare")

     nyDelagare.geometry("300x215")

     lblNyMedlemsnummer = Label(nyDelagare, text="Medlemsnr")
     lblNyMedlemsnummer.grid(row = 0, column = 0, sticky = W, padx = (10, 0))
     entNyMedlemsnummer = Entry(nyDelagare, width = 5)
     entNyMedlemsnummer.grid(row = 0, column = 1, sticky = W, padx = (10, 0))

     lblNyForetag = Label(nyDelagare, text= "Företag")
     lblNyForetag.grid(row = 1, column = 0, sticky = W, padx = (10, 0))
     entNyForetag = Entry(nyDelagare, width = 25)
     entNyForetag.grid(row = 1, column = 1, sticky = W, padx = (10, 0))

     lblNyFornamn = Label(nyDelagare, text= "Förnamn")
     lblNyFornamn.grid(row = 2, column = 0, sticky = W, padx = (10, 0))
     entNyFornamn = Entry(nyDelagare, width = 25)
     entNyFornamn.grid(row = 2, column = 1, sticky = W, padx = (10, 0))

     lblNyEfternamn = Label(nyDelagare, text= "Efternamn")
     lblNyEfternamn.grid(row = 3, column = 0, sticky = W, padx = (10, 0))
     entNyEfternamn = Entry(nyDelagare, width = 25)
     entNyEfternamn.grid(row = 3, column = 1, sticky = W, padx = (10, 0))

     lblNyGatuadress = Label(nyDelagare, text= "Gatuadress")
     lblNyGatuadress.grid(row = 4, column = 0, sticky = W, padx = (10, 0))
     entNyGatuadress = Entry(nyDelagare, width = 25)
     entNyGatuadress.grid(row = 4, column = 1, sticky = W, padx = (10, 0))

     lblNyPostnummer = Label(nyDelagare, text= "Postnummer")
     lblNyPostnummer.grid(row = 5, column = 0, sticky = W, padx = (10, 0))
     entNyPostnummer = Entry(nyDelagare, width = 25)
     entNyPostnummer.grid(row = 5, column = 1, sticky = W, padx = (10, 0))

     lblNyPostadress = Label(nyDelagare, text= "Postadress")
     lblNyPostadress.grid(row = 6, column = 0, sticky = W, padx = (10, 0))
     entNyPostadress = Entry(nyDelagare, width = 25)
     entNyPostadress.grid(row = 6, column = 1, sticky = W, padx = (10, 0))

     lblNyTelefon = Label(nyDelagare, text= "Telefon")
     lblNyTelefon.grid(row = 7, column = 0, sticky = W, padx = (10, 0))
     entNyTelefon = Entry(nyDelagare, width = 25)
     entNyTelefon.grid(row = 7, column = 1, sticky = W, padx = (10, 0))

     btnSpara = Button(nyDelagare, text="Spara")
     btnSpara.grid(row = 8, column = 1, sticky = W, pady = (10, 0))

     btnAvbryt = Button(nyDelagare, text="Avbryt")
     btnAvbryt.grid(row = 8, column = 1, pady = (10, 0))


def fetchMaskiner(self):
     global medlemsnummer, delagarInfo

     selectedDelagare = LbDelagare.get(LbDelagare.curselection())
     stringSelectedDelagare = str(selectedDelagare[0])
     delagare = "".join(stringSelectedDelagare)
     medlemsnummer = delagare
     cursor.execute('SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Medlemsnummer = ' + delagare + ';')
     result = cursor.fetchall()
        
     if LbMaskiner.index("end") != 0:
          LbMaskiner.delete(0, "end")
          for x in result:
               LbMaskiner.insert("end", x)
     else:
          for x in result:
               LbMaskiner.insert("end", x)

     cursor.execute('SELECT medlemsnummer, foretagsnamn, fornamn, efternamn, gatuadress, postnummer, postadress, telefon FROM foretagsregister WHERE medlemsnummer = ' + medlemsnummer+ ';')
     delagarInfo = cursor.fetchone()
     delagarInfo = list(delagarInfo)
     print(delagarInfo[2])

     #sätter delägaresidans info

     txtMedlemsnummerDelagare.delete('1.0', 'end')
     txtMedlemsnummerDelagare.insert('end', delagarInfo[0])
     
     txtForetag.config(state=NORMAL)
     txtForetag.delete('1.0', 'end')
     txtForetag.insert('end', delagarInfo[1])
     txtForetag.config(state=DISABLED)

     txtFornamn.config(state=NORMAL)
     txtFornamn.delete('1.0', 'end')
     txtFornamn.insert('end', delagarInfo[2])
     txtFornamn.config(state=DISABLED)

     txtEfternamn.config(state=NORMAL)
     txtEfternamn.delete('1.0', 'end')
     txtEfternamn.insert('end', delagarInfo[3])
     txtEfternamn.config(state=DISABLED)

     txtAdress.config(state=NORMAL)
     txtAdress.delete('1.0', 'end')
     txtAdress.insert('end', delagarInfo[4])
     txtAdress.config(state=DISABLED)

     txtPostnummer.config(state=NORMAL)
     txtPostnummer.delete('1.0', 'end')
     txtPostnummer.insert('end', delagarInfo[5])
     txtPostnummer.config(state=DISABLED)

     txtPostadress.config(state=NORMAL)
     txtPostadress.delete('1.0', 'end')
     txtPostadress.insert('end', delagarInfo[6])
     txtPostadress.config(state=DISABLED)

     txtTelefon.config(state=NORMAL)
     txtTelefon.delete('1.0', 'end')
     txtTelefon.insert('end', delagarInfo[7])
     txtTelefon.config(state=DISABLED)




# skapar en databasanslutning
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "Not1but2",
     database = "tschakt"
)
cursor = db.cursor()

# skapar och namnger fönster samt bestämmer storlek på fönstret
root = Tk()
root.title("T-schakts delägarregister")
root.geometry("950x500")
 
#tabs?#

tabControl = ttk.Notebook(root)
home = ttk.Frame(tabControl)
delagare = ttk.Frame(tabControl)
tabControl.add(home, text='Home')
tabControl.add(delagare, text='Delägare')
tabControl.grid(column=0, row=0)

#variables

medlemsnummer = ""
maskinnummer = ""
delagarInfo = ""

#skapar textfält och textboxar
#Label (root, text =" Medlemsnummer ") .grid(row=1, column=0, sticky=W)
EntMedlemsnummer = Entry(home, width=20, text = "Medlemsnummer") 
EntMedlemsnummer.grid(row=1, column=1, sticky = "w", pady = 10)
EntMedlemsnummer.insert(0,"Medlemsnummer")
EntMedlemsnummer.bind("<FocusIn>", lambda args: EntMedlemsnummer.delete('0', 'end'))

BtnMedlemsnummerSok = Button(home, text = "Sök", width = 5, height = 1) 
BtnMedlemsnummerSok.grid (row = 1, column = 2, sticky ="w")

#Label (root, text =" Maskinnummer ") .grid(row=1, column=2, sticky=W)
EntMaskinnummer = Entry(home, width=20, text ="Maskinnummer") 
EntMaskinnummer.grid(row=1, column=3, sticky = "w")
EntMaskinnummer.insert(0, "Maskinnummer")
EntMaskinnummer.bind("<FocusIn>", lambda args: EntMaskinnummer.delete('0', 'end'))

#skapar en knapp
BtnMaskinnummerSok = Button (home, text="Sök", width=5, height = 1, command= lambda: bytFlik()) 
BtnMaskinnummerSok.grid(row=1, column=4, sticky ="w")

BtnNyDelagare = Button (home, text ="Ny delägare", command = lambda: nyDelagare())
BtnNyDelagare.grid(row = 2, column = 5, padx= 10, sticky="n")

BtnRapport = Button (home, text = "Rapport", width = 9, command = clickButton)
BtnRapport.grid(row = 2, column =5)

BtnUppdateraForsakring = Button (home, text="Uppdatera försäkring", command = clickButton)
BtnUppdateraForsakring.grid(row = 4, column = 5)

BtnInstallningar = Button (home, text ="Inställningar", width=16, command = clickButton)
BtnInstallningar.grid(row = 5, column =5, pady=(8,0))

# skapar en listbox
LbDelagare = Listbox(home, width = 50)
LbDelagare.grid(row = 2, column = 1, columnspan = 2, rowspan = 2, padx=(0,10))
LbDelagare.bind('<<ListboxSelect>>', fetchMaskiner)

LbMaskiner = Listbox(home, width = 50)
LbMaskiner.grid(row = 2, column = 3, columnspan = 2, rowspan = 2)

# skapar en scrollbar
ScbDelagare = Scrollbar(home, orient="vertical")
ScbDelagare.grid(row = 2, column = 2, sticky = N+S+E, rowspan = 2)
ScbDelagare.config(command =LbDelagare.yview)

ScbDMaskiner = Scrollbar(home, orient="vertical")
ScbDMaskiner.grid(row = 2, column = 4, sticky = N+S+E, rowspan = 2)
ScbDMaskiner.config(command =LbMaskiner.yview)

LbDelagare.config(yscrollcommand=ScbDelagare.set)
LbMaskiner.config(yscrollcommand=ScbDMaskiner.set)


#frames

#frameDelagare = Frame(delagare, height = 145, bg = "red")
#frameDelagare.grid(row = 2, column = 3)

#sida delägare

lblMedlemsnummer = Label(delagare, text = "Medlemsnr.")
lblMedlemsnummer.grid(row = 1, column = 0, sticky=W)
txtMedlemsnummerDelagare = Text(delagare, width = 5, height=0.1)
txtMedlemsnummerDelagare.grid(row = 1, column =1, sticky = W)

lblForetag = Label(delagare, text = "Företag")
lblForetag.grid(row = 2, column = 0, sticky=W)
txtForetag = Text(delagare, width = 25, height=0.1)
txtForetag.grid(row = 2, column =1, sticky = W)

lblFornamn = Label(delagare, text = "Förnamn")
lblFornamn.grid(row = 3, column = 0, sticky=W)
txtFornamn = Text(delagare, width = 25, height=0.1)
txtFornamn.grid(row = 3, column =1, sticky = W)

lblEfternamn = Label(delagare, text = "Efternamn")
lblEfternamn.grid(row = 4, column = 0, sticky=W)
txtEfternamn = Text(delagare, width = 25, height=0.1)
txtEfternamn.grid(row = 4, column =1, sticky = W)

lblAdress = Label(delagare, text = "Adress")
lblAdress.grid(row = 5, column = 0, sticky=W)
txtAdress = Text(delagare, width = 25, height=0.1)
txtAdress.grid(row = 5, column =1, sticky = W)

lblPostnummer = Label(delagare, text = "Postnummer")
lblPostnummer.grid(row = 6, column = 0, sticky=W)
txtPostnummer = Text(delagare, width = 25, height=0.1)
txtPostnummer.grid(row = 6, column =1, sticky = W)

lblPostadress = Label(delagare, text = "Ort")
lblPostadress.grid(row = 7, column = 0, sticky=W)
txtPostadress = Text(delagare, width = 25, height=0.1)
txtPostadress.grid(row = 7, column =1, sticky = W)

lblTelefon = Label(delagare, text = "Telefon")
lblTelefon.grid(row = 8, column = 0, sticky=W)
txtTelefon = Text(delagare, width = 25, height=0.1)
txtTelefon.grid(row = 8, column =1, sticky = W)


cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn FROM foretagsregister")
delagareLista = cursor.fetchall()

if LbDelagare.index("end") == 0:
     for x in delagareLista:
          LbDelagare.insert("end", x)

# kör fönstret
root.mainloop()