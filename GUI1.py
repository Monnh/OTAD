# importerar Tkinter, PIL och MySQL Connector
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
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

     nyDelagare.geometry("300x275")

     lblNyMedlemsnummer = Label(nyDelagare, text="Medlemsnr")
     lblNyMedlemsnummer.grid(row = 0, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyMedlemsnummer = Entry(nyDelagare, width = 5)
     entNyMedlemsnummer.grid(row = 0, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyForetag = Label(nyDelagare, text= "Företag")
     lblNyForetag.grid(row = 1, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyForetag = Entry(nyDelagare, width = 25)
     entNyForetag.grid(row = 1, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyFornamn = Label(nyDelagare, text= "Förnamn")
     lblNyFornamn.grid(row = 2, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyFornamn = Entry(nyDelagare, width = 25)
     entNyFornamn.grid(row = 2, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyEfternamn = Label(nyDelagare, text= "Efternamn")
     lblNyEfternamn.grid(row = 3, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyEfternamn = Entry(nyDelagare, width = 25)
     entNyEfternamn.grid(row = 3, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyGatuadress = Label(nyDelagare, text= "Gatuadress")
     lblNyGatuadress.grid(row = 4, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyGatuadress = Entry(nyDelagare, width = 25)
     entNyGatuadress.grid(row = 4, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyPostnummer = Label(nyDelagare, text= "Postnummer")
     lblNyPostnummer.grid(row = 5, column = 0, sticky = W, padx = (10, 0), pady=(7, 0))
     entNyPostnummer = Entry(nyDelagare, width = 25)
     entNyPostnummer.grid(row = 5, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyPostadress = Label(nyDelagare, text= "Postadress")
     lblNyPostadress.grid(row = 6, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyPostadress = Entry(nyDelagare, width = 25)
     entNyPostadress.grid(row = 6, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyTelefon = Label(nyDelagare, text= "Telefon")
     lblNyTelefon.grid(row = 7, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyTelefon = Entry(nyDelagare, width = 25)
     entNyTelefon.grid(row = 7, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     btnSpara = Button(nyDelagare, text="Spara")
     btnSpara.grid(row = 8, column = 1, sticky = W, pady = (10, 0), padx=(5,0))

     btnAvbryt = Button(nyDelagare, text="Avbryt")
     btnAvbryt.grid(row = 8, column = 1, pady = (10, 0), padx=(5,0))

def nyMaskin():
     
     nyMaskin = Toplevel(root)

     nyMaskin.title("Lägg till ny maskin")

     nyMaskin.geometry("950x680")

     lblMaskinnummermaskininfo = Label(nyMaskin, text= "Maskinnummer")
     lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(7,8))
     txtMaskinnummermaskininfo = Text(nyMaskin, width = 5, height=0.1)
     txtMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0), pady=(7,0))

     lblMaskinbeteckning = Label(nyMaskin, text="Beteckning")
     lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbeteckning = Text(nyMaskin, width = 20, height=0.1)
     txtMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))


     lblMaskinme_klass = Label(nyMaskin, text="ME-Klass")
     lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinme_klass = Text(nyMaskin, width = 20, height=0.1)
     txtMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))


     lblMaskinmotorfabrikat = Label(nyMaskin, text="Motorfabrikat")
     lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotorfabrikat = Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))


     lblMaskinmotortyp = Label(nyMaskin, text="Motortyp")
     lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotortyp=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))


     lblMaskinmotor = Label(nyMaskin, text="Motor")
     lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotor = Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))


     lblMaskinvaxellada = Label(nyMaskin, text="Växellåda")
     lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinvaxellada=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))


     lblMaskinhydraulsystem = Label(nyMaskin, text="Hydraulsystem")
     lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinhydraulsystem=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))


     lblMaskinkylvatska = Label(nyMaskin, text="Kylvätska")
     lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinkylvatska=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))


     lblMaskinmotoreffekt = Label(nyMaskin, text="Motoreffekt/KW")
     lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotoreffekt=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))

     lblMaskinmotorvarmare = Label(nyMaskin, text="Motorvärmare")
     lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinmotorvarmare=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotorvarmare.grid(column=1, row=10, sticky=W, padx=(10,0))

     lblMaskinkatalysator = Label(nyMaskin, text="Katalysator")
     lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinkatalysator=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinkatalysator.grid(column=1,row=11, sticky=W, padx=(10,0))

     lblMaskinpartikelfilter = Label(nyMaskin, text="Partikelfilter")
     lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinpartikelfilter=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinpartikelfilter.grid(column=1,row=12, sticky=W, padx=(10,0))

     lblMaskinvattenbaseradlack = Label(nyMaskin, text="Vattenbaserad lack")
     lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinvattenbaseradlack=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinvattenbaseradlack.grid(column=1, row=13, sticky=W, padx=(10,0))

     lblMaskinkylmedia = Label(nyMaskin, text="Kylmedia")
     lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinkylmedia=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))

     lblMaskinbullernivautv = Label(nyMaskin, text="Bullernivå utvändigt")
     lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbullernivautv=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))

     lblMaskinbullernivainv = Label(nyMaskin, text="Bullernivå invändigt")
     lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinbullernivainv=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))

     lblMaskinsmorjfett = Label(nyMaskin, text="Smörjfett")
     lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinsmorjfett=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))

     lblMaskinBatterityp = Label(nyMaskin, text="Batterityp")
     lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinBatterityp=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))

     #checkbox
     lblMaskinKollektivforsakring = Label(nyMaskin, text="Kollektiv försäkring")
     lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
     cbMaskinKollektivforsakring = Checkbutton(nyMaskin)
     cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

     lblMaskinperiod = Label(nyMaskin, text="Period")
     lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinperiod=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinperiod.grid(column=1, row=20, sticky=W, padx=(10,0))

     lblMaskinarsbelopp = Label(nyMaskin, text="Årsbelopp")
     lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
     txtMaskinarsbelopp=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))

     #Buttons

     btnSparaNyMaskin=Button(nyMaskin, text="Spara", command = lambda: nyMaskin())
     btnSparaNyMaskin.grid(column=5, row=21, sticky=E, padx=(0,55))
     btnAvbrytNyMaskin=Button(nyMaskin, text="Avbryt")
     btnAvbrytNyMaskin.grid(column=5, row=21,sticky=E)

     #--------------------

     lblMaskinmiljostatus = Label(nyMaskin, text="Miljöstatus")
     lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0), pady=(7,0))
     txtMaskinmiljostatus=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0), pady=(7,0))

     lblMaskinarsmodell = Label(nyMaskin, text="Årsmodell")
     lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
     txtMaskinarsmodell=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))

     lblMaskinregistreringsnummer = Label(nyMaskin, text="Reg. nr/Ser. nr")
     lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
     txtMaskinregistreringsnummer=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))

     lblMaskintyp = Label(nyMaskin, text="Maskintyp")
     lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
     txtMaskintyp=Text(nyMaskin, width = 20, height=0.1)
     txtMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))

     lblMaskinmotoroljevolym  = Label(nyMaskin, text="Motorolja volym/liter")
     lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
     txtMaskinmotoroljevolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))

     lblMaskinvaxelladevolym = Label(nyMaskin, text="Växellåda volym/liter")
     lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
     txtMaskinvaxelladevolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))

     lblMaskinhydraulsystemvolym = Label(nyMaskin, text="Hydraul volym/liter")
     lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
     txtMaskinhydraulsystemvolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))

     lblMaskinkylvatskavolym = Label(nyMaskin, text="Kylvätska volym/liter")
     lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
     txtMaskinkylvatskavolym=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))

     lblMaskinbild = Label(nyMaskin, text="Maskinbild")
     lblMaskinbild.grid(column=2, row=10, sticky = W, padx=(10,0))

     #------------------------

     lblMaskinbransle = Label(nyMaskin, text="Bränsle")
     lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0), pady=(7,0))
     txtMaskinbransle=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0), pady=(7,0))

     lblMaskindackfabrikat = Label(nyMaskin, text="Däckfabrikat")
     lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
     txtMaskindackfabrikat=Text(nyMaskin, width = 20, height=0.1)
     txtMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))

     lblMaskindimension = Label(nyMaskin, text="Dimension/typ")
     lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
     txtMaskindimension=Text(nyMaskin, width = 20, height=0.1)
     txtMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))

     #Checkbox
     lblMaskinregummerbara = Label(nyMaskin, text="Regummerbara")
     lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
     cbMaskinregummerbara = Checkbutton(nyMaskin)
     cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

     #Checkbox
     lblMaskinregummerade = Label(nyMaskin, text="Regummerade")
     lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
     cbMaskinregummerade = Checkbutton(nyMaskin)
     cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

     lblMaskingasolanlaggning = Label(nyMaskin, text="Gasolanläggning")
     lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
     txtMaskingasolanlaggning=Text(nyMaskin, width = 20, height=0.1)
     txtMaskingasolanlaggning.grid(column=5, row=5, sticky=W, padx=(10,0))

     lblMaskinSaneringsvatska = Label(nyMaskin, text="Saneringsväska")
     lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
     txtMaskinSaneringsvatska=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinSaneringsvatska.grid(column=5, row=6, sticky=W, padx=(10,0))

     #Checkbox
     lblMaskininsattserlagd = Label(nyMaskin, text="Maskininsats erlagd")
     lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
     cbMaskininsatserlagd = Checkbutton(nyMaskin)
     cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

     lblMaskinforare = Label(nyMaskin, text="Förare")
     lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
     txtMaskinforare=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))

     lblMaskinreferens = Label(nyMaskin, text="Referensjobb")
     lblMaskinreferens.grid(column=4, row=9, sticky = W, padx=(10,0))
     txtMaskinreferens=Text(nyMaskin, width = 20, height=0.1)
     txtMaskinreferens.grid(column=5, row=9, sticky=W, padx=(10,0))

     lblMaskintillbehor = Label(nyMaskin, text="Tillbehör")
     lblMaskintillbehor.grid(column=4, row=10, sticky = W, padx=(10,0))
     txtMaskintillbehor=Text(nyMaskin, width = 20, height=0.1)
     txtMaskintillbehor.grid(column=5, row=10, sticky=W, padx=(10,0))

     def addTillbehor():
     
          txt = txtMaskintillbehor.get('1.0','end')
          lbMaskintillbehor.insert('end',txt)
          txtMaskintillbehor.delete('1.0','end')
     

     lbMaskintillbehor = Listbox(nyMaskin)
     lbMaskintillbehor.grid(column=4, row=11, columnspan=2, rowspan=10, sticky=NSEW, padx=(10,0), pady=(5,5))
     #txtMaskintillbehor.bind('<Return>', lambda x=None: lbMaskintillbehor.insert('end', txtMaskintillbehor.get('1.0', 'end')), txtMaskintillbehor.delete('1.0','end'))
     txtMaskintillbehor.bind('<Return>', lambda x: (lbMaskintillbehor.insert('end', txtMaskintillbehor.get('1.0', 'end')), txtMaskintillbehor.delete('1.0','end')))
     #txtMaskintillbehor.bind('<Return>', lambda x=None: addTillbehor())
     
     

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
     password = "password",
     database = "tschakt"
)
cursor = db.cursor()

# skapar och namnger fönster samt bestämmer storlek på fönstret
root = Tk()
root.title("T-schakts delägarregister")
root.geometry("1280x750")
 
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

delagare.columnconfigure(1, weight=1)
delagare.rowconfigure(0, weight=1)

frameDelagare = Frame(delagare)
frameDelagare.grid(row = 0, column = 0, sticky = NW, padx=(10,0), pady=(10,0))
frameMaskiner= Frame(delagare)
frameMaskiner.grid(row = 1, column =0, sticky = NSEW, padx=(10,0), pady=(10,0))
frameMaskininfo = Frame(delagare)
frameMaskininfo.grid(row = 0, column =1, rowspan = 2, sticky = NSEW, pady=(10,0))
frameMaskininfo.grid_rowconfigure(0, weight=1)
frameMaskininfo.grid_columnconfigure(1, weight=1)


#Listbox, maskiner tillhörande delägare
LbDelagaresMaskiner = Listbox(frameMaskiner, width = 45, height = 25)
LbDelagaresMaskiner.grid(row = 0, column = 0)
LbDelagaresMaskiner.grid_rowconfigure(1, weight=1)
LbDelagaresMaskiner.grid_columnconfigure(0, weight=1)

#Delägareinfo

lblMedlemsnummer = Label(frameDelagare, text = "Medlemsnr.")
lblMedlemsnummer.grid(row = 1, column = 0, sticky=W, pady=(0,8))
txtMedlemsnummerDelagare = Text(frameDelagare, width = 5, height=0.1)
txtMedlemsnummerDelagare.grid(row = 1, column =1, sticky = W )

lblForetag = Label(frameDelagare, text = "Företag")
lblForetag.grid(row = 2, column = 0, sticky=W, pady=(0,8))
txtForetag = Text(frameDelagare, width = 25, height=0.1)
txtForetag.grid(row = 2, column =1, sticky = W)

lblFornamn = Label(frameDelagare, text = "Förnamn")
lblFornamn.grid(row = 3, column = 0, sticky=W, pady=(0,8))
txtFornamn = Text(frameDelagare, width = 25, height=0.1)
txtFornamn.grid(row = 3, column =1, sticky = W)

lblEfternamn = Label(frameDelagare, text = "Efternamn")
lblEfternamn.grid(row = 4, column = 0, sticky=W, pady=(0,8))
txtEfternamn = Text(frameDelagare, width = 25, height=0.1)
txtEfternamn.grid(row = 4, column =1, sticky = W)

lblAdress = Label(frameDelagare, text = "Adress")
lblAdress.grid(row = 5, column = 0, sticky=W, pady=(0,8))
txtAdress = Text(frameDelagare, width = 25, height=0.1)
txtAdress.grid(row = 5, column =1, sticky = W)

lblPostnummer = Label(frameDelagare, text = "Postnummer")
lblPostnummer.grid(row = 6, column = 0, sticky=W, pady=(0,8))
txtPostnummer = Text(frameDelagare, width = 25, height=0.1)
txtPostnummer.grid(row = 6, column =1, sticky = W)

lblPostadress = Label(frameDelagare, text = "Ort")
lblPostadress.grid(row = 7, column = 0, sticky=W, pady=(0,8))
txtPostadress = Text(frameDelagare, width = 25, height=0.1)
txtPostadress.grid(row = 7, column =1, sticky = W)

lblTelefon = Label(frameDelagare, text = "Telefon")
lblTelefon.grid(row = 8, column = 0, sticky=W, pady=(0,8))
txtTelefon = Text(frameDelagare, width = 25, height=0.1)
txtTelefon.grid(row = 8, column =1, sticky = W)

#Maskininfo

lblMaskinnummermaskininfo = Label(frameMaskininfo, text= "Maskinnummer")
lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinnummermaskininfo = Text(frameMaskininfo, width = 5, height=0.1)
txtMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0))

lblMaskinbeteckning = Label(frameMaskininfo, text="Beteckning")
lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbeteckning = Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))


lblMaskinme_klass = Label(frameMaskininfo, text="ME-Klass")
lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinme_klass = Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))


lblMaskinmotorfabrikat = Label(frameMaskininfo, text="Motorfabrikat")
lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotorfabrikat = Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))


lblMaskinmotortyp = Label(frameMaskininfo, text="Motortyp")
lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotortyp=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))


lblMaskinmotor = Label(frameMaskininfo, text="Motor")
lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotor = Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))


lblMaskinvaxellada = Label(frameMaskininfo, text="Växellåda")
lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinvaxellada=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))


lblMaskinhydraulsystem = Label(frameMaskininfo, text="Hydraulsystem")
lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinhydraulsystem=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))


lblMaskinkylvatska = Label(frameMaskininfo, text="Kylvätska")
lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinkylvatska=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))


lblMaskinmotoreffekt = Label(frameMaskininfo, text="Motoreffekt/KW")
lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotoreffekt=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))

lblMaskinmotorvarmare = Label(frameMaskininfo, text="Motorvärmare")
lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinmotorvarmare=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotorvarmare.grid(column=1, row=10, sticky=W, padx=(10,0))

lblMaskinkatalysator = Label(frameMaskininfo, text="Katalysator")
lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinkatalysator=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinkatalysator.grid(column=1,row=11, sticky=W, padx=(10,0))

lblMaskinpartikelfilter = Label(frameMaskininfo, text="Partikelfilter")
lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinpartikelfilter=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinpartikelfilter.grid(column=1,row=12, sticky=W, padx=(10,0))

lblMaskinvattenbaseradlack = Label(frameMaskininfo, text="Vattenbaserad lack")
lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinvattenbaseradlack=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinvattenbaseradlack.grid(column=1, row=13, sticky=W, padx=(10,0))

lblMaskinkylmedia = Label(frameMaskininfo, text="Kylmedia")
lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinkylmedia=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))

lblMaskinbullernivautv = Label(frameMaskininfo, text="Bullernivå utvändigt")
lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbullernivautv=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))

lblMaskinbullernivainv = Label(frameMaskininfo, text="Bullernivå invändigt")
lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinbullernivainv=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))

lblMaskinsmorjfett = Label(frameMaskininfo, text="Smörjfett")
lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinsmorjfett=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))

lblMaskinBatterityp = Label(frameMaskininfo, text="Batterityp")
lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinBatterityp=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))

#checkbox
lblMaskinKollektivforsakring = Label(frameMaskininfo, text="Kollektiv försäkring")
lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinKollektivforsakring = Checkbutton(frameMaskininfo)
cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

lblMaskinperiod = Label(frameMaskininfo, text="Period")
lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinperiod=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinperiod.grid(column=1, row=20, sticky=W, padx=(10,0))

lblMaskinarsbelopp = Label(frameMaskininfo, text="Årsbelopp")
lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
txtMaskinarsbelopp=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))

#Buttons

btnMaskinpresentation=Button(frameMaskininfo,text="Maskinpresentation")
btnMaskinpresentation.grid(column=0, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnMiljodeklaration=Button(frameMaskininfo, text="Miljödeklaration")
btnMiljodeklaration.grid(column=1, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnHistorik=Button(frameMaskininfo, text="Historik")
btnHistorik.grid(column=6, row=0, sticky=W, padx=(10,10))

btnLaggtillmaskin=Button(frameMaskininfo, text="Lägg till ny", command = lambda: nyMaskin())
btnLaggtillmaskin.grid(column=4, row=22, sticky=W, pady=(20,0))
btnAndramaskin=Button(frameMaskininfo, text="Ändra")
btnAndramaskin.grid(column=4, row=22,sticky=E, pady=(20,0))
btnBytmaskin=Button(frameMaskininfo, text="Byt maskin")
btnBytmaskin.grid(column=5, row=22, sticky=W, padx=(10,0), pady=(20,0))
btnTabortmaskin=Button(frameMaskininfo, text="Ta bort maskin")
btnTabortmaskin.grid(column=5, row=22, sticky=E, pady=(20,0))



#--------------------

lblMaskinmiljostatus = Label(frameMaskininfo, text="Miljöstatus")
lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0))
txtMaskinmiljostatus=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0))

lblMaskinarsmodell = Label(frameMaskininfo, text="Årsmodell")
lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
txtMaskinarsmodell=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))

lblMaskinregistreringsnummer = Label(frameMaskininfo, text="Reg. nr/Ser. nr")
lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
txtMaskinregistreringsnummer=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))

lblMaskintyp = Label(frameMaskininfo, text="Maskintyp")
lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
txtMaskintyp=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))

lblMaskinmotoroljevolym  = Label(frameMaskininfo, text="Motorolja volym/liter")
lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
txtMaskinmotoroljevolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))

lblMaskinvaxelladevolym = Label(frameMaskininfo, text="Växellåda volym/liter")
lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
txtMaskinvaxelladevolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))

lblMaskinhydraulsystemvolym = Label(frameMaskininfo, text="Hydraul volym/liter")
lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
txtMaskinhydraulsystemvolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))

lblMaskinkylvatskavolym = Label(frameMaskininfo, text="Kylvätska volym/liter")
lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
txtMaskinkylvatskavolym=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))

lblMaskinbild = Label(frameMaskininfo, text="Maskinbild")
lblMaskinbild.grid(column=2, row=10, sticky = W, padx=(10,0))
#Bild
img = Image.open("1.jpg")  
img = img.resize((295, 295), Image. ANTIALIAS)
img2 = ImageTk.PhotoImage(img)
img_label = Label(frameMaskininfo, image=img2)
img_label.grid(row=11, column=2, rowspan =10, columnspan =2, sticky = NW, padx=(10,0))

#------------------------

lblMaskinbransle = Label(frameMaskininfo, text="Bränsle")
lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0))
txtMaskinbransle=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0))

lblMaskindackfabrikat = Label(frameMaskininfo, text="Däckfabrikat")
lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
txtMaskindackfabrikat=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))

lblMaskindimension = Label(frameMaskininfo, text="Dimension/typ")
lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
txtMaskindimension=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))

#Checkbox
lblMaskinregummerbara = Label(frameMaskininfo, text="Regummerbara")
lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
cbMaskinregummerbara = Checkbutton(frameMaskininfo)
cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

#Checkbox
lblMaskinregummerade = Label(frameMaskininfo, text="Regummerade")
lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
cbMaskinregummerade = Checkbutton(frameMaskininfo)
cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

lblMaskingasolanlaggning = Label(frameMaskininfo, text="Gasolanläggning")
lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
txtMaskingasolanlaggning=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskingasolanlaggning.grid(column=5, row=5, sticky=W, padx=(10,0))

lblMaskinSaneringsvatska = Label(frameMaskininfo, text="Saneringsväska")
lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
txtMaskinSaneringsvatska=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinSaneringsvatska.grid(column=5, row=6, sticky=W, padx=(10,0))

#Checkbox
lblMaskininsattserlagd = Label(frameMaskininfo, text="Maskininsats erlagd")
lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
cbMaskininsatserlagd = Checkbutton(frameMaskininfo)
cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

lblMaskinforare = Label(frameMaskininfo, text="Förare")
lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
txtMaskinforare=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))

lblMaskinreferens = Label(frameMaskininfo, text="Referensjobb")
lblMaskinreferens.grid(column=4, row=9, sticky = W, padx=(10,0))
txtMaskinreferens=Text(frameMaskininfo, width = 20, height=0.1)
txtMaskinreferens.grid(column=5, row=9, sticky=W, padx=(10,0))

#Listbox
lblMaskintillbehor = Label(frameMaskininfo, text="Tillbehör")
lblMaskintillbehor.grid(column=4, row=10, sticky = W, padx=(10,0))
lbMaskintillbehor=Listbox(frameMaskininfo)
lbMaskintillbehor.grid(column=4, row=11, rowspan=11, columnspan=2,sticky=NSEW, padx=(10,0))




cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn FROM foretagsregister")
delagareLista = cursor.fetchall()

if LbDelagare.index("end") == 0:
     for x in delagareLista:
          LbDelagare.insert("end", x)

# kör fönstret
root.mainloop()