# importerar Tkinter, PIL och MySQL Connector
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk,Image
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PIL
import mysql.connector
from tkinter.simpledialog import askstring
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime,date
import os
import traceback


def clickButton():
     pass
#Funktion som skapar PDF-rapporten miljödeklaration
def miljodeklaration(maskinnummer):

     if len(maskinnummer) == 0:
          messagebox.showerror("Fel", "Ingen maskin är vald.")
     
     else:

          cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + str(maskinnummer) + ';')
          maskinInfo = cursor.fetchone()
          maskinInfo = list(maskinInfo)
          
          cursor.execute('SELECT Fornamn, Efternamn, Foretagsnamn, Gatuadress, Postnummer, Postadress FROM foretagsregister WHERE Medlemsnummer = ' + str(maskinInfo[4]) + ';')
          delagarInfoLista = cursor.fetchone()
          delagarInfoLista = list(delagarInfoLista)

          cursor.execute('SELECT forsakringsgivare FROM forsakringsgivare WHERE idforsakringsgivare = "1"')
          forsakring = cursor.fetchone()

          packet = io.BytesIO()
          c = canvas.Canvas(packet, pagesize=letter)

          for item in range(len(maskinInfo)):
               if maskinInfo[item] == None:
                    maskinInfo[item] = ""

          for item in range(len(delagarInfoLista)):
               if delagarInfoLista[item] == None:
                    delagarInfoLista[item] = ""

          #Översta delen
          c.drawString(130, 722, str(maskinInfo[4]))
          c.drawString(130, 702, str(delagarInfoLista[2]))
          c.drawString(130, 682, str(delagarInfoLista[0]))
          c.drawString(195, 682, str(delagarInfoLista[1]))
          c.drawString(130, 662, str(delagarInfoLista[3]))
          c.drawString(130, 642, str(delagarInfoLista[4]))
          c.drawString(190, 642, str(delagarInfoLista[5]))
          c.drawString(470, 722, str(maskinInfo[0]))
          c.drawString(458, 702, str(maskinInfo[1]))
          c.drawString(458, 682, str(maskinInfo[6]))
          c.drawString(458, 662, str(maskinInfo[26]))
          c.drawString(458, 642, str(maskinInfo[2]))
          c.drawString(458, 622, str(maskinInfo[27]))

          #Motor
          c.drawString(50, 540, str(maskinInfo[8]))
          c.drawString(160, 540, str(maskinInfo[9]))
          c.drawString(270, 540, str(maskinInfo[10]))

          #Eftermonterad avgasreninsutrustning
          if maskinInfo[14] == 1:
               c.drawString(50, 482, "Ja")
          elif maskinInfo[14] == 0:
               c.drawString(50, 482, "Nej")

          if maskinInfo[15] == 1:
               c.drawString(120, 482, "Ja")
          elif maskinInfo[15] == 0:
               c.drawString(120, 482, "Nej")

          if maskinInfo[12] == 1:
               c.drawString(195, 482, "Ja")
          elif maskinInfo[12] == 0:
               c.drawString(195, 482, "Nej")

          if maskinInfo[11] == 1:
               c.drawString(280, 482, "Ja")
          elif maskinInfo[11] == 0:
               c.drawString(280, 482, "Nej")


          #Bullernivå
          c.drawString(340, 482, str(maskinInfo[29]))
          c.drawString(430, 482, str(maskinInfo[31]))

          #Oljor och smörjmedel - Volym, liter
          c.drawString(50, 420, str(maskinInfo[16])) 
          c.drawString(205, 420, str(maskinInfo[17]))
          c.drawString(50, 390, str(maskinInfo[18]))
          c.drawString(205, 390, str(maskinInfo[19]))
          c.drawString(50, 360, str(maskinInfo[20]))
          c.drawString(205, 360, str(maskinInfo[21]))
          c.drawString(50, 325, str(maskinInfo[24]))

          #Miljöklassificering
          c.drawString(340, 420, str(maskinInfo[30]))
          if maskinInfo[22] == 1:
               c.drawString(345, 330, "Ja")
          elif maskinInfo[22] == 0:
               c.drawString(345, 330, "Nej")

          #Övrigt
          c.drawString(50, 244, str(maskinInfo[13]))
          if maskinInfo[37] == 1:
               c.drawString(125, 244, "Ja")
          elif maskinInfo[37] == 0:
               c.drawString(125, 244, "Nej")
          c.drawString(205, 244, str(maskinInfo[25]))
          if maskinInfo[35] == 1:
               c.drawString(375, 244, "Ja")
          elif maskinInfo[35] == 0:
               c.drawString(375, 244, "Nej")
          c.drawString(470, 210, str(maskinInfo[38]))
          c.drawString(50, 210, str(maskinInfo[33]))
          c.drawString(205, 210, str(maskinInfo[34]))
          if maskinInfo[36] == 1:
               c.drawString(375, 210, "Ja")
          elif maskinInfo[36] == 0:
               c.drawString(375, 210, "Nej") 
          c.drawString(470, 210, str(maskinInfo[39]))

          #Bränsle
          c.drawString(50, 155, str(maskinInfo[23]))

          #Försärking
          if maskinInfo[3] == 1:
               c.drawString(50, 102, forsakring[0])
          c.drawString(240, 102, str(maskinInfo[7]))
          if maskinInfo[7] != "":
               c.drawString(305, 102, "-")
          c.drawString(315, 102, str(maskinInfo[42]))

          #Datum
          c.drawString(435, 52, str(datetime.date(datetime.now())))

          c.save()

          packet.seek(0)
          new_pdf = PdfFileReader(packet)

          existing_pdf = PdfFileReader(open("PDFMallar/Miljödeklaration.pdf", "rb"))
          output = PdfFileWriter()

          page = existing_pdf.getPage(0)
          page.mergePage(new_pdf.getPage(0))
          output.addPage(page)

          outputStream = open( "Miljödeklaration - " + str(maskinnummer) + ".pdf", "wb")
          output.write(outputStream)
          outputStream.close()
          os.startfile("Miljödeklaration - " + str(maskinnummer) + ".pdf" )
#Funktion som skapar PDF-rapporten maskinpresentation
def maskinpresentation(maskinnummer):     

     if len(maskinnummer) == 0:
          messagebox.showerror("Fel", "Ingen maskin är vald.")
     
     else:

          cursor.execute('SELECT Medlemsnummer, MarkeModell, Arsmodell, Registreringsnummer, ME_Klass, Maskintyp, Forarid FROM maskinregister WHERE Maskinnummer = ' + maskinnummer + ';')
          maskinInfo = cursor.fetchone()
          maskinInfo = list(maskinInfo)

          cursor.execute('SELECT Foretagsnamn FROM foretagsregister WHERE medlemsnummer = ' + str(maskinInfo[0]) + ';')
          foretag = cursor.fetchone()
          foretag = list(foretag)

          cursor.execute('SELECT tillbehor FROM tillbehor WHERE Maskinnummer = ' + maskinnummer + ';')
          tillbehor = cursor.fetchall()
          tillbehor = list(tillbehor)

          cursor.execute('SELECT sokvag FROM bilder WHERE Maskinnummer = ' + maskinnummer + ' order by bildid desc LIMIT 1;')
          bild = cursor.fetchone()

          if maskinInfo[6] is not None:
               cursor.execute('select namn from forare where forarid = '+ str(maskinInfo[6])+';')
               forarnamn = cursor.fetchone()
               forarnamn = list(forarnamn)

               cursor.execute('SELECT Beskrivning FROM referens WHERE forarid = ' + str(maskinInfo[6]) + ';')
               referenser = cursor.fetchall()
               referenser = list(referenser)

          else:
               forarnamn = None
               referenser = None

          packet = io.BytesIO()
          c = canvas.Canvas(packet, pagesize=letter)
          rad1=""
          rad2=""
          rad3=""
          rad4=""
          rad5=""
          y=1

          if bild is not None:
               c.drawImage(bild[0], 72, 134, 450, 340)
          c.drawString(133, 710, str(maskinInfo[0])) 
          c.drawString(455, 690, str(maskinInfo[1]))
          c.drawString(455, 670, str(maskinInfo[2]))
          c.drawString(455, 650, str(maskinInfo[3]))
          c.drawString(455, 630, str(maskinInfo[4]))
          c.drawString(455, 610, str(maskinInfo[5]))
          if forarnamn is not None:
               c.drawString(133, 670, str(forarnamn[0]))
          c.drawString(133, 690, str(foretag[0]))
          c.drawString(467, 710, str(maskinnummer))
          
          counter = 0
          for x in tillbehor:
               counter +=1
               s = x[0]
               if(counter == len(tillbehor)):
                    s+=""
               else:
                    s+=", "
                    
               if y>12:
                    rad5+=s
               elif y>9:
                    y+=1
                    rad4+=s          
               elif y>6:
                    y+=1
                    rad3+=s
               elif y>3:
                    y+=1
                    rad2+=s
               else:
                    y+=1
                    rad1+=s      

          
          c.drawString(140, 558, str(rad1))
          c.drawString(140, 538, str(rad2))
          c.drawString(140, 518, str(rad3))
          c.drawString(140, 498, str(rad4))
          c.drawString(140, 478, str(rad5))
          if referenser is not None and len(referenser) != 0:
               c.drawString(152, 112, str(referenser[0][0]))
               c.drawString(152, 86, str(referenser[1][0]))

          c.save() 

          packet.seek(0)
          new_pdf = PdfFileReader(packet)

          existing_pdf = PdfFileReader(open("PDFMallar/Maskinpresentation.pdf", "rb"))
          output = PdfFileWriter()

          page = existing_pdf.getPage(0)
          page.mergePage(new_pdf.getPage(0))
          output.addPage(page)
          #Fixa i framtiden så att man kan använda sig av custom paths (till servern) för att spara dokumenten på andra ställen.
          outputStream = open( "Maskinpresentation - " + maskinnummer + ".pdf", "wb")
          output.write(outputStream)
          outputStream.close()
          #Öppnar dokumentet efter man skapat det. Måste ändra sökväg efter vi fixat servern.
          os.startfile("Maskinpresentation - " + maskinnummer + ".pdf" )
#Funktion som skapar PDF-rapporten maskininnehav
def maskininnehav(medlemsnummer):

     if len(medlemsnummer) == 0:
          messagebox.showerror("Fel", "Ingen delägare är vald.")
     
     else:
          cursor.execute("SELECT Maskinnummer, MarkeModell, ME_Klass, Maskininsats, Forsakring, Arsmodell, Registreringsnummer FROM maskinregister WHERE Medlemsnummer = " + medlemsnummer + "")
          maskiner = cursor.fetchall()
          maskiner = list(maskiner)

          cursor.execute("SELECT Foretagsnamn FROM foretagsregister WHERE Medlemsnummer = " + medlemsnummer + "")
          foretag = cursor.fetchone()
          
          packet = io.BytesIO()
          c = canvas.Canvas(packet, pagesize=letter)
          

          s = str(medlemsnummer)
          s+= "  -  " + foretag[0]

          #Delägare
          c.setFontSize(14)
          c.drawString(75, 650, s)

          #Maskiner
          y=590
          counter = 0
          pages = 1

          for i in maskiner:

               if counter < 21:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27
               
               elif counter == 21:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1

               elif counter > 21 and counter < 42:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27
               
               elif counter == 42:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1

               elif counter > 42 and counter < 63:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27

               elif counter == 63:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1

               elif counter > 63 and counter < 84:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27

               elif counter == 84:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1
               
               elif counter > 105 and counter < 126:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27

               elif counter == 126:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1

               elif counter > 126 and counter < 147:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27

               elif counter == 147:
                    if counter != len(maskiner):
                         c.showPage()
                         c.setFontSize(14)
                         c.drawString(75, 650, s)
                         y=590
                         pages += 1

               elif counter > 168 and counter < 189:
                    c.setFontSize(10)
                    c.drawString(77, y, str(i[0]))
                    if i[3] == 1:
                         c.drawString(131, y, str("Ja"))
                    elif i[3] == 0:
                         c.drawString(131, y, str("Nej"))
                    if i[4] == 1:
                         c.drawString(167, y, str("Ja"))
                    elif i[4] == 0:
                         c.drawString(167, y, str("Nej"))
                    if i[1] is not None:
                         c.drawString(215, y, str(i[1]))
                    if i[2] is not None:
                         c.drawString(340, y, str(i[2])) 
                    if i[5] is not None:
                         c.drawString(395, y, str(i[5]))
                    if i[6] is not None:
                         c.drawString(450, y, str(i[6]))
                    y-=27

               counter+=1

          c.save()
          packet.seek(0)
          new_pdf = PdfFileReader(packet)
          output = PdfFileWriter()

          for x in range(pages):
               existing_pdf = PdfFileReader(open("PDFMallar/Maskininnehav.pdf", "rb"))
               page = existing_pdf.getPage(0)
               page.mergePage(new_pdf.getPage(x))
               output.addPage(page)
               outputStream = open( "Maskininnehav - " + medlemsnummer + ".pdf", "wb")
               output.write(outputStream)
               outputStream.close()
          
          os.startfile("Maskininnehav - " + medlemsnummer + ".pdf" )
#Funktion som skapar PDF-rapporten försäkring per delägare (fråga)
def forsakringPerDelagareFraga(medlemsnummer):

     if len(medlemsnummer) == 0:
          messagebox.showerror("Fel", "Ingen delägare är vald.")
     
     else:

          cursor.execute("SELECT Maskinnummer, MarkeModell, Period_start, Period_slut, Arsbelopp, Registreringsnummer FROM maskinregister WHERE Medlemsnummer = " + medlemsnummer + " and Forsakring = '1'")
          maskiner = cursor.fetchall()
          maskiner = list(maskiner)

          cursor.execute("SELECT Foretagsnamn, Fornamn, Efternamn FROM foretagsregister WHERE Medlemsnummer = " + medlemsnummer + "")
          foretag = cursor.fetchone()

          cursor.execute("SELECT forsakringsgivare FROM forsakringsgivare WHERE idforsakringsgivare = 1")
          forsakringsgivare = cursor.fetchone()

          cursor.execute("SELECT MAX(Arsbelopp) FROM maskinregister WHERE Forsakring = '1'")
          arsbelopp = cursor.fetchone()

          packet = io.BytesIO()
          c = canvas.Canvas(packet, pagesize=letter)
          c.setFontSize(10)

          dPacket = io.BytesIO()
          d = canvas.Canvas(dPacket, pagesize=letter)
          d.setFontSize(10)

          #Datum
          c.drawString(490, 800, str(datetime.date(datetime.now())))

          #Företag
          c.setFontSize(12)
          c.drawString(40, 645, str(foretag[0]))
          if foretag[1] is not None:
               c.drawString(247, 645, str(foretag[1]))
          if foretag[1] is not None:
               c.drawString(348, 645, str(foretag[2]))
          c.drawString(510, 645, str(medlemsnummer))
          c.setFontSize(10)

          #Maskiner
          y=580
          dy=580
          counter = 0
          dCounter = 0
          belopp = 0
          dBelopp = 0
          pages = 1
          dPages = 0

          for i in maskiner:

               if i[4] == arsbelopp[0]:

                    if counter < 22: 
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         c.setFontSize(7)
                         c.drawString(140, y, str(i[2]))
                         c.drawString(174, y, " - ")
                         c.drawString(180, y, str(i[3]))
                         c.setFontSize(10)
                         c.drawString(240, y, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   c.drawString(285, y, str(i[1]))
                              else:
                                   c.drawString(300, y, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(i[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(i[5]))
                         c.drawString(530, y, str(i[4]))
                         y-=25

                    elif counter == 22:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.setFontSize(12)
                              c.drawString(40, 645, str(foretag[0]))
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(medlemsnummer))
                              c.setFontSize(10)
                              y = 580
                              pages += 1

                    elif counter > 22 and counter < 44:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         c.setFontSize(7)
                         c.drawString(140, y, str(i[2]))
                         c.drawString(174, y, " - ")
                         c.drawString(180, y, str(i[3]))
                         c.setFontSize(10)
                         c.drawString(240, y, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   c.drawString(285, y, str(i[1]))
                              else:
                                   c.drawString(300, y, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(i[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(i[5]))
                         c.drawString(530, y, str(i[4]))
                         y-=25

                    elif counter == 44:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.setFontSize(12)
                              c.drawString(40, 645, str(foretag[0]))
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(medlemsnummer))
                              c.setFontSize(10)
                              y = 580
                              pages += 1

                    elif counter > 44 and counter < 66:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         c.setFontSize(7)
                         c.drawString(140, y, str(i[2]))
                         c.drawString(174, y, " - ")
                         c.drawString(180, y, str(i[3]))
                         c.setFontSize(10)
                         c.drawString(240, y, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   c.drawString(285, y, str(i[1]))
                              else:
                                   c.drawString(300, y, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(i[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(i[5]))
                         c.drawString(530, y, str(i[4]))
                         y-=25

                    elif counter == 66:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.setFontSize(12)
                              c.drawString(40, 645, str(foretag[0]))
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(medlemsnummer))
                              c.setFontSize(10)
                              y = 580
                              pages += 1

                    elif counter > 66 and counter < 88:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         c.setFontSize(7)
                         c.drawString(140, y, str(i[2]))
                         c.drawString(174, y, " - ")
                         c.drawString(180, y, str(i[3]))
                         c.setFontSize(10)
                         c.drawString(240, y, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   c.drawString(285, y, str(i[1]))
                              else:
                                   c.drawString(300, y, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(i[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(i[5]))
                         c.drawString(530, y, str(i[4]))
                         y-=25
                         
                    elif counter == 88:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.setFontSize(12)
                              c.drawString(40, 645, str(foretag[0]))
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(medlemsnummer))
                              c.setFontSize(10)
                              y = 580
                              pages += 1

                    elif counter > 88 and counter < 110:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         c.setFontSize(7)
                         c.drawString(140, y, str(i[2]))
                         c.drawString(174, y, " - ")
                         c.drawString(180, y, str(i[3]))
                         c.setFontSize(10)
                         c.drawString(240, y, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   c.drawString(285, y, str(i[1]))
                              else:
                                   c.drawString(300, y, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(i[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(i[5]))
                         c.drawString(530, y, str(i[4]))
                         y-=25


                    belopp += i[4]
                    counter += 1
               
               else:

                    if dCounter < 22: 
                         d.drawString(71, dy, str(forsakringsgivare[0]))
                         d.setFontSize(7)
                         d.drawString(175, dy, str(i[2]))
                         d.drawString(209, dy, " - ")
                         d.drawString(215, dy, str(i[3]))
                         d.setFontSize(10)
                         d.drawString(265, dy, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   d.drawString(295, dy, str(i[1]))
                              else:
                                   d.drawString(310, dy, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   d.setFontSize(6)
                                   d.drawString(430, dy, str(i[5]))
                                   d.setFontSize(10)
                              else:
                                   d.drawString(430, dy, str(i[5]))
                         d.drawString(500, dy, str(i[4]))
                         dy-=25

                    elif dCounter == 22:
                         if dCounter != len(maskiner):
                              d.showPage()
                              d.setFontSize(10)
                              d.drawString(490, 820, str(datetime.date(datetime.now())))
                              d.drawString(71, 620, str(foretag[0]))
                              if foretag[1] is not None:
                                   d.drawString(270, 620, str(foretag[1]))
                              if foretag[1] is not None:
                                   d.drawString(348, 620, str(foretag[2]))
                              d.drawString(480, 620, str(medlemsnummer))
                              dy = 580
                              dPages += 1

                    elif dCounter > 22 and counter < 44:
                         d.drawString(71, dy, str(forsakringsgivare[0]))
                         d.setFontSize(7)
                         d.drawString(175, dy, str(i[2]))
                         d.drawString(209, dy, " - ")
                         d.drawString(215, dy, str(i[3]))
                         d.setFontSize(10)
                         d.drawString(265, dy, str(i[0]))
                         if i[1] is not None:
                              if len(i[1]) > 22:
                                   d.drawString(295, dy, str(i[1]))
                              else:
                                   d.drawString(310, dy, str(i[1]))
                         if i[5] is not None:
                              if len(i[5]) > 10:
                                   d.setFontSize(6)
                                   d.drawString(430, dy, str(i[5]))
                                   d.setFontSize(10)
                              else:
                                   d.drawString(430, dy, str(i[5]))
                         d.drawString(500, y, str(i[4]))
                         dy-=25

                    dBelopp += i[4]
                    dCounter += 1

          if dCounter > 0:
               
               d.drawString(490, 820, str(datetime.date(datetime.now())))
               d.drawString(71, 620, str(foretag[0]))
               if foretag[1] is not None:
                    d.drawString(270, 620, str(foretag[1]))
               if foretag[1] is not None:
                    d.drawString(348, 620, str(foretag[2]))
               d.drawString(480, 620, str(medlemsnummer))

               if counter + dCounter == len(maskiner):
                    if dCounter == 22:
                         dy-=2
                    else:
                         dy-=15
                    d.setFontSize(11)
                    d.drawString(460, dy, str("Total:"))
                    d.drawString(500, dy, str(dBelopp))
                    dy-=3
                    d.drawString(459, dy, "_____________")

          if counter + dCounter == len(maskiner):
               if counter == 22 or counter == 44 or counter == 66 or counter == 88 or counter == 110:
                    y-=4
               else:
                    y-=15
               c.setFontSize(11)
               c.drawString(460, y, str("Total:"))
               c.drawString(500, y, str(belopp))
               y-=3
               c.drawString(459, y, "_____________")

          c.save()
          d.save()
          packet.seek(0)
          dPacket.seek(0)
          new_pdf = PdfFileReader(packet)
          output = PdfFileWriter()

          andradeBelopp_pdf = PdfFileReader(dPacket)
          dOutput = PdfFileWriter()

          for x in range(pages):
               existing_pdf = PdfFileReader(open("PDFMallar/Kollektivförsäkring.pdf", "rb"))
               page = existing_pdf.getPage(0)
               page.mergePage(new_pdf.getPage(x))
               output.addPage(page)
               outputStream = open("Kollektivförsäkring - " + medlemsnummer + ".pdf", "wb")
               output.write(outputStream)
               outputStream.close()

          if dCounter > 0:
               if dPages > 0:
                    for x in range(dPages):
                         existing_pdf = PdfFileReader(open("PDFMallar/Kollektivförsäkring.pdf", "rb"))
                         page = existing_pdf.getPage(0)
                         page.mergePage(andradeBelopp_pdf.getPage(x))
                         dOutput.addPage(page)
                         outputStream = open("Kollektivförsäkring - ändrade belopp -  " + medlemsnummer + ".pdf", "wb")
                         dOutput.write(outputStream)
                         outputStream.close()
               else:
                    existing_pdf = PdfFileReader(open("PDFMallar/Kollektivförsäkring.pdf", "rb"))
                    page = existing_pdf.getPage(0)
                    page.mergePage(andradeBelopp_pdf.getPage(0))
                    dOutput.addPage(page)
                    outputStream = open("Kollektivförsäkring - ändrade belopp -  " + medlemsnummer + ".pdf", "wb")
                    dOutput.write(outputStream)
                    outputStream.close()
               os.startfile("Kollektivförsäkring - ändrade belopp -  " + medlemsnummer + ".pdf")


          os.startfile("Kollektivförsäkring - " + medlemsnummer + ".pdf" )
#Funktion som skapar PDF-rapporten försäkring per delägare
def forsakringPerDelagare():

     cursor.execute("SELECT Medlemsnummer FROM foretagsregister")
     medlemmar = cursor.fetchall()
     medlemmar = list(medlemmar)

     cursor.execute("SELECT forsakringsgivare FROM forsakringsgivare WHERE idforsakringsgivare = 1")
     forsakringsgivare = cursor.fetchone()
     
     cursor.execute("SELECT Maskinnummer FROM maskinregister where Forsakring = '1'")
     totaltMaskiner = cursor.fetchall()
     totaltMaskiner = list(totaltMaskiner)

     packet = io.BytesIO()
     c = canvas.Canvas(packet, pagesize=letter)
     c.setFontSize(10)
     totalCounter = 0
     pages = 0
     belopp = 0
     

     for i in medlemmar:
          cursor.execute("SELECT Maskinnummer, MarkeModell, Period_start, Period_slut, Arsbelopp, Registreringsnummer FROM maskinregister WHERE Medlemsnummer = " + str(i[0]) + " and Forsakring = '1';")
          maskiner = cursor.fetchall()
          maskiner = list(maskiner)

          cursor.execute("SELECT Foretagsnamn, Fornamn, Efternamn FROM foretagsregister WHERE Medlemsnummer = " + str(i[0]) + "")
          foretag = cursor.fetchone()

          counter = 0
          y=580


          if len(maskiner) != 0:
               c.setFontSize(10)
               c.drawString(490, 800, str(datetime.date(datetime.now())))
               c.drawString(40, 645, str(foretag[0]))
               c.setFontSize(12)
               if foretag[1] is not None:
                    c.drawString(247, 645, str(foretag[1]))
               if foretag[1] is not None:
                    c.drawString(348, 645, str(foretag[2]))
               c.drawString(510, 645, str(str(i[0])))
               c.setFontSize(10)
               pages+=1
          
          
               for n in maskiner:
                    
                    if n[4] is not None:
                         belopp += int(n[4])

                    if counter < 22: 
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         if n[2] is not None and n[3] is not None:
                              c.setFontSize(7)
                              c.drawString(140, y, str(n[2]))
                              c.drawString(174, y, " - ")
                              c.drawString(180, y, str(n[3]))
                              c.setFontSize(10)
                         c.drawString(240, y, str(n[0]))
                         if n[1] is not None:
                              if len(n[1]) > 22:
                                   c.drawString(285, y, str(n[1]))
                              else:
                                   c.drawString(300, y, str(n[1]))
                         if n[5] is not None:
                              if len(n[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(n[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(n[5]))
                         if n[4] is not None:
                              c.drawString(535, y, str(n[4]))
                         y-=25
                    elif counter == 22:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.drawString(40, 645, str(foretag[0]))
                              c.setFontSize(12)
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(str(i[0])))
                              c.setFontSize(10)
                              y = 580
                              pages += 1
                              c.drawString(40, y, str(forsakringsgivare[0]))
                              if n[2] is not None and n[3] is not None:
                                   c.setFontSize(7)
                                   c.drawString(140, y, str(n[2]))
                                   c.drawString(174, y, " - ")
                                   c.drawString(180, y, str(n[3]))
                                   c.setFontSize(10)
                              c.drawString(240, y, str(n[0]))
                              if n[1] is not None:
                                   if len(n[1]) > 22:
                                        c.drawString(285, y, str(n[1]))
                                   else:
                                        c.drawString(300, y, str(n[1]))
                              if n[5] is not None:
                                   if len(n[5]) > 10:
                                        c.setFontSize(8)
                                        c.drawString(430, y, str(n[5]))
                                        c.setFontSize(10)
                                   else:
                                        c.drawString(430, y, str(n[5]))
                              if n[4] is not None:
                                   c.drawString(535, y, str(n[4]))
                              y-=25
                    elif counter > 22 and counter < 44:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         if n[2] is not None and n[3] is not None:
                              c.setFontSize(7)
                              c.drawString(140, y, str(n[2]))
                              c.drawString(174, y, " - ")
                              c.drawString(180, y, str(n[3]))
                              c.setFontSize(10)
                         c.drawString(240, y, str(n[0]))
                         if n[1] is not None:
                              if len(n[1]) > 22:
                                   c.drawString(285, y, str(n[1]))
                              else:
                                   c.drawString(300, y, str(n[1]))
                         if n[5] is not None:
                              if len(n[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(n[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(n[5]))
                         if n[4] is not None:
                              c.drawString(535, y, str(n[4]))
                         y-=25
                    elif counter == 44:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.drawString(40, 645, str(foretag[0]))
                              c.setFontSize(12)
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(str(i[0])))
                              c.setFontSize(10)
                              y = 580
                              pages += 1
                              c.drawString(40, y, str(forsakringsgivare[0]))
                              if n[2] is not None and n[3] is not None:
                                   c.setFontSize(7)
                                   c.drawString(140, y, str(n[2]))
                                   c.drawString(174, y, " - ")
                                   c.drawString(180, y, str(n[3]))
                                   c.setFontSize(10)
                              c.drawString(240, y, str(n[0]))
                              if n[1] is not None:
                                   if len(n[1]) > 22:
                                        c.drawString(285, y, str(n[1]))
                                   else:
                                        c.drawString(300, y, str(n[1]))
                              if n[5] is not None:
                                   if len(n[5]) > 10:
                                        c.setFontSize(8)
                                        c.drawString(430, y, str(n[5]))
                                        c.setFontSize(10)
                                   else:
                                        c.drawString(430, y, str(n[5]))
                              if n[4] is not None:
                                   c.drawString(535, y, str(n[4]))
                              y-=25
                    elif counter > 44 and counter < 66:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         if n[2] is not None and n[3] is not None:
                              c.setFontSize(7)
                              c.drawString(140, y, str(n[2]))
                              c.drawString(174, y, " - ")
                              c.drawString(180, y, str(n[3]))
                              c.setFontSize(10)
                         c.drawString(240, y, str(n[0]))
                         if n[1] is not None:
                              if len(n[1]) > 22:
                                   c.drawString(285, y, str(n[1]))
                              else:
                                   c.drawString(300, y, str(n[1]))
                         if n[5] is not None:
                              if len(n[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(n[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(n[5]))
                         if n[4] is not None:
                              c.drawString(535, y, str(n[4]))
                         y-=25
                    elif counter == 66:
                         if counter != len(maskiner):
                              c.showPage()
                              c.setFontSize(10)
                              c.drawString(490, 800, str(datetime.date(datetime.now())))
                              c.drawString(40, 645, str(foretag[0]))
                              c.setFontSize(12)
                              if foretag[1] is not None:
                                   c.drawString(247, 645, str(foretag[1]))
                              if foretag[1] is not None:
                                   c.drawString(348, 645, str(foretag[2]))
                              c.drawString(510, 645, str(str(i[0])))
                              c.setFontSize(10)
                              y = 580
                              pages += 1
                              c.drawString(40, y, str(forsakringsgivare[0]))
                              if n[2] is not None and n[3] is not None:
                                   c.setFontSize(7)
                                   c.drawString(140, y, str(n[2]))
                                   c.drawString(174, y, " - ")
                                   c.drawString(180, y, str(n[3]))
                                   c.setFontSize(10)
                              c.drawString(240, y, str(n[0]))
                              if n[1] is not None:
                                   if len(n[1]) > 22:
                                        c.drawString(285, y, str(n[1]))
                                   else:
                                        c.drawString(300, y, str(n[1]))
                              if n[5] is not None:
                                   if len(n[5]) > 10:
                                        c.setFontSize(8)
                                        c.drawString(430, y, str(n[5]))
                                        c.setFontSize(10)
                                   else:
                                        c.drawString(430, y, str(n[5]))
                              if n[4] is not None:
                                   c.drawString(535, y, str(n[4]))
                              y-=25
                    elif counter > 66 and counter < 88:
                         c.drawString(40, y, str(forsakringsgivare[0]))
                         if n[2] is not None and n[3] is not None:
                              c.setFontSize(7)
                              c.drawString(140, y, str(n[2]))
                              c.drawString(174, y, " - ")
                              c.drawString(180, y, str(n[3]))
                              c.setFontSize(10)
                         c.drawString(240, y, str(n[0]))
                         if n[1] is not None:
                              if len(n[1]) > 22:
                                   c.drawString(285, y, str(n[1]))
                              else:
                                   c.drawString(300, y, str(n[1]))
                         if n[5] is not None:
                              if len(n[5]) > 10:
                                   c.setFontSize(8)
                                   c.drawString(430, y, str(n[5]))
                                   c.setFontSize(10)
                              else:
                                   c.drawString(430, y, str(n[5]))
                         if n[4] is not None:
                              c.drawString(535, y, str(n[4]))
                         y-=25     
                    

                    counter+=1
                    totalCounter+=1
                    if counter == len(maskiner):
                         c.showPage()

               if totalCounter == len(totaltMaskiner):
                    c.setFontSize(14)
                    c.drawString(150, 350, "Totalt: ")
                    c.drawString(195, 350, str(belopp))
                    pages+=1
                    c.save()
                    packet.seek(0)
                    new_pdf = PdfFileReader(packet)
                    output = PdfFileWriter()

                    for x in range(pages):
                         existing_pdf = PdfFileReader(open("PDFMallar/Kollektivförsäkring.pdf", "rb"))
                         page = existing_pdf.getPage(0)
                         page.mergePage(new_pdf.getPage(x))
                         output.addPage(page)
                         outputStream = open( "AllaFörsäkradeMaskiner.pdf", "wb")
                         output.write(outputStream)
                         outputStream.close()    
               
     os.startfile("AllaFörsäkradeMaskiner.pdf")
#Funktion som skapar PDF-rapporten maskiner med ändrade belopp
def maskinerMedAndradeBelopp():
     
     cursor.execute("SELECT MAX(Arsbelopp) FROM maskinregister WHERE Forsakring = '1'")
     arsbelopp = cursor.fetchone()

     cursor.execute("SELECT Maskinnummer, Forsakring, Arsbelopp, Period_start, Period_slut, Medlemsnummer FROM maskinregister WHERE Arsbelopp != '"+ str(arsbelopp[0]) +"' AND Arsbelopp > 0")
     maskiner = cursor.fetchall()
     maskiner = list(maskiner)

     packet = io.BytesIO()
     c = canvas.Canvas(packet, pagesize=letter)
     y=625
     counter = 0
     pages = 1

     c.drawString(490, 800, str(datetime.date(datetime.now())))

     for i in maskiner:

          if counter < 25: 
               c.drawString(60, y, str(i[0]))
               if i[1] == 0:
                    c.drawString(125, y, "Nej")
               elif i[1] == 1:
                    c.drawString(125, y, "Ja")
               c.drawString(190, y, str(i[2]))
               if i[3] is not None:
                    c.drawString(285, y, str(i[3]))
               if i[3] is not None:
                    c.drawString(349, y, "-")
                    c.drawString(360, y, str(i[4]))
               c.drawString(485, y, str(i[5]))
               y-=25
          elif counter == 25:
               if counter != len(maskiner):
                    c.showPage()
                    c.drawString(490, 800, str(datetime.date(datetime.now())))
                    y = 625
                    pages += 1
          elif counter > 26 and counter < 50:
               c.drawString(60, y, str(i[0]))
               if i[1] == 0:
                    c.drawString(125, y, "Nej")
               elif i[1] == 1:
                    c.drawString(125, y, "Ja")
               c.drawString(190, y, str(i[2]))
               if i[3] is not None:
                    c.drawString(285, y, str(i[3]))
               if i[3] is not None:
                    c.drawString(349, y, "-")
                    c.drawString(360, y, str(i[4]))
               c.drawString(485, y, str(i[5]))
               y-=25
          elif counter == 50:
               if counter != len(maskiner):
                    c.showPage()
                    c.drawString(490, 800, str(datetime.date(datetime.now())))
                    y = 625
                    pages += 1
          elif counter > 50 and counter < 75:
               c.drawString(60, y, str(i[0]))
               if i[1] == 0:
                    c.drawString(125, y, "Nej")
               elif i[1] == 1:
                    c.drawString(125, y, "Ja")
               c.drawString(190, y, str(i[2]))
               if i[3] is not None:
                    c.drawString(285, y, str(i[3]))
               if i[3] is not None:
                    c.drawString(349, y, "-")
                    c.drawString(360, y, str(i[4]))
               c.drawString(485, y, str(i[5]))
               y-=25

          counter += 1


     c.save()
     packet.seek(0)
     new_pdf = PdfFileReader(packet)
     output = PdfFileWriter()

     for x in range(pages):
               existing_pdf = PdfFileReader(open("PDFMallar/MaskinerÄndradeBelopp.pdf", "rb"))
               page = existing_pdf.getPage(0)
               page.mergePage(new_pdf.getPage(x))
               output.addPage(page)
               outputStream = open("Maskiner med ändrade årsbelopp.pdf", "wb")
               output.write(outputStream)
               outputStream.close()
     os.startfile("Maskiner med ändrade årsbelopp.pdf")
#Fyller delägarfönstret med maskinens data
def fyllMaskinInfo(self):
     global maskinnummer
     global medlemsnummer
     if self == "franDelagare":
          selectedMaskin = LbMaskiner.get(LbMaskiner.curselection())
          index2 = selectedMaskin.index(" ")
          stringSelectedMaskin = str(selectedMaskin[0:index2])
          maskinnummer = "".join(stringSelectedMaskin)
     elif self =="franMaskiner":
          maskinnummer = LbDelagaresMaskiner.get(LbDelagaresMaskiner.curselection())
          maskinnummer = maskinnummer[0]
          maskinnummer = str(maskinnummer) 
     elif self =="endastDelagare":
          LbDelagaresMaskiner.selection_set(0)
          maskinnummer = LbDelagaresMaskiner.get(LbDelagaresMaskiner.curselection())
          maskinnummer = maskinnummer[0]
          maskinnummer = str(maskinnummer) 
     cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + str(maskinnummer) + ';')
     maskinInfo = cursor.fetchone()
     maskinInfo = list(maskinInfo)
     medlemsnummer = str(maskinInfo[4])

     try:
          entMaskinBatteriantal.config(state=NORMAL)
          entMaskinBatteriantal.delete(0, 'end')
          entMaskinBatteriantal.insert(0, maskinInfo[39])
          entMaskinBatteriantal.config(state=DISABLED)
     except:
          entMaskinBatteriantal.config(state=DISABLED)

     try:
          entMaskinnummermaskininfo.config(state=NORMAL)
          entMaskinnummermaskininfo.delete(0, 'end')
          entMaskinnummermaskininfo.insert(0, maskinInfo[0])
          entMaskinnummermaskininfo.config(state=DISABLED)
     except:
          entMaskinnummermaskininfo.config(state=DISABLED)

     try:
          entMaskinbeteckning.config(state=NORMAL)
          entMaskinbeteckning.delete(0, 'end')
          entMaskinbeteckning.insert(0, maskinInfo[1])
          entMaskinbeteckning.config(state=DISABLED)
     except:
          entMaskinbeteckning.config(state=DISABLED)

     try:
          entMaskinme_klass.config(state=NORMAL)
          entMaskinme_klass.delete(0, 'end')
          entMaskinme_klass.insert(0, maskinInfo[2])
          entMaskinme_klass.config(state=DISABLED)
     except:
          entMaskinme_klass.config(state=DISABLED)
     
     try:
          entMaskinmotorfabrikat.config(state=NORMAL)
          entMaskinmotorfabrikat.delete(0, 'end')
          entMaskinmotorfabrikat.insert(0, maskinInfo[8])
          entMaskinmotorfabrikat.config(state=DISABLED)
     except:
          entMaskinmotorfabrikat.config(state=DISABLED)

     try:
          entMaskinmotortyp.config(state=NORMAL)
          entMaskinmotortyp.delete(0, 'end')
          entMaskinmotortyp.insert(0, maskinInfo[9])
          entMaskinmotortyp.config(state=DISABLED)
     except:
          entMaskinmotortyp.config(state=DISABLED)

     try:
          entMaskinmotor.config(state=NORMAL)
          entMaskinmotor.delete(0, 'end')
          entMaskinmotor.insert(0, maskinInfo[16])
          entMaskinmotor.config(state=DISABLED)
     except:
          entMaskinmotor.config(state=DISABLED)
     
     try:
          entMaskinvaxellada.config(state=NORMAL)
          entMaskinvaxellada.delete(0, 'end')
          entMaskinvaxellada.insert(0, maskinInfo[18])
          entMaskinvaxellada.config(state=DISABLED)
     except:
          entMaskinvaxellada.config(state=DISABLED)
     
     try:
          entMaskinhydraulsystem.config(state=NORMAL)
          entMaskinhydraulsystem.delete(0, 'end')
          entMaskinhydraulsystem.insert(0, maskinInfo[20])
          entMaskinhydraulsystem.config(state=DISABLED)
     except:
          entMaskinhydraulsystem.config(state=DISABLED)
     
     try:
          entMaskinkylvatska.config(state=NORMAL)
          entMaskinkylvatska.delete(0, 'end')
          entMaskinkylvatska.insert(0, maskinInfo[33])
          entMaskinkylvatska.config(state=DISABLED)
     except:
          entMaskinkylvatska.config(state=DISABLED)
     
     try:
          entMaskinmotoreffekt.config(state=NORMAL)
          entMaskinmotoreffekt.delete(0, 'end')
          entMaskinmotoreffekt.insert(0, maskinInfo[10])
          entMaskinmotoreffekt.config(state=DISABLED)
     except:
          entMaskinmotoreffekt.config(state=DISABLED)

     try:
          if maskinInfo[12] == 1:
               cbMaskinmotorvarmare.state(['selected'])
               cbMaskinmotorvarmare.state(['disabled'])
          else:
               cbMaskinmotorvarmare.state(['!selected'])
               cbMaskinmotorvarmare.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[14] == 1:
               cbMaskinkatalysator.state(['selected'])
               cbMaskinkatalysator.state(['disabled'])
          else:
               cbMaskinkatalysator.state(['!selected'])
               cbMaskinkatalysator.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[15] == 1:
               cbMaskinpartikelfilter.state(['selected'])
               cbMaskinpartikelfilter.state(['disabled'])
          else:
               cbMaskinpartikelfilter.state(['!selected'])
               cbMaskinpartikelfilter.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[11] == 1:
               cbMaskinvattenbaseradlack.state(['selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
          else:
               cbMaskinvattenbaseradlack.state(['!selected'])
               cbMaskinvattenbaseradlack.state(['disabled'])
     except:
          pass

     try:
          entMaskinkylmedia.config(state=NORMAL)
          entMaskinkylmedia.delete(0, 'end')
          entMaskinkylmedia.insert(0, maskinInfo[13])
          entMaskinkylmedia.config(state=DISABLED)
     except:
          entMaskinkylmedia.config(state=DISABLED)

     try:
          entMaskinbullernivautv.config(state=NORMAL)
          entMaskinbullernivautv.delete(0, 'end')
          entMaskinbullernivautv.insert(0, maskinInfo[29])
          entMaskinbullernivautv.config(state=DISABLED)
     except:
          entMaskinbullernivautv.config(state=DISABLED)

     try:
          entMaskinbullernivainv.config(state=NORMAL)
          entMaskinbullernivainv.delete(0, 'end')
          entMaskinbullernivainv.insert(0, maskinInfo[31])
          entMaskinbullernivainv.config(state=DISABLED)
     except:
          entMaskinbullernivainv.config(state=DISABLED)

     try:
          entMaskinsmorjfett.config(state=NORMAL)
          entMaskinsmorjfett.delete(0, 'end')
          entMaskinsmorjfett.insert(0, maskinInfo[24])
          entMaskinsmorjfett.config(state=DISABLED)
     except:
          entMaskinsmorjfett.config(state=DISABLED)
     
     try:
          entMaskinBatterityp.config(state=NORMAL)
          entMaskinBatterityp.delete(0, 'end')
          entMaskinBatterityp.insert(0, maskinInfo[38])
          entMaskinBatterityp.config(state=DISABLED)
     except:
          entMaskinBatterityp.config(state=DISABLED)

     deMaskinperiod1.delete(0, END)
     deMaskinperiod2.delete(0, END)

     if maskinInfo[7] is not None:
          try:
               deMaskinperiod1.set_date(maskinInfo[7])
               deMaskinperiod2.set_date(maskinInfo[42])
           
          except Exception:
               traceback.print_exc()

     try:
          entMaskinarsbelopp.config(state=NORMAL)
          entMaskinarsbelopp.delete(0, 'end')
          entMaskinarsbelopp.insert(0, maskinInfo[5])
          entMaskinarsbelopp.config(state=DISABLED)
     except:
          entMaskinarsbelopp.config(state=DISABLED)

     try:
          entMaskinmiljostatus.config(state=NORMAL)
          entMaskinmiljostatus.delete(0, 'end')
          entMaskinmiljostatus.insert(0, maskinInfo[30])
          entMaskinmiljostatus.config(state=DISABLED)
     except:
          entMaskinmiljostatus.config(state=DISABLED)

     try:
          entMaskinarsmodell.config(state=NORMAL)
          entMaskinarsmodell.delete(0, 'end')
          entMaskinarsmodell.insert(0, maskinInfo[6])
          entMaskinarsmodell.config(state=DISABLED)
     except:
          entMaskinarsmodell.config(state=DISABLED)

     try:
          entMaskinregistreringsnummer.config(state=NORMAL)
          entMaskinregistreringsnummer.delete(0, 'end')
          entMaskinregistreringsnummer.insert(0, maskinInfo[26])
          entMaskinregistreringsnummer.config(state=DISABLED)
     except:
          entMaskinregistreringsnummer.config(state=DISABLED)

     try:
          entMaskintyp.config(state=NORMAL)
          entMaskintyp.delete(0, 'end')
          entMaskintyp.insert(0, maskinInfo[27])
          entMaskintyp.config(state=DISABLED)
     except:
          entMaskintyp.config(state=DISABLED)

     try:
          entMaskinmotoroljevolym.config(state=NORMAL)
          entMaskinmotoroljevolym.delete(0, 'end')
          entMaskinmotoroljevolym.insert(0, maskinInfo[17])
          entMaskinmotoroljevolym.config(state=DISABLED)
     except:
          entMaskinmotoroljevolym.config(state=DISABLED)

     try:
          entMaskinvaxelladevolym.config(state=NORMAL)
          entMaskinvaxelladevolym.delete(0, 'end')
          entMaskinvaxelladevolym.insert(0, maskinInfo[19])
          entMaskinvaxelladevolym.config(state=DISABLED)
     except:
          entMaskinvaxelladevolym.config(state=DISABLED)

     try:
          entMaskinhydraulsystemvolym.config(state=NORMAL)
          entMaskinhydraulsystemvolym.delete(0, 'end')
          entMaskinhydraulsystemvolym.insert(0, maskinInfo[21])
          entMaskinhydraulsystemvolym.config(state=DISABLED)
     except:
          entMaskinhydraulsystemvolym.config(state=DISABLED)

     try:
          entMaskinkylvatskavolym.config(state=NORMAL)
          entMaskinkylvatskavolym.delete(0, 'end')
          entMaskinkylvatskavolym.insert(0, maskinInfo[32])
          entMaskinkylvatskavolym.config(state=DISABLED)
     except:
          entMaskinkylvatskavolym.config(state=DISABLED)

     try:
          TxtOvrigtext.config(state=NORMAL)
          TxtOvrigtext.delete(1.0, 'end')
          TxtOvrigtext.insert(END, maskinInfo[41])
          TxtOvrigtext.config(state=DISABLED)
     except Exception:
          TxtOvrigtext.config(state=DISABLED)

     try:
          entMaskinbransle.config(state=NORMAL)
          entMaskinbransle.delete(0, 'end')
          entMaskinbransle.insert(0, maskinInfo[23])
          entMaskinbransle.config(state=DISABLED)
     except:
          entMaskinbransle.config(state=DISABLED)

     try:
          entMaskindackfabrikat.config(state=NORMAL)
          entMaskindackfabrikat.delete(0, 'end')
          entMaskindackfabrikat.insert(0, maskinInfo[25])
          entMaskindackfabrikat.config(state=DISABLED)
     except:
          entMaskindackfabrikat.config(state=DISABLED)

     try:
          entMaskindimension.config(state=NORMAL)
          entMaskindimension.delete(0, 'end')
          entMaskindimension.insert(0, maskinInfo[34])
          entMaskindimension.config(state=DISABLED)
     except:
          entMaskindimension.config(state=DISABLED)

     try:
          if maskinInfo[37] == 1:
               cbMaskingasolanlaggning.state(['selected'])
               cbMaskingasolanlaggning.state(['disabled'])
          else:
               cbMaskingasolanlaggning.state(['!selected'])
               cbMaskingasolanlaggning.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[22] == 1:
               cbMaskinSaneringsvatska.state(['selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
          else:
               cbMaskinSaneringsvatska.state(['!selected'])
               cbMaskinSaneringsvatska.state(['disabled'])
     except:
          pass

     forarnamn=""
     if maskinInfo[40] != None:
          cursor.execute('SELECT Namn FROM forare WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          forarnamn = cursor.fetchone()

     try:
          entMaskinforare.config(state=NORMAL)
          entMaskinforare.delete(0, 'end')
          entMaskinforare.insert(0, forarnamn[0])
          entMaskinforare.config(state=DISABLED)
     except:
          entMaskinforare.config(state=DISABLED)
     
     referenser = []     
     referenser.clear()
     if maskinInfo[40] != None:
          cursor.execute('SELECT Beskrivning FROM referens WHERE Forarid = ' + str(maskinInfo[40]) + ';')
          referenser = cursor.fetchall()
          
     try:
          lbMaskinreferens.config(state=NORMAL)
          if lbMaskinreferens.index("end") != 0:
               lbMaskinreferens.delete(0, "end")
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
          else:
               for x in referenser:
                    lbMaskinreferens.insert("end", x[0])
          lbMaskinreferens.config(state=DISABLED)
     except:
          lbMaskinreferens.config(state=DISABLED)

     try:
          if maskinInfo[28] == 1:
               cbMaskininsatserlagd.state(['selected'])
               cbMaskininsatserlagd.state(['disabled'])
          else:
               cbMaskininsatserlagd.state(['!selected'])
               cbMaskininsatserlagd.state(['disabled'])
     except:
          pass
     
     try:
          if maskinInfo[36] == 1:
               cbMaskinregummerade.state(['selected'])
               cbMaskinregummerade.state(['disabled'])
          else:
               cbMaskinregummerade.state(['!selected'])
               cbMaskinregummerade.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[35] == 1:
               cbMaskinregummerbara.state(['selected'])
               cbMaskinregummerbara.state(['disabled'])
          else:
               cbMaskinregummerbara.state(['!selected'])
               cbMaskinregummerbara.state(['disabled'])
     except:
          pass

     try:
          if maskinInfo[3] == 1:
               cbMaskinKollektivforsakring.state(['selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
          else:
               cbMaskinKollektivforsakring.state(['!selected'])
               cbMaskinKollektivforsakring.state(['disabled'])
     except:
          pass
     #Hämtar bilden kopplad till maskinen, om detta inte går används en placeholder.
     try:
          cursor.execute("SELECT Sokvag FROM bilder WHERE Maskinnummer = " + str(maskinnummer) + " order by bildid desc LIMIT 1;")
          img = cursor.fetchone()
          img = Image.open(img[0])  
          img = img.resize((225,200), Image. ANTIALIAS)
          img2 = ImageTk.PhotoImage(img)
          img_label.config(image = img2)
          img_label.image=img2
     except Exception:
          img = Image.open("1.jpg")  
          img = img.resize((225,200), Image. ANTIALIAS)
          img2 = ImageTk.PhotoImage(img)
          img_label.config(image = img2)
          img_label.image=img2
          #traceback.print_exc()

     cursor.execute('SELECT Tillbehor FROM tillbehor WHERE Maskinnummer = ' + str(maskinnummer) + ';')
     tillbehor = cursor.fetchall()
     
     if lbMaskintillbehor.index("end") != 0:
          lbMaskintillbehor.delete(0, "end")
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     else:
          for x in tillbehor:
               lbMaskintillbehor.insert("end", x[0])
     if self == "franDelagare":
          cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
          maskiner = cursor.fetchall()

          if LbDelagaresMaskiner.index("end") != 0:
               LbDelagaresMaskiner.delete(0, "end")
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)
          else:
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)    
     
          fyllDelagarInfo(medlemsnummer)
     tabControl.select(delagare)
#Funktion för att ägga till nya delägare och ändra information på befintliga delägare 
def laggTillAndraDelagare(Typ):
     global medlemsnummer

     if Typ == "Ändra":
          titel = "Ändra befintlig delägare"
     elif Typ == "Ny":
          titel = "Lägg till ny delägare"
     
     def spara(Typ):
          global medlemsnummer
          
          if Typ == "Ändra":              
               if len(entNyForetag.get()) == 0:
                    messagebox.showerror("Fel", "Delägaren måste ha ett företagsnamn.")
                    nyDelagare.lift() 
               else:
                    cursor.execute("UPDATE foretagsregister SET Foretagsnamn = '" + entNyForetag.get() + "', Fornamn = '" + entNyFornamn.get() + "', Efternamn = '" + entNyEfternamn.get() + "', Gatuadress = '" + entNyGatuadress.get() + "', Postnummer = '" + entNyPostnummer.get() + "', Postadress = '" + entNyPostadress.get() + "', Telefon = '" + entNyTelefon.get() + "' WHERE Medlemsnummer = " + medlemsnummer +";")
                    db.commit()
                    fyllDelagarInfo(medlemsnummer)
                    nyDelagare.destroy()
                    tabControl.select(delagare)
                    fyllListboxDelagare()

          elif Typ == "Ny":
               cursor.execute("SELECT Medlemsnummer FROM foretagsregister")
               upptagnaMedlemsnummer = cursor.fetchall()
               upptagnaMedlemsnummer = list(upptagnaMedlemsnummer)
               upptaget = False

               if len(entNyMedlemsnummer.get()) == 0:
                    messagebox.showerror("Fel", "Delägaren måste ha ett medlemsnummer.")
                    nyDelagare.lift()
               elif len(entNyForetag.get()) == 0:
                    messagebox.showerror("Fel", "Delägaren måste ha ett företagsnamn.")
                    nyDelagare.lift()
               else:
                    for i in upptagnaMedlemsnummer:
                         if i[0] == int(entNyMedlemsnummer.get()):
                              upptaget = True
                              break
                    if upptaget == False:
                         cursor.execute("INSERT INTO foretagsregister (Medlemsnummer, Foretagsnamn, Fornamn, Efternamn, Gatuadress, Postnummer, Postadress, Telefon) VALUES ('" + entNyMedlemsnummer.get() + "', '" + entNyForetag.get() + "', '" + entNyFornamn.get() + "', '" + entNyEfternamn.get() + "', '" + entNyGatuadress.get() + "', '" + entNyPostnummer.get() + "', '" + entNyPostadress.get() + "', '" + entNyTelefon.get() + "');")
                         db.commit()
                         medlemsnummer = entNyMedlemsnummer.get()
                         nyDelagare.destroy()
                         tomDelagareInfo()
                         tomMaskinInfo()
                         fyllDelagarInfo(medlemsnummer)
                         tabControl.select(delagare)
                         fyllListboxDelagare()
                    else:
                         messagebox.showerror("Fel", "Medlemsnumret är upptaget, välj ett annat.")
                         nyDelagare.lift()

     nyDelagare = Toplevel(root)

     nyDelagare.title(titel)

     nyDelagare.geometry("300x275")

     lblNyMedlemsnummer = Label(nyDelagare, text="Medlemsnr")
     lblNyMedlemsnummer.grid(row = 0, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyMedlemsnummer = Entry(nyDelagare, width = 5, validate="key", validatecommand=(validera, "%P"))
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
     entNyPostnummer = Entry(nyDelagare, width = 25, validate="key", validatecommand=(validera, "%P"))
     entNyPostnummer.grid(row = 5, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyPostadress = Label(nyDelagare, text= "Postadress")
     lblNyPostadress.grid(row = 6, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyPostadress = Entry(nyDelagare, width = 25)
     entNyPostadress.grid(row = 6, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     lblNyTelefon = Label(nyDelagare, text= "Telefon")
     lblNyTelefon.grid(row = 7, column = 0, sticky = W, padx = (10, 0), pady=(7,0))
     entNyTelefon = Entry(nyDelagare, width = 25)
     entNyTelefon.grid(row = 7, column = 1, sticky = W, padx = (10, 0), pady=(7,0))

     btnSparaNyDelagare = Button(nyDelagare, text="Spara", command = lambda: spara(Typ))
     btnSparaNyDelagare.grid(row = 8, column = 1, sticky = W, pady = (10, 0), padx=(5,0))

     btnAvbrytNyDelagare = Button(nyDelagare, text="Avbryt", command = lambda: nyDelagare.destroy())
     btnAvbrytNyDelagare.grid(row = 8, column = 1, pady = (10, 0), padx=(5,0))

     if Typ == "Ändra" and len(medlemsnummer) == 0:
          nyDelagare.destroy()
          messagebox.showerror("Fel", "Välj en delägare att ändra.")

     elif Typ == "Ändra":
          cursor.execute('SELECT * FROM foretagsregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
          delagarInformation = cursor.fetchone()
          delagarInformation = list(delagarInformation)

          try:
               entNyMedlemsnummer.insert('end', medlemsnummer)
               entNyMedlemsnummer.config(state = 'disabled')
          except:
               pass

          try:
               entNyForetag.insert('end', delagarInformation[1])
          except:
               pass

          try:
               entNyFornamn.insert('end', delagarInformation[6])
          except:
               pass

          try:
               entNyEfternamn.insert('end', delagarInformation[7])
          except:
               pass

          try:
               entNyGatuadress.insert('end', delagarInformation[2])
          except:
               pass

          try:
               entNyPostnummer.insert('end', delagarInformation[3])
          except:
               pass

          try:
               entNyPostadress.insert('end', delagarInformation[4])
          except:
               pass

          try:
               entNyTelefon.insert('end', delagarInformation[5])
          except:
               pass
#Funktion för att ta bort delägare
def taBortDelagare():
     global medlemsnummer

     if len(medlemsnummer) == 0:
          messagebox.showerror("Fel", "Ingen delägare är vald.")
     else:
          response = messagebox.askyesno("Varning!", "Är du säker på att du vill ta bort delägare nr. " + medlemsnummer + "? \nDetta tar även bort alla maskiner på detta medlemsnummer.")
          if response == 1:
               cursor.execute("DELETE FROM maskinregister WHERE Medlemsnummer = " + medlemsnummer + ";")
               cursor.execute("DELETE FROM foretagsregister WHERE Medlemsnummer = " + medlemsnummer + ";" )
               db.commit()
               medlemsnummer = ""
               tomMaskinInfo()
               tomDelagareInfo()
               fyllListboxDelagare()

          else:
               pass
#Skapar ett nytt fönster där man kan Lägga till ny maskin, ändra maskin eller byta maskin.
def nyMaskinFonster(Typ, entrymaskinnummer, entrymedlemsnummer):

     if len(entrymedlemsnummer) == 1:
          messagebox.showerror(title="Ej valt delägare/maskin", message="Du måste välja en delägare och/eller en maskin innan du kan Lägga till ny/ändra/byta." )
     elif Typ =="Byt" and len (entrymaskinnummer) ==0:
          messagebox.showerror(title="Ej valt maskin.", message="Du måste välja en maskin för att kunna byta.")
     elif len(Typ)==0 and len(entrymaskinnummer) == 0:
          messagebox.showerror(title="Ej valt maskin", message ="Du måste välja en maskin för att kunna ändra den.")

     else:
          global filePath
          
               #Bestämmer vilka funktioner som borde köras baserat på om man vill ändra/byta/lägga till                 
          def sparaMaskin(Typ):
               global maskinnummer 

               if Typ=="Byt":
                    response = messagebox.askyesno("Varning!", "Vill du byta maskin med maskinnummer " + str(maskinnummer) + "? \nTidigare data sparas som historik.")
                    nyMaskin.lift()
                    if response == 1:
                         try:                        
                              andraMaskin(maskinnummer, True)
                              sparaHistorik(maskinnummer) 
                              db.commit()
                              fileSave()
                              maskinnummer = entNyMaskinnummermaskininfo.get()                       
                              fyllMaskinInfo("empty")
                              nyMaskin.destroy()
                         except Exception:
                              db.rollback()
                              traceback.print_exc()
                    else:
                         pass
               elif Typ=="Ny":
                    try:
                         bytOchNyMaskin()
                         print("nyMaskin Ny")
                         db.commit()
                         fileSave()
                         fyllMaskinInfo("empty")
                         hamtaDelagarensMaskiner()                                  
                         nyMaskin.destroy()
                    except Exception:
                         db.rollback()
                         nyMaskin.lift()
                         traceback.print_exc()
                    
               else:
                    print("nyMaskin Ändra")
                    try:
                         andraMaskin(Typ, False)
                         db.commit()
                         fileSave()
                         fyllMaskinInfo("empty")
                         nyMaskin.destroy()
                    except Exception:
                         db.rollback()
                         traceback.print_exc()
                         print("Kunde inte ändra maskin")


     
          #Insertar en ny maskin i databasen
          def bytOchNyMaskin():
               global maskinnummer

               varCbMotorvarmare = cbMaskinmotorvarmare.instate(['selected'])
               varCbKatalysator = cbMaskinkatalysator.instate(['selected'])
               varCbPartikelfilter = cbMaskinpartikelfilter.instate(['selected'])
               varCbVattenbaseradlack = cbMaskinvattenbaseradlack.instate(['selected'])
               varCbKollektivForsakring = cbMaskinKollektivforsakring.instate(['selected'])
               varCbRegummerbara = cbMaskinregummerbara.instate(['selected'])
               varCbRegummerade = cbMaskinregummerade.instate(['selected'])
               varCbGasolanlaggning = cbMaskingasolanlaggning.instate(['selected'])
               varCbSaneringsvatska = cbMaskinSaneringsvatska.instate(['selected'])
               varCbMaskininsatserlagd = cbMaskininsatserlagd.instate(['selected'])

               
               if cbMaskinnummer.instate(['selected']) == True:
                    try:
                         if len(deMaskinperiod1.get()) == 0 or len(deMaskinperiod2.get()) == 0:
                              cursor.execute("INSERT INTO maskinregister (MarkeModell, ME_Klass, Forsakring, Medlemsnummer, Arsbelopp, Arsmodell, Motorfabrikat, Motortyp, Motoreffekt, Vattenbaseradlack, Motorvarmare, Kylmedia, Katalysator, Partikelfilter, Motorolja, Motorvolymolja, Vaxelladsolja, Vaxelladavolym, Hydraulolja, Hydraulvolym, Saneringsvatska, Bransle, Smorjfett, Dackfabrikat, Registreringsnummer, Maskintyp, Maskininsats, Bullernivaute, Miljostatus, Bullernivainne, Kylvatskavolym, Kylvatska, Dimension, Regummerbar, Regummerad, Gasol, Batterityp, Batteriantal, Ovrig_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (entMaskinbeteckning.get(), entMaskinme_klass.get(), varCbKollektivForsakring, medlemsnummer, entMaskinarsbelopp.get(), entMaskinarsmodell.get(), entMaskinmotorfabrikat.get(), entMaskinmotortyp.get(), entMaskinmotoreffekt.get(), varCbVattenbaseradlack, varCbMotorvarmare, entMaskinkylmedia.get(), varCbKatalysator, varCbPartikelfilter, entMaskinmotor.get(), entMaskinmotoroljevolym.get(), entMaskinvaxellada.get(), entMaskinvaxelladevolym.get(), entMaskinhydraulsystem.get(), entMaskinhydraulsystemvolym.get(), varCbSaneringsvatska, entMaskinbransle.get(), entMaskinsmorjfett.get(), entMaskindackfabrikat.get(), entMaskinregistreringsnummer.get(), entMaskintyp.get(), varCbMaskininsatserlagd, entMaskinbullernivautv.get(), entMaskinmiljostatus.get(), entMaskinbullernivainv.get(), entMaskinkylvatskavolym.get(), entMaskinkylvatska.get(), entMaskindimension.get(), varCbRegummerbara, varCbRegummerade, varCbGasolanlaggning, entMaskinBatterityp.get(), entMaskinbatteriAntal.get(), TxtOvrigtext.get('1.0','end')))
                              maskinnummer=cursor.lastrowid
                         else:
                              cursor.execute("INSERT INTO maskinregister (MarkeModell, ME_Klass, Forsakring, Medlemsnummer, Arsbelopp, Arsmodell, Period_start, Motorfabrikat, Motortyp, Motoreffekt, Vattenbaseradlack, Motorvarmare, Kylmedia, Katalysator, Partikelfilter, Motorolja, Motorvolymolja, Vaxelladsolja, Vaxelladavolym, Hydraulolja, Hydraulvolym, Saneringsvatska, Bransle, Smorjfett, Dackfabrikat, Registreringsnummer, Maskintyp, Maskininsats, Bullernivaute, Miljostatus, Bullernivainne, Kylvatskavolym, Kylvatska, Dimension, Regummerbar, Regummerad, Gasol, Batterityp, Batteriantal, Ovrig_text, Period_slut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (entMaskinbeteckning.get(), entMaskinme_klass.get(), varCbKollektivForsakring, medlemsnummer, entMaskinarsbelopp.get(), entMaskinarsmodell.get(), deMaskinperiod1.get_date().strftime('%Y-%m-%d'), entMaskinmotorfabrikat.get(), entMaskinmotortyp.get(), entMaskinmotoreffekt.get(), varCbVattenbaseradlack, varCbMotorvarmare, entMaskinkylmedia.get(), varCbKatalysator, varCbPartikelfilter, entMaskinmotor.get(), entMaskinmotoroljevolym.get(), entMaskinvaxellada.get(), entMaskinvaxelladevolym.get(), entMaskinhydraulsystem.get(), entMaskinhydraulsystemvolym.get(), varCbSaneringsvatska, entMaskinbransle.get(), entMaskinsmorjfett.get(), entMaskindackfabrikat.get(), entMaskinregistreringsnummer.get(), entMaskintyp.get(), varCbMaskininsatserlagd, entMaskinbullernivautv.get(), entMaskinmiljostatus.get(), entMaskinbullernivainv.get(), entMaskinkylvatskavolym.get(), entMaskinkylvatska.get(), entMaskindimension.get(), varCbRegummerbara, varCbRegummerade, varCbGasolanlaggning, entMaskinBatterityp.get(), entMaskinbatteriAntal.get(), TxtOvrigtext.get('1.0','end'), deMaskinperiod2.get_date().strftime('%Y-%m-%d')))
                              maskinnummer=cursor.lastrowid
                    except Exception:
                         traceback.print_exc()
                    for x in tillbehorAttLaggaTill:
                         cursor.execute("INSERT INTO tillbehor (Tillbehor, Maskinnummer) values ('" + x + "', " + str(maskinnummer) + ");" )
                    if filePath is not None:                        
                         cursor.execute("insert into bilder (sokvag, maskinnummer) values ('pics/"+str(maskinnummer)+filePath+"', '"+str(maskinnummer)+"');")
                         

               else:
                    maskinnummerFinns = False
                    valtMaskinNummer = entNyMaskinnummermaskininfo.get()
                    cursor.execute('SELECT Maskinnummer FROM maskinregister')
                    result = cursor.fetchall()

                    for x in result:
                         if valtMaskinNummer== str(x[0]):
                              maskinnummerFinns = True
                              break
                         else:
                              pass
                    #Kollar om maskinnummret existerar sedan innan.
                    if maskinnummerFinns == False:
                         try:
                              maskinnummer = valtMaskinNummer
                              if len(deMaskinperiod1.get()) == 0 or len(deMaskinperiod2.get()) == 0:
                                   cursor.execute("INSERT INTO maskinregister (Maskinnummer, MarkeModell, ME_Klass, Forsakring, Medlemsnummer, Arsbelopp, Arsmodell, Motorfabrikat, Motortyp, Motoreffekt, Vattenbaseradlack, Motorvarmare, Kylmedia, Katalysator, Partikelfilter, Motorolja, Motorvolymolja, Vaxelladsolja, Vaxelladavolym, Hydraulolja, Hydraulvolym, Saneringsvatska, Bransle, Smorjfett, Dackfabrikat, Registreringsnummer, Maskintyp, Maskininsats, Bullernivaute, Miljostatus, Bullernivainne, Kylvatskavolym, Kylvatska, Dimension, Regummerbar, Regummerad, Gasol, Batterityp, Batteriantal, Ovrig_text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (entNyMaskinnummermaskininfo.get(), entMaskinbeteckning.get(), entMaskinme_klass.get(), varCbKollektivForsakring, medlemsnummer, entMaskinarsbelopp.get(), entMaskinarsmodell.get(), entMaskinmotorfabrikat.get(), entMaskinmotortyp.get(), entMaskinmotoreffekt.get(), varCbVattenbaseradlack, varCbMotorvarmare, entMaskinkylmedia.get(), varCbKatalysator, varCbPartikelfilter, entMaskinmotor.get(), entMaskinmotoroljevolym.get(), entMaskinvaxellada.get(), entMaskinvaxelladevolym.get(), entMaskinhydraulsystem.get(), entMaskinhydraulsystemvolym.get(), varCbSaneringsvatska, entMaskinbransle.get(), entMaskinsmorjfett.get(), entMaskindackfabrikat.get(), entMaskinregistreringsnummer.get(), entMaskintyp.get(), varCbMaskininsatserlagd, entMaskinbullernivautv.get(), entMaskinmiljostatus.get(), entMaskinbullernivainv.get(), entMaskinkylvatskavolym.get(), entMaskinkylvatska.get(), entMaskindimension.get(), varCbRegummerbara, varCbRegummerade, varCbGasolanlaggning, entMaskinBatterityp.get(), entMaskinbatteriAntal.get(), TxtOvrigtext.get('1.0','end')))
                              else:
                                   cursor.execute("INSERT INTO maskinregister (Maskinnummer, MarkeModell, ME_Klass, Forsakring, Medlemsnummer, Arsbelopp, Arsmodell, Period_start, Motorfabrikat, Motortyp, Motoreffekt, Vattenbaseradlack, Motorvarmare, Kylmedia, Katalysator, Partikelfilter, Motorolja, Motorvolymolja, Vaxelladsolja, Vaxelladavolym, Hydraulolja, Hydraulvolym, Saneringsvatska, Bransle, Smorjfett, Dackfabrikat, Registreringsnummer, Maskintyp, Maskininsats, Bullernivaute, Miljostatus, Bullernivainne, Kylvatskavolym, Kylvatska, Dimension, Regummerbar, Regummerad, Gasol, Batterityp, Batteriantal, Ovrig_text, Period_slut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (entNyMaskinnummermaskininfo.get(), entMaskinbeteckning.get(), entMaskinme_klass.get(), varCbKollektivForsakring, medlemsnummer, entMaskinarsbelopp.get(), entMaskinarsmodell.get(), deMaskinperiod1.get_date().strftime('%Y-%m-%d'), entMaskinmotorfabrikat.get(), entMaskinmotortyp.get(), entMaskinmotoreffekt.get(), varCbVattenbaseradlack, varCbMotorvarmare, entMaskinkylmedia.get(), varCbKatalysator, varCbPartikelfilter, entMaskinmotor.get(), entMaskinmotoroljevolym.get(), entMaskinvaxellada.get(), entMaskinvaxelladevolym.get(), entMaskinhydraulsystem.get(), entMaskinhydraulsystemvolym.get(), varCbSaneringsvatska, entMaskinbransle.get(), entMaskinsmorjfett.get(), entMaskindackfabrikat.get(), entMaskinregistreringsnummer.get(), entMaskintyp.get(), varCbMaskininsatserlagd, entMaskinbullernivautv.get(), entMaskinmiljostatus.get(), entMaskinbullernivainv.get(), entMaskinkylvatskavolym.get(), entMaskinkylvatska.get(), entMaskindimension.get(), varCbRegummerbara, varCbRegummerade, varCbGasolanlaggning, entMaskinBatterityp.get(), entMaskinbatteriAntal.get(), TxtOvrigtext.get('1.0','end'), deMaskinperiod2.get_date().strftime('%Y-%m-%d')))
                         except Exception:
                              traceback.print_exc()                              
                         for x in tillbehorAttLaggaTill:
                              print(x)
                              cursor.execute("INSERT INTO tillbehor (Tillbehor, Maskinnummer) values ('" + x + "', " + entNyMaskinnummermaskininfo.get() + ");")
                         if filePath is not None:
                              try:
                                   cursor.execute("insert into bilder (sokvag, maskinnummer) values ('pics/"+str(maskinnummer)+filePath+"', '"+str(maskinnummer)+"');")
                              except:
                                   pass
                    else:
                         messagebox.showerror(title="Upptaget", message="Maskinnumret är upptaget, var god välj ett.")
                         raise ValueError("Inkorrekt")
                    


          #Ändrar maskin baserat på de nya inputsen/entrys.
          def andraMaskin(Typ, byteTillbehor):
               global filePath
               if byteTillbehor is True:
                    cursor.execute("Delete from tillbehor where maskinnummer ="+Typ+";")
                    cursor.execute("Delete from bilder where maskinnummer ="+Typ+";")


               if cbMaskinregummerbara.instate(['selected']) == True:                    
                    cursor.execute("UPDATE maskinregister SET regummerbar = 1 WHERE Maskinnummer = " + Typ +";")                   
               else:                   
                    cursor.execute("UPDATE maskinregister SET regummerbar = 0 WHERE Maskinnummer = " + Typ +";")
                    
               
               if cbMaskinregummerade.instate(['selected']) == True:                   
                    cursor.execute("UPDATE maskinregister SET regummerad = 1 WHERE Maskinnummer = " + Typ +";")                
               else:                   
                    cursor.execute("UPDATE maskinregister SET regummerad = 0 WHERE Maskinnummer = " + Typ +";")           
               if cbMaskinKollektivforsakring.instate(['selected']) == True:                 
                    cursor.execute("UPDATE maskinregister SET Forsakring = 1 WHERE Maskinnummer = " + Typ +";")            
               else:             
                    cursor.execute("UPDATE maskinregister SET Forsakring = 0 WHERE Maskinnummer = " + Typ +";")      
               if cbMaskininsatserlagd.instate(['selected']) == True:              
                    cursor.execute("UPDATE maskinregister SET Maskininsats = 1 WHERE Maskinnummer = " + Typ +";")      
               else:               
                    cursor.execute("UPDATE maskinregister SET Maskininsats = 0 WHERE Maskinnummer = " + Typ +";")
               if cbMaskinmotorvarmare.instate(['selected']) == True:              
                    cursor.execute("UPDATE maskinregister SET Motorvarmare = 1 WHERE Maskinnummer = " + Typ +";")         
               else:            
                    cursor.execute("UPDATE maskinregister SET Motorvarmare = 0 WHERE Maskinnummer = " + Typ +";")
                    

               if cbMaskinkatalysator.instate(['selected']) == True:   
                    cursor.execute("UPDATE maskinregister SET Katalysator = 1 WHERE Maskinnummer = " + Typ +";")
                    
               else:
                         cursor.execute("UPDATE maskinregister SET Katalysator = 0 WHERE Maskinnummer = " + Typ +";")
                    

               if cbMaskinpartikelfilter.instate(['selected']) == True:
                    
                    cursor.execute("UPDATE maskinregister SET Partikelfilter = 1 WHERE Maskinnummer = " + Typ +";")
                    
               else:
                    
                    cursor.execute("UPDATE maskinregister SET Partikelfilter = 0 WHERE Maskinnummer = " + Typ +";")
                    

               if cbMaskinvattenbaseradlack.instate(['selected']) == True:
                    
                    cursor.execute("UPDATE maskinregister SET Vattenbaseradlack = 1 WHERE Maskinnummer = " + Typ +";")
                    
               else:
                    
                    cursor.execute("UPDATE maskinregister SET Vattenbaseradlack = 0 WHERE Maskinnummer = " + Typ +";")
                    

               if cbMaskingasolanlaggning.instate(['selected']) == True:
                    
                    cursor.execute("UPDATE maskinregister SET Gasol = 1 WHERE Maskinnummer = " + Typ +";")
                    
               else:
                    
                    cursor.execute("UPDATE maskinregister SET Gasol = 0 WHERE Maskinnummer = " + Typ +";")
                    

               if cbMaskinSaneringsvatska.instate(['selected']) == True:             
                    cursor.execute("UPDATE maskinregister SET Saneringsvatska = 1 WHERE Maskinnummer = " + Typ +";")
                    
               else:              
                    cursor.execute("UPDATE maskinregister SET Saneringsvatska = 0 WHERE Maskinnummer = " + Typ +";")
               cursor.execute("UPDATE maskinregister SET Maskinnummer = '" + entNyMaskinnummermaskininfo.get() + "', MarkeModell = '" + entMaskinbeteckning.get() + "', ME_Klass = '" + entMaskinme_klass.get() + "', Motorfabrikat = '" + entMaskinmotorfabrikat.get() + "', Motortyp = '" + entMaskinmotortyp.get() + "', Motorolja = '" + entMaskinmotor.get() + "', Vaxelladsolja = '" + entMaskinvaxellada.get() + "', Hydraulolja = '" + entMaskinhydraulsystem.get() + "', Kylvatska = '" + entMaskinkylvatska.get() + "', Motoreffekt = '" + entMaskinmotoreffekt.get() + "', Kylmedia = '" + entMaskinkylmedia.get() + "', Bullernivaute = '" + entMaskinbullernivautv.get() + "', Bullernivainne = '" + entMaskinbullernivainv.get() + "', Smorjfett = '" + entMaskinsmorjfett.get() + "', Batterityp = '" + entMaskinBatterityp.get() + "', Arsbelopp = '" + entMaskinarsbelopp.get() + "', Miljostatus = '" + entMaskinmiljostatus.get() + "', Arsmodell = '" + entMaskinarsmodell.get() + "', Registreringsnummer = '" + entMaskinregistreringsnummer.get() + "', Maskintyp = '" + entMaskintyp.get() + "', Motorvolymolja = '" + entMaskinmotoroljevolym.get() + "', Vaxelladavolym = '" + entMaskinvaxelladevolym.get() + "', Hydraulvolym = '" + entMaskinhydraulsystemvolym.get() + "', Kylvatskavolym = '" + entMaskinkylvatskavolym.get() + "', Ovrig_text = '" + TxtOvrigtext.get('1.0','end') + "', Bransle = '" + entMaskinbransle.get() + "', Dackfabrikat = '" + entMaskindackfabrikat.get() + "', Dimension = '" + entMaskindimension.get() + "', Batteriantal = '" + entMaskinbatteriAntal.get() + "' WHERE Maskinnummer = " + Typ +";")            
               cursor.execute("UPDATE maskinregister SET Period_start = '" + deMaskinperiod1.get_date().strftime('%Y-%m-%d') + "' WHERE Maskinnummer = " + Typ +";")              
               cursor.execute("UPDATE maskinregister SET Period_slut = '" + deMaskinperiod2.get_date().strftime('%Y-%m-%d') + "' WHERE Maskinnummer = " + Typ +";")
          
               for x in tillbehorAttTaBort:
                    cursor.execute("DELETE tillbehor FROM Tillbehor WHERE Maskinnummer = " + Typ +" AND Tillbehor = '" + x +"';")                   
               for x in tillbehorAttLaggaTill:
                    print(x)
                    cursor.execute("INSERT INTO tillbehor (Tillbehor, Maskinnummer) values ('" + x + "', " + Typ + ");" )
               
               if filePath is not None:
                    try:                         
                         cursor.execute("insert into bilder (sokvag, maskinnummer) values ('pics/"+maskinnummer+filePath+"', '"+maskinnummer+"');")
                    except Exception:
                         traceback.print_exc()    
               

          nyMaskin = Toplevel(root)

          #Bestämmer titel baserat på vilken knapp man tryckte på.
          if Typ=="Ny":
               nyMaskin.title("Lägg till ny maskin")
          elif Typ=="Byt":
               nyMaskin.title("Byt maskin")
          else:
               nyMaskin.title("Ändra maskin")

          nyMaskin.geometry("1025x680")

          lblMaskinnummermaskininfo = Label(nyMaskin, text= "Maskinnummer")
          lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(7,8))
          entNyMaskinnummermaskininfo = Entry(nyMaskin, width = 5 ,validate="key", validatecommand=(validera, "%P"))
          entNyMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0), pady=(7,0))

          if Typ=="Ny":
               lblMaskinnummerVal = Label(nyMaskin, text = "Autogen eller ej?")
               lblMaskinnummerVal.grid(column = 1, row = 0, sticky = E, padx=(0,23))
               cbMaskinnummer = ttk.Checkbutton(nyMaskin, command = lambda: autogenEllerEj())
               cbMaskinnummer.state(['!alternate', '!selected', '!disabled'])
               cbMaskinnummer.grid(column = 1, row = 0, sticky = E, padx=(5,0))

               def autogenEllerEj():
                    if cbMaskinnummer.instate(['selected']) == True:
                         entNyMaskinnummermaskininfo.config(state=DISABLED)
                    else:
                         entNyMaskinnummermaskininfo.config(state=NORMAL)
          else:
               pass

          #Skapar fälten för att kunna skriva i den nya informationen.
          lblMaskinbeteckning = Label(nyMaskin, text="Beteckning")
          lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinbeteckning = Entry(nyMaskin, width = 32)
          entMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))

          lblMaskinme_klass = Label(nyMaskin, text="ME-Klass")
          lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinme_klass = Entry(nyMaskin, width = 32,validate="key", validatecommand=(validera, "%P"))
          entMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))

          lblMaskinmotorfabrikat = Label(nyMaskin, text="Motorfabrikat")
          lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinmotorfabrikat = Entry(nyMaskin, width = 32)
          entMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))

          lblMaskinmotortyp = Label(nyMaskin, text="Motortyp")
          lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinmotortyp=Entry(nyMaskin, width = 32)
          entMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))

          lblMaskinmotor = Label(nyMaskin, text="Motor")
          lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinmotor = Entry(nyMaskin, width = 32)
          entMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))

          lblMaskinvaxellada = Label(nyMaskin, text="Växellåda")
          lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinvaxellada=Entry(nyMaskin, width = 32)
          entMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))

          lblMaskinhydraulsystem = Label(nyMaskin, text="Hydraulsystem")
          lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinhydraulsystem=Entry(nyMaskin, width = 32)
          entMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))

          lblMaskinkylvatska = Label(nyMaskin, text="Kylvätska")
          lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinkylvatska=Entry(nyMaskin, width = 32)
          entMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))

          lblMaskinmotoreffekt = Label(nyMaskin, text="Motoreffekt/KW")
          lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinmotoreffekt=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))

          lblMaskinmotorvarmare = Label(nyMaskin, text="Motorvärmare")
          lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
          cbMaskinmotorvarmare = ttk.Checkbutton(nyMaskin)
          cbMaskinmotorvarmare.state(['!alternate', '!selected', '!disabled'])
          cbMaskinmotorvarmare.grid(column = 1, row = 10, sticky = W, padx=(5,0))

          lblMaskinkatalysator = Label(nyMaskin, text="Katalysator")
          lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
          cbMaskinkatalysator = ttk.Checkbutton(nyMaskin)
          cbMaskinkatalysator.state(['!alternate', '!selected', '!disabled'])
          cbMaskinkatalysator.grid(column = 1, row = 11, sticky = W, padx=(5,0))

          lblMaskinpartikelfilter = Label(nyMaskin, text="Partikelfilter")
          lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
          cbMaskinpartikelfilter = ttk.Checkbutton(nyMaskin)
          cbMaskinpartikelfilter.state(['!alternate', '!selected', '!disabled'])
          cbMaskinpartikelfilter.grid(column = 1, row = 12, sticky = W, padx=(5,0))

          lblMaskinvattenbaseradlack = Label(nyMaskin, text="Vattenbaserad lack")
          lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
          cbMaskinvattenbaseradlack = ttk.Checkbutton(nyMaskin)
          cbMaskinvattenbaseradlack.state(['!alternate', '!selected', '!disabled'])
          cbMaskinvattenbaseradlack.grid(column = 1, row = 13, sticky = W, padx=(5,0))

          lblMaskinkylmedia = Label(nyMaskin, text="Kylmedia")
          lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinkylmedia=Entry(nyMaskin, width = 32)
          entMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))

          lblMaskinbullernivautv = Label(nyMaskin, text="Bullernivå utvändigt")
          lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinbullernivautv=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))

          lblMaskinbullernivainv = Label(nyMaskin, text="Bullernivå invändigt")
          lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinbullernivainv=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))

          lblMaskinsmorjfett = Label(nyMaskin, text="Smörjfett")
          lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinsmorjfett=Entry(nyMaskin, width = 32)
          entMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))

          lblMaskinBatterityp = Label(nyMaskin, text="Batterityp")
          lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinBatterityp=Entry(nyMaskin, width = 20)
          entMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))

          lblMaskinbatteriAntal = Label(nyMaskin, text="Antal")
          lblMaskinbatteriAntal.grid(column=1, row=18, sticky=E, padx=(0,35))
          entMaskinbatteriAntal = Entry(nyMaskin, width=5, validate="key", validatecommand=(validera, "%P"))
          entMaskinbatteriAntal.grid(column=1, row=18, sticky=E)

          #checkbox
          lblMaskinKollektivforsakring = Label(nyMaskin, text="Kollektiv försäkring")
          lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
          cbMaskinKollektivforsakring = ttk.Checkbutton(nyMaskin)
          cbMaskinKollektivforsakring.state(['!alternate', '!selected', '!disabled'])
          cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

          lblMaskinperiod = Label(nyMaskin, text="Period")
          lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))

          #Date entry
          deMaskinperiod1 = DateEntry(nyMaskin, values="Text", date_pattern="yyyy-mm-dd")
          deMaskinperiod1.delete(0, 'end')
          deMaskinperiod1.grid(column=1, row=20, sticky=W, padx=(10,0))

          deMaskinperiod2 = DateEntry(nyMaskin, values="Text", date_pattern="yyyy-mm-dd")
          deMaskinperiod2.delete(0, 'end')
          deMaskinperiod2.grid(column=1, row=20, sticky=E)

          lblMaskinarsbelopp = Label(nyMaskin, text="Årsbelopp")
          lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
          entMaskinarsbelopp=Entry(nyMaskin, width = 25, validate="key", validatecommand=(validera, "%P"))
          entMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))

          #Buttons

          btnSparaNyMaskin=Button(nyMaskin, text="Spara", command = lambda: sparaMaskin(Typ))
          btnSparaNyMaskin.grid(column=5, row=21, sticky=E, padx=(0,55))
          btnAvbrytNyMaskin=Button(nyMaskin, text="Avbryt", command = lambda: nyMaskin.destroy())
          btnAvbrytNyMaskin.grid(column=5, row=21,sticky=E)

          #--------------------

          lblMaskinmiljostatus = Label(nyMaskin, text="Miljöstatus")
          lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0), pady=(7,0))
          entMaskinmiljostatus=Entry(nyMaskin, width = 32)
          entMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0), pady=(7,0))

          lblMaskinarsmodell = Label(nyMaskin, text="Årsmodell")
          lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
          entMaskinarsmodell=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))

          lblMaskinregistreringsnummer = Label(nyMaskin, text="Reg. nr/Ser. nr")
          lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
          entMaskinregistreringsnummer=Entry(nyMaskin, width = 20, validate="key", validatecommand=(validera, "%P"))
          entMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))

          lblMaskintyp = Label(nyMaskin, text="Maskintyp")
          lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
          entMaskintyp=Entry(nyMaskin, width = 32)
          entMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))

          lblMaskinmotoroljevolym  = Label(nyMaskin, text="Motorolja volym/liter")
          lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
          entMaskinmotoroljevolym=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))

          lblMaskinvaxelladevolym = Label(nyMaskin, text="Växellåda volym/liter")
          lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
          entMaskinvaxelladevolym=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))

          lblMaskinhydraulsystemvolym = Label(nyMaskin, text="Hydraul volym/liter")
          lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
          entMaskinhydraulsystemvolym=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))

          lblMaskinkylvatskavolym = Label(nyMaskin, text="Kylvätska volym/liter")
          lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
          entMaskinkylvatskavolym=Entry(nyMaskin, width = 32, validate="key", validatecommand=(validera, "%P"))
          entMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))

          lblOvrigtext = Label(nyMaskin, text="Övrig Text")
          lblOvrigtext.grid(column=2, row=9, sticky = W, padx=(10,0))
          TxtOvrigtext = Text(nyMaskin, width = 32, height=3)
          TxtOvrigtext.grid(row=10, column=2, columnspan=2, rowspan=4, sticky=NSEW, padx=(10,15))
          TxtOvrigtext.config(state=DISABLED)

          #Scrollbar
          ScbTxtOvrigText = Scrollbar(nyMaskin, orient="vertical")
          ScbTxtOvrigText.grid(row = 10, column = 3, sticky = N+S+E, rowspan = 4)
          ScbTxtOvrigText.config(command =TxtOvrigtext.yview)

          TxtOvrigtext.config(yscrollcommand=ScbTxtOvrigText.set) 

          #Bild
          img_Bild = Label(nyMaskin) 
          img_Bild.grid(row=15, column=2, columnspan=2, rowspan=6)

          #Skapar fram en dialogruta där man får välja vilken bild det är man ska spara.
          def fileDialog():
               global filePath
               global img3
               global imgNyBild
               filename = filedialog.askopenfilename(initialdir =  "/", title = "Välj en fil", filetype = (("jpeg files","*.jpg"),("all files","*.*")) )
               sparSokVag = filename.rsplit("/", 1)
               filePath=sparSokVag[1]
               txtSokvag = Text(nyMaskin, width = 20, height=0.1)
               txtSokvag.grid(column = 2, row = 14, padx=(10,0), columnspan=2, sticky=W+E)
               txtSokvag.insert('end', filename)
               nyMaskin.lift()
               imgNyBild = Image.open(filename)  
               imgFixadBild = imgNyBild.resize((150,145), Image. ANTIALIAS)
               img3 = ImageTk.PhotoImage(imgFixadBild)
               img_NyBild = Label(nyMaskin, image=img3) 
               img_NyBild.grid(row=15, column=2, columnspan=2, rowspan=6)
          #Kollar om det finns en bild och isåfall sparas den i korrekt mapp.
          def fileSave():
               print("Maskinnummret är: "+str(maskinnummer))
               if imgNyBild is not None:
                    imgNyBild.save('pics/'+str(maskinnummer)+filePath)
          
          
               
          btnNyBild = Button(nyMaskin, text="Lägg till bild", command= fileDialog)
          btnNyBild.grid(column=2, row=21, sticky=W, padx=(10,0))

          #------------------------

          lblMaskinbransle = Label(nyMaskin, text="Bränsle")
          lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0), pady=(7,0))
          entMaskinbransle=Entry(nyMaskin, width = 32)
          entMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0), pady=(7,0))

          lblMaskindackfabrikat = Label(nyMaskin, text="Däckfabrikat")
          lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
          entMaskindackfabrikat=Entry(nyMaskin, width = 32)
          entMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))

          lblMaskindimension = Label(nyMaskin, text="Dimension/typ")
          lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
          entMaskindimension=Entry(nyMaskin, width = 32)
          entMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))

          #Checkbox
          lblMaskinregummerbara = Label(nyMaskin, text="Regummerbara")
          lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
          cbMaskinregummerbara = ttk.Checkbutton(nyMaskin)
          cbMaskinregummerbara.state(['!alternate', '!selected', '!disabled'])
          cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

          #Checkbox
          lblMaskinregummerade = Label(nyMaskin, text="Regummerade")
          lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
          cbMaskinregummerade = ttk.Checkbutton(nyMaskin)
          cbMaskinregummerade.state(['!alternate', '!selected', '!disabled'])
          cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

          lblMaskingasolanlaggning = Label(nyMaskin, text="Gasolanläggning")
          lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
          cbMaskingasolanlaggning = ttk.Checkbutton(nyMaskin)
          cbMaskingasolanlaggning.state(['!alternate', '!selected', '!disabled'])
          cbMaskingasolanlaggning.grid(column = 5, row = 5, sticky = W, padx=(5,0))

          lblMaskinSaneringsvatska = Label(nyMaskin, text="Saneringsvätska")
          lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
          cbMaskinSaneringsvatska = ttk.Checkbutton(nyMaskin)
          cbMaskinSaneringsvatska.state(['!alternate', '!selected', '!disabled'])
          cbMaskinSaneringsvatska.grid(column = 5, row = 6, sticky = W, padx=(5,0))

          #Checkbox
          lblMaskininsattserlagd = Label(nyMaskin, text="Maskininsats erlagd")
          lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
          cbMaskininsatserlagd = ttk.Checkbutton(nyMaskin)
          cbMaskininsatserlagd.state(['!alternate', '!selected', '!disabled'])
          cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

          lblMaskinforare = Label(nyMaskin, text="Förare")
          lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
          entMaskinforare=Entry(nyMaskin, width = 32)
          entMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))
          entMaskinforare.config(state=DISABLED)
     
          lblMaskintillbehor = Label(nyMaskin, text="Tillbehör")
          lblMaskintillbehor.grid(column=4, row=9, sticky = W, padx=(10,0))
          txtMaskintillbehor=Text(nyMaskin, width = 25, height=0.1)
          txtMaskintillbehor.grid(column=5, row=9, sticky=W, padx=(10,0))

          tillbehorAttTaBort=[]
          tillbehorAttLaggaTill=[]

          def taBortTillbehor(self):
               nyMaskin.lift()
               response = messagebox.askyesno("Ta bort tillbehör", "Vill du ta bort " + lbMaskintillbehor.get(lbMaskintillbehor.curselection()) + "?")
               nyMaskin.lift()
               if response == True:
                    tillbehorAttTaBort.append(lbMaskintillbehor.get(lbMaskintillbehor.curselection()))
                    try:
                         tillbehorAttLaggaTill.remove(lbMaskintillbehor.get(lbMaskintillbehor.curselection()))
                    except:
                         pass
                    lbMaskintillbehor.delete(lbMaskintillbehor.curselection())

          
          
          lbMaskintillbehor = Listbox(nyMaskin, height=4)
          lbMaskintillbehor.bind('<Double-Button>', taBortTillbehor)
          lbMaskintillbehor.grid(column=4, row=10, columnspan=2, rowspan=4, sticky=NSEW, padx=(10,0), pady=(5,5))  

          ScbLbMaskintillbehor = Scrollbar(nyMaskin, orient="vertical")
          ScbLbMaskintillbehor.grid(row = 10, column = 6, sticky = N+S+W, rowspan = 4)
          ScbLbMaskintillbehor.config(command =lbMaskintillbehor.yview)
          lbMaskintillbehor.config(yscrollcommand=ScbLbMaskintillbehor.set)
     
          txtMaskintillbehor.bind('<Return>', lambda x: (lbMaskintillbehor.insert('end', txtMaskintillbehor.get('1.0', 'end')), tillbehorAttLaggaTill.append(txtMaskintillbehor.get('1.0', 'end')), txtMaskintillbehor.delete('1.0','end')))


          #Försöker fylla all relevant information i korrekt entrys.
          if Typ == "Byt":
               try:
                    entNyMaskinnummermaskininfo.config(state=NORMAL)
                    entNyMaskinnummermaskininfo.delete(0, 'end')
                    entNyMaskinnummermaskininfo.insert(0, maskinnummer)
                    entNyMaskinnummermaskininfo.config(state=DISABLED)
               except:
                    pass

          if Typ != "Ny" and Typ != "Byt":
               try:
                    cursor.execute('SELECT * FROM maskinregister WHERE Maskinnummer = ' + Typ + ';')
                    maskinInfo = cursor.fetchone()
                    maskinInfo = list(maskinInfo)
               except:
                    pass
               
               try:
                    entNyMaskinnummermaskininfo.config(state=NORMAL)
                    entNyMaskinnummermaskininfo.delete(0, 'end')
                    entNyMaskinnummermaskininfo.insert(0, maskinInfo[0])
               except:
                    pass

               try:
                    entMaskinbeteckning.config(state=NORMAL)
                    entMaskinbeteckning.delete(0, 'end')
                    entMaskinbeteckning.insert(0, maskinInfo[1])
               except:
                    pass

               try:
                    entMaskinme_klass.config(state=NORMAL)
                    entMaskinme_klass.delete(0, 'end')
                    entMaskinme_klass.insert(0, maskinInfo[2])
               except:
                    pass
               
               try:
                    entMaskinmotorfabrikat.config(state=NORMAL)
                    entMaskinmotorfabrikat.delete(0, 'end')
                    entMaskinmotorfabrikat.insert(0, maskinInfo[8])
               except:
                    pass

               try:
                    entMaskinmotortyp.config(state=NORMAL)
                    entMaskinmotortyp.delete(0, 'end')
                    entMaskinmotortyp.insert(0, maskinInfo[9])
               except:
                    pass

               try:
                    entMaskinmotor.config(state=NORMAL)
                    entMaskinmotor.delete(0, 'end')
                    entMaskinmotor.insert(0, maskinInfo[16])
               except:
                    pass
               
               try:
                    entMaskinvaxellada.config(state=NORMAL)
                    entMaskinvaxellada.delete(0, 'end')
                    entMaskinvaxellada.insert(0, maskinInfo[18])
               except:
                    pass
               
               try:
                    entMaskinhydraulsystem.config(state=NORMAL)
                    entMaskinhydraulsystem.delete(0, 'end')
                    entMaskinhydraulsystem.insert(0, maskinInfo[20])
               except:
                    pass
               
               try:
                    entMaskinkylvatska.config(state=NORMAL)
                    entMaskinkylvatska.delete(0, 'end')
                    entMaskinkylvatska.insert(0, maskinInfo[33])
               except:
                    pass
               
               try:
                    TxtOvrigtext.config(state=NORMAL)
                    TxtOvrigtext.delete('1.0', 'end')
                    TxtOvrigtext.insert(END, maskinInfo[41])
                    #TxtOvrigtext.config(state=DISABLED)
               except:
                    pass

               try:
                    cursor.execute("SELECT Sokvag FROM bilder WHERE Maskinnummer = " + maskinnummer + " order by bildid desc LIMIT 1;")
                    img = cursor.fetchone()
                    print(img[0])
                    img = Image.open(img[0])  
                    img = img.resize((150,145), Image. ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img)
                    img_Bild.config(image = img2)
                    img_Bild.image=img2
               except:
                    img = Image.open("1.jpg")  
                    img = img.resize((150,145), Image. ANTIALIAS)
                    img2 = ImageTk.PhotoImage(img)
                    img_Bild.config(image = img2)
                    img_Bild.image=img2

               try:
                    entMaskinmotoreffekt.config(state=NORMAL)
                    entMaskinmotoreffekt.delete(0, 'end')
                    entMaskinmotoreffekt.insert(0, maskinInfo[10])
               except:
                    pass

               try:
                    if maskinInfo[12] == 1:
                         cbMaskinmotorvarmare.state(['selected'])
                         cbMaskinmotorvarmare.state(['!disabled'])
                    else:
                         cbMaskinmotorvarmare.state(['!selected'])
                         cbMaskinmotorvarmare.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[14] == 1:
                         cbMaskinkatalysator.state(['selected'])
                         cbMaskinkatalysator.state(['!disabled'])
                    else:
                         cbMaskinkatalysator.state(['!selected'])
                         cbMaskinkatalysator.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[15] == 1:
                         cbMaskinpartikelfilter.state(['selected'])
                         cbMaskinpartikelfilter.state(['!disabled'])
                    else:
                         cbMaskinpartikelfilter.state(['!selected'])
                         cbMaskinpartikelfilter.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[11] == 1:
                         cbMaskinvattenbaseradlack.state(['selected'])
                         cbMaskinvattenbaseradlack.state(['!disabled'])
                    else:
                         cbMaskinvattenbaseradlack.state(['!selected'])
                         cbMaskinvattenbaseradlack.state(['!disabled'])
               except:
                    pass

               try:
                    entMaskinkylmedia.config(state=NORMAL)
                    entMaskinkylmedia.delete(0, 'end')
                    entMaskinkylmedia.insert(0, maskinInfo[13])
               except:
                    pass

               try:
                    entMaskinbullernivautv.config(state=NORMAL)
                    entMaskinbullernivautv.delete(0, 'end')
                    entMaskinbullernivautv.insert(0, maskinInfo[29])
               except:
                    pass

               try:
                    entMaskinbullernivainv.config(state=NORMAL)
                    entMaskinbullernivainv.delete(0, 'end')
                    entMaskinbullernivainv.insert(0, maskinInfo[31])
               except:
                    pass

               try:
                    entMaskinsmorjfett.config(state=NORMAL)
                    entMaskinsmorjfett.delete(0, 'end')
                    entMaskinsmorjfett.insert(0, maskinInfo[24])
               except:
                    pass
               
               try:
                    entMaskinBatterityp.config(state=NORMAL)
                    entMaskinBatterityp.delete(0, 'end')
                    entMaskinBatterityp.insert(0, maskinInfo[38])
               except:
                    pass

               if maskinInfo[7] is not None:
                    try:
                         deMaskinperiod1.set_date(maskinInfo[7])
                         deMaskinperiod2.set_date(maskinInfo[42])
                    except:
                         pass

               try:
                    entMaskinarsbelopp.config(state=NORMAL)
                    entMaskinarsbelopp.delete(0, 'end')
                    entMaskinarsbelopp.insert(0, maskinInfo[5])
               except:
                    pass

               try:
                    entMaskinmiljostatus.config(state=NORMAL)
                    entMaskinmiljostatus.delete(0, 'end')
                    entMaskinmiljostatus.insert(0, maskinInfo[30])
               except:
                    pass

               try:
                    entMaskinarsmodell.config(state=NORMAL)
                    entMaskinarsmodell.delete(0, 'end')
                    entMaskinarsmodell.insert(0, maskinInfo[6])
               except:
                    pass

               try:
                    entMaskinregistreringsnummer.config(state=NORMAL)
                    entMaskinregistreringsnummer.delete(0, 'end')
                    entMaskinregistreringsnummer.insert(0, maskinInfo[26])
               except:
                    pass

               try:
                    entMaskintyp.config(state=NORMAL)
                    entMaskintyp.delete(0, 'end')
                    entMaskintyp.insert(0, maskinInfo[27])
               except:
                    pass

               try:
                    entMaskinmotoroljevolym.config(state=NORMAL)
                    entMaskinmotoroljevolym.delete(0, 'end')
                    entMaskinmotoroljevolym.insert(0, maskinInfo[17])
               except:
                    pass

               try:
                    entMaskinvaxelladevolym.config(state=NORMAL)
                    entMaskinvaxelladevolym.delete(0, 'end')
                    entMaskinvaxelladevolym.insert(0, maskinInfo[19])
               except:
                    pass

               try:
                    entMaskinhydraulsystemvolym.config(state=NORMAL)
                    entMaskinhydraulsystemvolym.delete(0, 'end')
                    entMaskinhydraulsystemvolym.insert(0, maskinInfo[21])
               except:
                    pass

               try:
                    entMaskinkylvatskavolym.config(state=NORMAL)
                    entMaskinkylvatskavolym.delete(0, 'end')
                    entMaskinkylvatskavolym.insert(0, maskinInfo[32])
               except:
                    pass

               try:
                    entMaskinbransle.config(state=NORMAL)
                    entMaskinbransle.delete(0, 'end')
                    entMaskinbransle.insert(0, maskinInfo[23])
               except:
                    pass

               try:
                    entMaskindackfabrikat.config(state=NORMAL)
                    entMaskindackfabrikat.delete(0, 'end')
                    entMaskindackfabrikat.insert(0, maskinInfo[25])
               except:
                    pass

               try:
                    entMaskindimension.config(state=NORMAL)
                    entMaskindimension.delete(0, 'end')
                    entMaskindimension.insert(0, maskinInfo[34])
               except:
                    pass

               try:
                    if maskinInfo[37] == 1:
                         cbMaskingasolanlaggning.state(['selected'])
                         cbMaskingasolanlaggning.state(['!disabled'])
                    else:
                         cbMaskingasolanlaggning.state(['!selected'])
                         cbMaskingasolanlaggning.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[22] == 1:
                         cbMaskinSaneringsvatska.state(['selected'])
                         cbMaskinSaneringsvatska.state(['!disabled'])
                    else:
                         cbMaskinSaneringsvatska.state(['!selected'])
                         cbMaskinSaneringsvatska.state(['!disabled'])
               except:
                    pass

               forarnamn=""
               if maskinInfo[40] != None:
                    cursor.execute('SELECT Namn FROM forare WHERE Forarid = ' + str(maskinInfo[40]) + ';')
                    forarnamn = cursor.fetchone()

               try:
                    entMaskinforare.config(state=NORMAL)
                    entMaskinforare.delete(0, 'end')
                    entMaskinforare.insert(0, forarnamn[0])
                    entMaskinforare.config(state=DISABLED)
               except:
                    pass
               
               referenser = []     
               referenser.clear()
               if maskinInfo[40] != None:
                    cursor.execute('SELECT Beskrivning FROM referens WHERE Forarid = ' + str(maskinInfo[40]) + ';')
                    referenser = cursor.fetchall()
                    
               try:
                    if lbMaskinreferens.index("end") != 0:
                         lbMaskinreferens.delete(0, "end")
                         for x in referenser:
                              lbMaskinreferens.insert("end", x[0])
                    else:
                         for x in referenser:
                              lbMaskinreferens.insert("end", x[0])
               except:
                    pass

               try: 
                    if maskinInfo[28] == 1:
                         cbMaskininsatserlagd.state(['selected'])
                         cbMaskininsatserlagd.state(['!disabled'])
                    else:
                         cbMaskininsatserlagd.state(['!selected'])
                         cbMaskininsatserlagd.state(['!disabled'])
               except:
                    pass
               
               try:
                    if maskinInfo[36] == 1:
                         cbMaskinregummerade.state(['selected'])
                         cbMaskinregummerade.state(['!disabled'])
                    else:
                         cbMaskinregummerade.state(['!selected'])
                         cbMaskinregummerade.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[35] == 1:
                         cbMaskinregummerbara.state(['selected'])
                         cbMaskinregummerbara.state(['!disabled'])
                    else:
                         cbMaskinregummerbara.state(['!selected'])
                         cbMaskinregummerbara.state(['!disabled'])
               except:
                    pass

               try:
                    if maskinInfo[3] == 1:
                         cbMaskinKollektivforsakring.state(['selected'])
                         cbMaskinKollektivforsakring.state(['!disabled'])
                    else:
                         cbMaskinKollektivforsakring.state(['!selected'])
                         cbMaskinKollektivforsakring.state(['!disabled'])
               except:
                    pass

               cursor.execute('SELECT Tillbehor FROM tillbehor WHERE Maskinnummer = ' + str(maskinnummer) + ';')
               tillbehor = cursor.fetchall()
          
               if lbMaskintillbehor.index("end") != 0:
                    lbMaskintillbehor.delete(0, "end")
                    for x in tillbehor:
                         lbMaskintillbehor.insert("end", x[0])
               else:
                    for x in tillbehor:
                         lbMaskintillbehor.insert("end", x[0])
               
               cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
               maskiner = cursor.fetchall()

               if LbDelagaresMaskiner.index("end") != 0:
                    LbDelagaresMaskiner.delete(0, "end")
                    for x in maskiner:
                         LbDelagaresMaskiner.insert("end", x)
               else:
                    for x in maskiner:
                         LbDelagaresMaskiner.insert("end", x)    
#Fyller LbDelagare (Listboxen på Home-fliken) med delägarna ifrån databsen
def fyllListboxDelagare():

     cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn, Foretagsnamn FROM foretagsregister")
     delagareLista = []
     delagareLista = cursor.fetchall()
     LbDelagare.delete(0, 'end')

     for item in delagareLista:
          item = list(item)
          if item[1] == None:
               item[1] = ""
          if item[2] == None:
               item[2] = ""
          s=""
          s += str(item[0])
          if item[1] == "":
               s+= ""
          else:
               s+= " - "
               s+=str(item[1])
               s+= " "
               s+=str(item[2])
          s+=" - "
          s+=str(item[3])                              
               
          LbDelagare.insert("end", s)
#Fyller LbMaskiner (Listboxen på Home-fliken) med maskinerna ifrån databasen
def hamtaAllaMaskiner(self):
     global medlemsnummer

     selectedDelagare = LbDelagare.get(LbDelagare.curselection())
     indexSpace = selectedDelagare.index(" ")
     stringSelectedDelagare = str(selectedDelagare[0:indexSpace])
     delagare = "".join(stringSelectedDelagare)
     medlemsnummer = delagare
     cursor.execute('SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Medlemsnummer = ' + delagare + ';')
     result = cursor.fetchall()
        
     if LbMaskiner.index("end") != 0:
          LbMaskiner.delete(0, "end")
          for item in result:
               item = list(item)
               if item[1] == None:
                    item[1] = ""
               if item[2] == None:
                    item[2] = ""
               
               s=""
               s += str(item[0])
               if item[1] == "":
                    s+= ""
               else:
                    s+= " - "
                    s+=str(item[1])
               if item[2] == "":
                    s+= " "
               else:
                    s+= " - "
                    s+=str(item[2])
                      
               LbMaskiner.insert("end",s )

     else:
          for item in result:
               item = list(item)
               if item[1] == None:
                    item[1] = ""
               if item[2] == None:
                    item[2] = ""
               
               s=""
               s += str(item[0])
               if item[1] == "":
                    s+= ""
               else:
                    s+= " - "
                    s+=str(item[1])
               if item[2] == "":
                    s+= " "
               else:
                    s+= " - "
                    s+=str(item[2])
                                               
               LbMaskiner.insert("end",s )




     fyllDelagarInfo(medlemsnummer)
#Fyller delägarens info i Delägare-fliken när delägaren väljs via Listboxen (LbDelagare)
def fyllDelagarInfoMedNummer(self):
     global medlemsnummer

     selectedDelagare = LbDelagare.get(LbDelagare.curselection())
     indexSpace = selectedDelagare.index(" ")
     stringSelectedDelagare = str(selectedDelagare[0:indexSpace])
     medlemsnummer = "".join(stringSelectedDelagare)

     tomMaskinInfo()
     fyllDelagarInfo(medlemsnummer)
     try:
          hamtaDelagarensMaskiner()
          fyllMaskinInfo("endastDelagare")
     except Exception:
          traceback.print_exc()

     tabControl.select(delagare)
#Fyller delägarens info i Delägare-fliken
def fyllDelagarInfo(medlemsnummer):
     #global medlemsnummer

     cursor.execute('SELECT medlemsnummer, foretagsnamn, fornamn, efternamn, gatuadress, postnummer, postadress, telefon FROM foretagsregister WHERE medlemsnummer = ' + medlemsnummer + ';')
     delagarInfo = cursor.fetchone()
     if delagarInfo is None:
          tomDelagareInfo()
          messagebox.showerror("Fel", "Def finns ingen delägare med det numret.")
     else:
          delagarInfo = list(delagarInfo)

          #sätter delägaresidans info

          txtMedlemsnummerDelagare.config(state=NORMAL)
          txtMedlemsnummerDelagare.delete('1.0', 'end')
          txtMedlemsnummerDelagare.insert('end', delagarInfo[0])
          txtMedlemsnummerDelagare.config(state=DISABLED)
          
          try:
               txtForetag.config(state=NORMAL)
               txtForetag.delete('1.0', 'end')
               txtForetag.insert('end', delagarInfo[1])
               txtForetag.config(state=DISABLED)
          except:
               txtForetag.config(state=DISABLED)
          
          try:
               txtFornamn.config(state=NORMAL)
               txtFornamn.delete('1.0', 'end')
               txtFornamn.insert('end', delagarInfo[2])
               txtFornamn.config(state=DISABLED)
          except:
               txtFornamn.config(state=DISABLED)
          
          try:
               txtEfternamn.config(state=NORMAL)
               txtEfternamn.delete('1.0', 'end')
               txtEfternamn.insert('end', delagarInfo[3])
               txtEfternamn.config(state=DISABLED)
          except:
               txtEfternamn.config(state=DISABLED)
          
          try:
               txtAdress.config(state=NORMAL)
               txtAdress.delete('1.0', 'end')
               txtAdress.insert('end', delagarInfo[4])
               txtAdress.config(state=DISABLED)
          except:
               txtAdress.config(state=DISABLED)
          
          try:
               txtPostnummer.config(state=NORMAL)
               txtPostnummer.delete('1.0', 'end')
               txtPostnummer.insert('end', delagarInfo[5])
               txtPostnummer.config(state=DISABLED)
          except:
               txtPostnummer.config(state=DISABLED)
          
          try:
               txtPostadress.config(state=NORMAL)
               txtPostadress.delete('1.0', 'end')
               txtPostadress.insert('end', delagarInfo[6])
               txtPostadress.config(state=DISABLED)
          except:
               txtPostadress.config(state=DISABLED)
          
          try:
               txtTelefon.config(state=NORMAL)
               txtTelefon.delete('1.0', 'end')
               txtTelefon.insert('end', delagarInfo[7])
               txtTelefon.config(state=DISABLED)
          except:
               txtTelefon.config(state=DISABLED)
#Tömmer alla entrys/checkboxes etc gällande Maskininfon.
def tomMaskinInfo():
     
          entMaskinnummermaskininfo.config(state=NORMAL)
          entMaskinnummermaskininfo.delete(0, 'end')
          entMaskinnummermaskininfo.config(state=DISABLED)

          entMaskinbeteckning.config(state=NORMAL)
          entMaskinbeteckning.delete(0, 'end')
          entMaskinbeteckning.config(state=DISABLED)

          entMaskinme_klass.config(state=NORMAL)
          entMaskinme_klass.delete(0, 'end')
          entMaskinme_klass.config(state=DISABLED)

          entMaskinmotorfabrikat.config(state=NORMAL)
          entMaskinmotorfabrikat.delete(0, 'end')
          entMaskinmotorfabrikat.config(state=DISABLED)

          entMaskinmotortyp.config(state=NORMAL)
          entMaskinmotortyp.delete(0, 'end')
          entMaskinmotortyp.config(state=DISABLED)

          entMaskinmotor.config(state=NORMAL)
          entMaskinmotor.delete(0, 'end')
          entMaskinmotor.config(state=DISABLED)

          entMaskinvaxellada.config(state=NORMAL)
          entMaskinvaxellada.delete(0, 'end')
          entMaskinvaxellada.config(state=DISABLED)

          entMaskinhydraulsystem.config(state=NORMAL)
          entMaskinhydraulsystem.delete(0, 'end')
          entMaskinhydraulsystem.config(state=DISABLED)

          entMaskinkylvatska.config(state=NORMAL)
          entMaskinkylvatska.delete(0, 'end')
          entMaskinkylvatska.config(state=DISABLED)

          entMaskinmotoreffekt.config(state=NORMAL)
          entMaskinmotoreffekt.delete(0, 'end')
          entMaskinmotoreffekt.config(state=DISABLED)

          cbMaskinmotorvarmare.state(['!selected'])
          cbMaskinmotorvarmare.state(['disabled'])

          cbMaskinkatalysator.state(['!selected'])
          cbMaskinkatalysator.state(['disabled'])

          cbMaskinpartikelfilter.state(['!selected'])
          cbMaskinpartikelfilter.state(['disabled'])

          cbMaskinvattenbaseradlack.state(['!selected'])
          cbMaskinvattenbaseradlack.state(['disabled'])

          entMaskinkylmedia.config(state=NORMAL)
          entMaskinkylmedia.delete(0, 'end')
          entMaskinkylmedia.config(state=DISABLED)

          entMaskinbullernivautv.config(state=NORMAL)
          entMaskinbullernivautv.delete(0, 'end')
          entMaskinbullernivautv.config(state=DISABLED)

          entMaskinbullernivainv.config(state=NORMAL)
          entMaskinbullernivainv.delete(0, 'end')
          entMaskinbullernivainv.config(state=DISABLED)

          entMaskinsmorjfett.config(state=NORMAL)
          entMaskinsmorjfett.delete(0, 'end')
          entMaskinsmorjfett.config(state=DISABLED)

          entMaskinBatterityp.config(state=NORMAL)
          entMaskinBatterityp.delete(0, 'end')
          entMaskinBatterityp.config(state=DISABLED)

          deMaskinperiod1.delete(0, END)
          deMaskinperiod2.delete(0, END)

          entMaskinarsbelopp.config(state=NORMAL)
          entMaskinarsbelopp.delete(0, 'end')
          entMaskinarsbelopp.config(state=DISABLED)

          entMaskinmiljostatus.config(state=NORMAL)
          entMaskinmiljostatus.delete(0, 'end')
          entMaskinmiljostatus.config(state=DISABLED)

          entMaskinarsmodell.config(state=NORMAL)
          entMaskinarsmodell.delete(0, 'end')
          entMaskinarsmodell.config(state=DISABLED)

          entMaskinregistreringsnummer.config(state=NORMAL)
          entMaskinregistreringsnummer.delete(0, 'end')
          entMaskinregistreringsnummer.config(state=DISABLED)

          entMaskintyp.config(state=NORMAL)
          entMaskintyp.delete(0, 'end')
          entMaskintyp.config(state=DISABLED)

          entMaskinmotoroljevolym.config(state=NORMAL)
          entMaskinmotoroljevolym.delete(0, 'end')
          entMaskinmotoroljevolym.config(state=DISABLED)

          entMaskinvaxelladevolym.config(state=NORMAL)
          entMaskinvaxelladevolym.delete(0, 'end')
          entMaskinvaxelladevolym.config(state=DISABLED)

          entMaskinhydraulsystemvolym.config(state=NORMAL)
          entMaskinhydraulsystemvolym.delete(0, 'end')
          entMaskinhydraulsystemvolym.config(state=DISABLED)

          entMaskinkylvatskavolym.config(state=NORMAL)
          entMaskinkylvatskavolym.delete(0, 'end')
          entMaskinkylvatskavolym.config(state=DISABLED)

          entMaskinbransle.config(state=NORMAL)
          entMaskinbransle.delete(0, 'end')
          entMaskinbransle.config(state=DISABLED)

          entMaskindackfabrikat.config(state=NORMAL)
          entMaskindackfabrikat.delete(0, 'end')
          entMaskindackfabrikat.config(state=DISABLED)

          entMaskindimension.config(state=NORMAL)
          entMaskindimension.delete(0, 'end')
          entMaskindimension.config(state=DISABLED)

          cbMaskingasolanlaggning.state(['!selected'])
          cbMaskingasolanlaggning.state(['disabled'])

          cbMaskinSaneringsvatska.state(['!selected'])
          cbMaskinSaneringsvatska.state(['disabled'])


          entMaskinforare.config(state=NORMAL)
          entMaskinforare.delete(0, 'end')
          entMaskinforare.config(state=DISABLED)

          cbMaskininsatserlagd.state(['!selected'])
          cbMaskininsatserlagd.state(['disabled'])

          cbMaskinregummerade.state(['!selected'])
          cbMaskinregummerade.state(['disabled'])

          cbMaskinregummerbara.state(['!selected'])
          cbMaskinregummerbara.state(['disabled'])

          cbMaskinKollektivforsakring.state(['!selected'])
          cbMaskinKollektivforsakring.state(['disabled'])

          lbMaskinreferens.delete(0, "end")
          lbMaskintillbehor.delete(0, "end")
          LbDelagaresMaskiner.delete(0, "end")
#Tömmer alla entrys/texts etc gällande Delägare
def tomDelagareInfo():
          
          txtMedlemsnummerDelagare.config(state=NORMAL)
          txtMedlemsnummerDelagare.delete('1.0', 'end')
          txtMedlemsnummerDelagare.config(state=DISABLED)

          txtForetag.config(state=NORMAL)
          txtForetag.delete('1.0', 'end')
          txtForetag.config(state=DISABLED)

          txtFornamn.config(state=NORMAL)
          txtFornamn.delete('1.0', 'end')
          txtFornamn.config(state=DISABLED)

          txtEfternamn.config(state=NORMAL)
          txtEfternamn.delete('1.0', 'end')
          txtEfternamn.config(state=DISABLED)

          txtAdress.config(state=NORMAL)
          txtAdress.delete('1.0', 'end')
          txtAdress.config(state=DISABLED)

          txtPostnummer.config(state=NORMAL)
          txtPostnummer.delete('1.0', 'end')
          txtPostnummer.config(state=DISABLED)

          txtPostadress.config(state=NORMAL)
          txtPostadress.delete('1.0', 'end')
          txtPostadress.config(state=DISABLED)

          txtTelefon.config(state=NORMAL)
          txtTelefon.delete('1.0', 'end')
          txtTelefon.config(state=DISABLED)   
#Funktion för att ta bort maskiner
def taBortMaskin(maskinnummer):
     global medlemsnummer
     
     if len(maskinnummer) == 0:
          messagebox.showerror(title="Välj en maskin först.", message="Du måste välja en maskin innan du kan ta bort den.")
     else:
          response = messagebox.askyesno("Varning!", "Är du säker på att du vill ta bort maskin nr. " + str(maskinnummer) + "?")
          if response == 1:  
               try:  
                    cursor.execute("select sokvag from bilder where maskinnummer ="+maskinnummer+";")
                    listaAvBilder = cursor.fetchall() 
                    cursor.execute("Delete from bilder where maskinnummer ="+maskinnummer+";")   
                    cursor.execute("Delete from tillbehor where maskinnummer ="+maskinnummer+";")   
                    cursor.execute("DELETE FROM maskinregister WHERE Maskinnummer = " + str(maskinnummer) + ";")
                    db.commit()
                    taBortBilder(listaAvBilder)
                    tomMaskinInfo()
                    hamtaDelagarensMaskiner()
                    fyllMaskinInfo("franMaskiner")
               except Exception:
                    db.rollback()
                    traceback.print_exc()
          else:
               pass
#Funktion för att ta bort bilder
def taBortBilder(listaAvBilder):     
     for x in listaAvBilder:
          if os.path.exists(x[0]):
               os.remove(x[0])
          else:
               print("Finns inga bilder")      
#Hämtar maskinerna som tillhör en viss Delägare och fyller LbDelagaresMaskiner med dem.
def hamtaDelagarensMaskiner():
     global medlemsnummer

     cursor.execute('SELECT Maskinnummer FROM maskinregister WHERE Medlemsnummer = ' + medlemsnummer + ';')
     maskiner = cursor.fetchall()
     if len(maskiner) != 0:
          LbDelagaresMaskiner.selection_clear(0, "end")
          if LbDelagaresMaskiner.index("end") != 0:
               LbDelagaresMaskiner.delete(0, "end")
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)
          else:
               for x in maskiner:
                    LbDelagaresMaskiner.insert("end", x)   
          LbDelagaresMaskiner.selection_set(0)
          fyllMaskinInfo("endastDelagare")
#Hämtar delägare ifrån Delägare-flikens sökfunktion
def hamtaDelagare(medlemsnr):
     global medlemsnummer

     if len(medlemsnr) == 0:
          messagebox.showerror("Fel", "Fyll i ett medlemsnummer.") 
     else:
          medlemsnummer = medlemsnr

          tomMaskinInfo()
          fyllDelagarInfo(medlemsnummer)
          hamtaDelagarensMaskiner()
#Skapar ett fönster med historiken kopplad till en maskin
def historikFonster(maskinnummer):

     if len(maskinnummer) == 0:
          messagebox.showerror("Fel", "Välj en maskin att se historiken för.")
     
     else:
          historikFonster = Toplevel(root)

          historikFonster.title("Historik")

          historikFonster.geometry("475x280")

          def hamtaHistorik():

               if maskinnummer is not None and maskinnummer != "":
                    cursor.execute('SELECT Maskinnummer, Beteckning, Registreringsnummer, ME_klass, Datum FROM historik WHERE Maskinnummer = ' + str(maskinnummer) + ';')
                    result = cursor.fetchall()

                    count = 0

                    for x in result:                           
                         LbHistorik.insert(parent='', index="end", iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4]))
                         count += 1
                    
                    if len(result) == 0:
                         btnTaBortHistorik["state"] = DISABLED
                    else:
                         btnTaBortHistorik["state"] = NORMAL
               else:
                    btnTaBortHistorik["state"] = DISABLED

          def taBortHistorik():
               maskinnummer=  ""
               datum = ""
               for item in LbHistorik.selection():
                    id = LbHistorik.item(item, "values")
                    maskinnummer = id[0]
                    datum = (id[4])
                    LbHistorik.delete(item)

               cursor.execute("SELECT historikid FROM historik WHERE Maskinnummer = " + str(maskinnummer) + " and Datum = '" + datum + "'")
               historikid = cursor.fetchone()

               try:
                    cursor.execute("DELETE FROM historik WHERE historikid = '" + str(historikid[0]) + "'")
                    db.commit()
               except Exception:
                    traceback.print_exc()
                    db.rollback()
          
          LbHistorik = ttk.Treeview(historikFonster)
          LbHistorik.grid(row=1, column=1, padx=(10,0), pady=(10,0))
          LbHistorik['columns'] = ("Maskinnummer", "Beteckning", "Reg.nr", "ME-klass", "Datum")
          LbHistorik.column('#0', width=0)
          LbHistorik.column("Maskinnummer", anchor=W, width=65)
          LbHistorik.column("Beteckning", anchor=W, width=135)
          LbHistorik.column("Reg.nr", anchor=W, width=75)
          LbHistorik.column("ME-klass", anchor=W, width=75)
          LbHistorik.column("Datum", anchor=W, width=100)

          LbHistorik.heading('#0', text="")
          LbHistorik.heading("Maskinnummer", text="Maskinnr.", anchor=W)
          LbHistorik.heading("Beteckning", text="Beteckning", anchor=W)
          LbHistorik.heading("Reg.nr", text="Reg.nr", anchor=W)
          LbHistorik.heading("ME-klass", text="ME-klass", anchor=W)
          LbHistorik.heading("Datum", text="Datum", anchor=W)

          btnTaBortHistorik = Button(historikFonster, text="Ta bort", command=lambda: taBortHistorik())
          btnTaBortHistorik.grid(row=2, column=1, sticky=E, pady=(5,0))

          

          hamtaHistorik()
#Sparar historik i databasen
def sparaHistorik(maskinnummer):

     cursor.execute("SELECT MarkeModell, Registreringsnummer, ME_Klass FROM maskinregister WHERE Maskinnummer = " + str(maskinnummer) + ";")
     maskinHistorik = cursor.fetchone()
     maskinHistorik = list(maskinHistorik)

     cursor.execute("SELECT Foretagsnamn FROM foretagsregister WHERE Medlemsnummer IN (SELECT Medlemsnummer FROM maskinregister WHERE Maskinnummer = " + str(maskinnummer) + ");")
     foretagLista = cursor.fetchone()   
     foretagLista = list(foretagLista)

     beteckning = ""
     regnr = ""
     me_klass = None

     maskinnummer = int(maskinnummer)
     beteckning = maskinHistorik[0]
     regnr = maskinHistorik[1]
     foretag = foretagLista[0]
     datum = datetime.date(datetime.now())
     if maskinHistorik[2] is not None:
          me_klass = str(maskinHistorik[2])
     else: 
          pass
     
     if me_klass is None:
          cursor.execute("INSERT INTO historik (Maskinnummer, Beteckning, Datum, Registreringsnummer, Foretag) VALUES (%s, %s, %s, %s, %s)", (maskinnummer, beteckning, datum, regnr, foretag))
     else:
          cursor.execute("INSERT INTO historik (Maskinnummer, Beteckning, Datum, Registreringsnummer, ME_klass, Foretag) VALUES (%s, %s, %s, %s, %s, %s)", (maskinnummer, beteckning, datum, regnr, me_klass, foretag))
     db.commit()
#Hämtar förare ur databasen och lägger dessa i LbForare på Förare-fliken
def hamtaForare():

     cursor.execute("SELECT Forarid, Namn FROM forare")
     forarlista = cursor.fetchall()
     lbForare.delete(0, 'end')
     for item in forarlista:         
          s=""
          s+= str(item[0])
          s+=" "
          s+= str(item[1])
          lbForare.insert("end", s) 
#Fyller lbReferenser och EntKoppladMaskin
def hamtaReferenser(self):
     global forarid

     selectedForare = lbForare.get(lbForare.curselection())
     indexSpace = selectedForare.index(" ")
     stringSelectedForare = str(selectedForare[0:indexSpace])
     forarid = "".join(stringSelectedForare)

     cursor.execute("SELECT Beskrivning FROM referens WHERE Forarid = "+ forarid +";")
     referenser = cursor.fetchall()
     cursor.execute("SELECT Maskinnummer FROM maskinregister WHERE Forarid = " +forarid +" LIMIT 1;")
     koppladMaskin = cursor.fetchone()
     lbReferenser.delete(0, 'end')
     refreshKoppladMaskin(forarid)
     

     for item in referenser:                              
          lbReferenser.insert("end", item[0])
#Lägger till en förare i databasen.
def laggTillForare(forare):
     
     if len(forare) == 0:
          messagebox.showerror("Fel", "Fyll i ett namn på föraren.")
     else:
          cursor.execute("INSERT INTO forare (Namn) VALUES ('"+ forare +"')")
          hamtaForare()
          db.commit()

          entLaggTillForare.delete(0, 'end')
#Lägger till referenser som är kopplade till en förare.
def laggTillReferens(beskrivning):
     global forarid     
     print(forarid)
     print(len(forarid))
     if len(beskrivning) == 0:
          messagebox.showerror("Fel", "Fyll i en referens.")
     
     elif len(forarid) == 0:
          messagebox.showerror("Fel", "Välj en förare.")

     else:
          cursor.execute("INSERT INTO referens (Beskrivning, Forarid) VALUES ('" + beskrivning + "', " + forarid +")")
          db.commit()
          
          entLaggTillReferens.delete(0, 'end')

          cursor.execute("SELECT Beskrivning FROM referens WHERE Forarid = "+ forarid +";")
          referenser = cursor.fetchall()
          lbReferenser.delete(0, 'end')
               
          for item in referenser:                              
               lbReferenser.insert("end", item[0])
#Tar bort referenser som är kopplade till en förare.
def taBortReferens():
     global forarid

     if len(lbReferenser.curselection()) == 0:
          messagebox.showerror("Fel", "Välj referensen som skall tas bort.")
     else:
          referens = lbReferenser.get(lbReferenser.curselection())
          cursor.execute("DELETE FROM referens WHERE Beskrivning = '"+ referens +"'")
          db.commit()

          cursor.execute("SELECT Beskrivning FROM referens WHERE Forarid = "+ forarid +";")
          referenser = cursor.fetchall()
          lbReferenser.delete(0, 'end')
               
          for item in referenser:                              
               lbReferenser.insert("end", item[0])
#Tar bort referenser kopplade till en förare samt tar även bort föraren.     
def taBortForare():
     global forarid
     def deleteForare(forarensId):
          cursor.execute("UPDATE maskinregister SET Forarid = NULL WHERE Forarid = %s", (forarensId,))
          cursor.execute("Delete from referens where forarid =%s", (forarensId,))
          cursor.execute("DELETE FROM forare WHERE forarid = %s", (forarensId,))
     if len(lbForare.curselection()) == 0:
          messagebox.showerror("Fel", "Välj föraren som skall tas bort.")
     else:
          selectedForare = lbForare.get(lbForare.curselection())
          indexSpace = selectedForare.index(" ")
          stringSelectedForare = str(selectedForare[0:indexSpace])
          forarid = "".join(stringSelectedForare)
          cursor.execute("SELECT forarid FROM maskinregister WHERE forarid = %s", (forarid,))
          kopplad = cursor.fetchall()
          #Kollar om föraren är kopplad till en maskin.
          if len(kopplad) != 0:
               response = messagebox.askyesno("Varning", "Föraren är kopplad till en maskin.\nVill du ta bort föraren ändå?")
               if response == 1:  
                    try:
                         deleteForare(forarid)
                         db.commit()
                    except Exception:
                         traceback.print_exc()
                    entKoppladMaskin.config(state=NORMAL)
                    entKoppladMaskin.delete(0, 'end')
                    lbReferenser.delete(0,'end')
                    hamtaForare()
                    lbForare.selection_clear(0, END)
                    forarid = ""
                    
               elif response == 0:
                    pass
          #Om föraren in är kopplad till en maskin
          else:
               response = messagebox.askyesno("Varning", "Är du säker på att du vill ta bort föraren? Hans referenser kommer också tas bort.")
               if response == 1:
                    try:
                         deleteForare(forarid)
                         db.commit()
                    except Exception:
                         traceback.print_exc()
                    entKoppladMaskin.config(state=NORMAL)
                    entKoppladMaskin.delete(0, 'end')
                    lbReferenser.delete(0,'end')
                    hamtaForare()
                    lbForare.selection_clear(0, END)
                    forarid = ""
                    
               elif response == 0:
                    pass 
#Hämtar delägare efter det medlemsnummer som söks på i Home-fliken
def hamtaDelagareFranEntry():

     cursor.execute("SELECT Medlemsnummer, Fornamn, Efternamn, Foretagsnamn FROM foretagsregister WHERE Medlemsnummer LIKE '" + EntMedlemsnummer.get() + "%'")
     delagareLista = []
     delagareLista = cursor.fetchall()
     delagareLista = list(delagareLista)
     LbDelagare.delete(0, 'end')

     for item in delagareLista:
          item = list(item)
          if item[1] == None:
               item[1] = ""
          if item[2] == None:
               item[2] = ""
          s=""
          s += str(item[0])
          if item[1] == "":
               s+= ""
          else:
               s+= " - "
               s+=str(item[1])
               s+= " "
               s+=str(item[2])
          s+=" - "
          s+=str(item[3])                              
               
          LbDelagare.insert("end", s)
#Hämta maskiner efter det maskinnummer som söks på i Home-fliken
def hamtaMaskinerFranEntry():

     cursor.execute("SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Maskinnummer LIKE '" + EntMaskinnummer.get() + "%'")
     result = cursor.fetchall()
     result = list(result)
     LbMaskiner.delete(0, "end")   

     for item in result:
          item = list(item)
          if item[1] == None:
               item[1] = ""
          if item[2] == None:
               item[2] = ""

          s=""
          s += str(item[0])

          if item[1] == "":
               s+= " "
          else:
               s+= " - "
               s+=str(item[1])
          if item[2] == "":
               s+= " "
          else:
               s+= " - "
               s+=str(item[2])

          LbMaskiner.insert("end",s )
#Byter försäkringsbolag.               
def bytForsakring():
     nyForsakring=askstring("Försakring","Namnet på nya försäkringsgivaren.")
     if len(nyForsakring)!=0:

          print(nyForsakring)
          if nyForsakring is not None:
               try:
                    cursor.execute("update forsakringsgivare set forsakringsgivare ='"+nyForsakring+"' where idforsakringsgivare=1")
                    db.commit()
                    hamtaForsakring()
               except Exception:
                    traceback.print_exc()
                    db.rollback()
     else:
          messagebox.showerror(title="Ej godkännt försäkringsnamn.", message="Du måste skriva i ett giltigt försäkringsnamn.")
#Hämtar det försäkringsbolag som är inlagt i databasen      
def hamtaForsakring():
     forsakringsGivare=""
     try:
          cursor.execute("select Forsakringsgivare from forsakringsgivare where idforsakringsgivare=1")
          forsakringsGivare = cursor.fetchone()
     except Exception:
          traceback.print_exc()
     txtNuvarandeForsakring.config(state=NORMAL)
     txtNuvarandeForsakring.delete(1.0, END)
     txtNuvarandeForsakring.insert(END, forsakringsGivare[0])
     txtNuvarandeForsakring.config(state=DISABLED)
#Uppdaterar försäkringsinformationen gällande Startdatum, Slutdatum och Årspremien
def uppdateraForsakring():
     print(denyttStartDatum.get())
     if len(denyttStartDatum.get())==0:
          messagebox.showerror("Felmeddelande", "Du måste ha ett nytt start datum ifyllt.")
     elif len(denyttSlutDatum.get())==0:
          messagebox.showerror("Felmeddelande", "Du måste ha ett nytt slut datum ifyllt.")
     elif len(entnyArsPremie.get()) ==0:
          messagebox.showerror("Felmeddelande", "Du måste ha en ny årspremie ifylld.")
     else:
          response = messagebox.askyesno("Varning!", "Är du säker på att du vill uppdatera all försäkringsinformation? \nDetta kommer uppdatera alla maskiner i maskinregistret.")
          if response ==1:
               denyttStartDatum.get_date().strftime('%Y-%m-%d')
               denyttSlutDatum.get_date().strftime('%Y-%m-%d')
               entnyArsPremie.get()
               try:
                    for result in cursor.execute("set sql_safe_updates=0; update maskinregister set period_start ='"+denyttStartDatum.get_date().strftime('%Y-%m-%d')+"' where forsakring =1; update maskinregister set period_slut ='"+denyttSlutDatum.get_date().strftime('%Y-%m-%d')+"' where forsakring =1; update maskinregister set arsbelopp ='"+entnyArsPremie.get()+"' where forsakring=1; set sql_safe_updates=1;", multi=True):
                         pass
                    db.commit()
               except Exception:
                    db.rollback()
                    traceback.print_exc()
#Hämtar alla maskiner i databasen och lägger dessa i Listboxen på Förare-fliken
def hamtaForareMaskin():
     cursor.execute("SELECT Maskinnummer, MarkeModell, Arsmodell FROM maskinregister WHERE Maskinnummer LIKE '" + EntMaskinnummer.get() + "%'")
     result = cursor.fetchall()
     result = list(result)
     LbForareDelagaresMaskiner.delete(0, "end")   
    
     for item in result:
          item = list(item)
          if item[1] == None:
               item[1] = ""
          if item[2] == None:
               item[2] = ""
          
          s=""
          s += str(item[0])
          if item[1] == "":
               s+= ""
          else:
               s+= " - "
               s+=str(item[1])
          if item[2] == "":
               s+= ""
          else:
               s+= " - "
               s+=str(item[2])
                      
               LbForareDelagaresMaskiner.insert("end",s )
#Kopplar ihop en förare och en maskin.
def kopplaMaskin():

     if len(lbForare.curselection()) == 0:
          messagebox.showerror("Fel", "Välj föraren som skall kopplas.")
     elif len(LbForareDelagaresMaskiner.curselection()) == 0:
          messagebox.showerror("Fel", "Välj maskinen som skall kopplas.")
     else:
          forarid = lbForare.get(lbForare.curselection())
          index2 = forarid.index(" ")
          stringforarid = str(forarid[0:index2])
          foraridString = "".join(stringforarid)
          print("Forarid: " +foraridString)

          maskinid = LbForareDelagaresMaskiner.get(LbForareDelagaresMaskiner.curselection())
          index3 = maskinid.index(" ")
          stringmaskinid = str(maskinid[0:index3])
          maskinidString = "".join(stringmaskinid)
          print("Maskinid: " +maskinidString)

     
     #Återanvändningsbar metod för att koppla en forare till en maskin.
     def queryKopplaMaskin():
          try:
               cursor.execute("UPDATE maskinregister SET Forarid = NULL WHERE Forarid = " +foraridString +";")
               cursor.execute("UPDATE maskinregister SET Forarid =" +foraridString + " WHERE Maskinnummer =" +maskinidString +";")
               db.commit()
               refreshKoppladMaskin(foraridString)
          except Exception:
               traceback.print_exc()
               db.rollback()

     cursor.execute("SELECT Forarid FROM maskinregister WHERE Maskinnummer = " +maskinidString +";")
     x=cursor.fetchone()
     if x[0] is not None:
          response = messagebox.askyesno("Varning!", "Det finns redan en förare registrerad på maskin nummer "+maskinidString +" \nVill du fortsätta ändå?")
          if response ==1:
               queryKopplaMaskin()
          else: 
            pass   
     else:
          queryKopplaMaskin()
#Kopplar isär en förare och en maskin.
def kopplaBortMaskin():
     if len(lbForare.curselection()) == 0:
          messagebox.showerror("Fel", "Ingen förare vald")
     else:
          forarid = lbForare.get(lbForare.curselection())
          index2 = forarid.index(" ")
          stringforarid = str(forarid[0:index2])
          foraridString = "".join(stringforarid)
          print("Forarid: " +foraridString)

          try:
               cursor.execute("SELECT Namn from forare WHERE Forarid = '" +foraridString +"';")
               forarNamn = cursor.fetchone()
               response = messagebox.askyesno("Varning", "Är du säker att du vill kopplingen mellan " + str(forarNamn[0]) +" och maskin " + entKoppladMaskin.get() + "?")
               if response == 1:
                    cursor.execute("UPDATE maskinregister SET Forarid = NULL WHERE Forarid = " +foraridString +";")
                    db.commit()
                    refreshKoppladMaskin(foraridString)
          except Exception:
               traceback.print_exc()
               db.rollback()
#Uppdaterar rutan som visar vilken maskin en förare är kopplad till.
def refreshKoppladMaskin(forarId):
     cursor.execute("SELECT Maskinnummer FROM maskinregister WHERE Forarid = " +forarId +" LIMIT 1;")
     koppladMaskin = cursor.fetchone()
     entKoppladMaskin.config(state=NORMAL)
     entKoppladMaskin.delete(0, 'end')

     if koppladMaskin is not None:
          entKoppladMaskin.insert(0, koppladMaskin[0])
     
     entKoppladMaskin.config(state=DISABLED)
#Validerar entrys så att endast siffror går att använda i dem.
def valideraSiffror(input):
     if input.isdigit() and len(input) < 7 or len(input)==0 :
          return True
     else:
          return False
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
root.geometry("1365x750")
root.resizable(False, False)
 
#tabs

tabControl = ttk.Notebook(root)
home = ttk.Frame(tabControl)
delagare = ttk.Frame(tabControl)
forare = ttk.Frame(tabControl)
forsakring = ttk.Frame(tabControl)
installningar = ttk.Frame(tabControl)
tabControl.add(home, text='Home')
tabControl.add(delagare, text='Delägare')
tabControl.add(forare, text="Förare")
tabControl.add(forsakring, text='Försäkringar')
tabControl.add(installningar, text='Inställningar')
tabControl.grid(column=0, row=0)


#Globala variabler

filePath = None
imgNyBild = None
medlemsnummer = ""
maskinnummer = ""
forarid = ""

validera = root.register(valideraSiffror)

#skapar textfält och textboxar

BtnMaskinnehav = Button(home, text="Maskininnehav", command = lambda: maskininnehav(medlemsnummer))
BtnMaskinnehav.grid(row=3, column = 5)

BtnForsakringFraga = Button(home, text="Försäkring (fråga)", command = lambda: forsakringPerDelagareFraga(medlemsnummer))
BtnForsakringFraga.grid(row=3, column=5, pady=(100,0))

BtnForsakringLista = Button(home, text="Försäkringar", command = lambda: forsakringPerDelagare())
BtnForsakringLista.grid(row=3, column=5, pady=(200,0))

BtnMaskinerAndradeBelopp = Button(home, text="Maskiner med\nändrade belopp", command = lambda: maskinerMedAndradeBelopp())
BtnMaskinerAndradeBelopp.grid(row=3, column=5, pady=(0,100))

EntMedlemsnummer = Entry(home, width=5, text = "Medlemsnummer") 
EntMedlemsnummer.grid(row=1, column=1, pady=(50,0), padx=(72,0), sticky=E)
EntMedlemsnummer.bind("<KeyRelease>", lambda args: hamtaDelagareFranEntry())

EntMaskinnummer = Entry(home, width=5, text ="Maskinnummer") 
EntMaskinnummer.grid(row=1, column=3, pady=(50,0), padx=(22,0), sticky=W)
EntMaskinnummer.bind("<KeyRelease>", lambda args: hamtaMaskinerFranEntry())

BtnNyDelagare = Button (home, text ="Lägg till delägare", height = 1, command = lambda: laggTillAndraDelagare("Ny"))
BtnNyDelagare.grid(row = 4, column = 2, pady=(5,0))

LbDelagare = Listbox(home, width = 60, height = 30, exportselection=0)
LbDelagare.grid(row = 2, column = 1, columnspan = 2, rowspan = 2, padx=(300,0), pady=(5,0))
LbDelagare.bind('<<ListboxSelect>>', hamtaAllaMaskiner)
LbDelagare.bind('<Double-Button>', fyllDelagarInfoMedNummer)

LbMaskiner = Listbox(home, width = 60, height = 30, exportselection=0)
LbMaskiner.grid(row = 2, column = 3, columnspan = 2, rowspan = 2, padx=(20,0), pady=(5,0))
LbMaskiner.bind('<Double-Button>', lambda x=None: fyllMaskinInfo("franDelagare"))

ScbDelagare = Scrollbar(home, orient="vertical")
ScbDelagare.grid(row = 2, column = 2, sticky = N+S+E, rowspan = 2, pady=(10,0))
ScbDelagare.config(command =LbDelagare.yview)

ScbDMaskiner = Scrollbar(home, orient="vertical")
ScbDMaskiner.grid(row = 2, column = 4, sticky = N+S+E, rowspan = 2, pady=(10,0))
ScbDMaskiner.config(command =LbMaskiner.yview)

LbDelagare.config(yscrollcommand=ScbDelagare.set)
LbMaskiner.config(yscrollcommand=ScbDMaskiner.set)

#frames

delagare.columnconfigure(1, weight=1)
delagare.rowconfigure(0, weight=1)

frameDelagare = Frame(delagare, highlightbackground="grey", highlightthickness=1)
frameDelagare.grid(row = 0, column = 0, sticky = NW, padx=(10,0), pady=(10,0))
frameMaskiner= Frame(delagare)
frameMaskiner.grid(row = 1, column =0, sticky = N+E+W, padx=(10,0), pady=(10,0))
frameOvrigText= Frame(delagare)
frameOvrigText.grid(row=2, column=0, sticky=NSEW, padx=(10,0), pady=(10,0))
frameMaskininfo = Frame(delagare)
frameMaskininfo.grid(row = 0, column =1, rowspan = 3, sticky = NSEW, pady=(10,0))

#Listbox, maskiner tillhörande delägare
LbDelagaresMaskiner = Listbox(frameMaskiner, width = 45, height = 12, exportselection=0)
LbDelagaresMaskiner.grid(row = 1, column = 0)
LbDelagaresMaskiner.grid_rowconfigure(1, weight=1)
LbDelagaresMaskiner.grid_columnconfigure(0, weight=1)
LbDelagaresMaskiner.bind('<<ListboxSelect>>', lambda x=None: fyllMaskinInfo("franMaskiner"))

lblDelagareMaskiner = Label(frameMaskiner, text = "Delägarens maskiner")
lblDelagareMaskiner.grid(row=0, column=0, sticky=NW)

#Scrollbar
ScbLbDelagaresMaskiner = Scrollbar(frameMaskiner, orient="vertical")
ScbLbDelagaresMaskiner.grid(row = 1, column = 0, sticky = N+S+E)
ScbLbDelagaresMaskiner.config(command =LbMaskiner.yview)

LbDelagaresMaskiner.config(yscrollcommand=ScbLbDelagaresMaskiner.set)

#Maskinbild
img = Image.open("1.jpg")  
img = img.resize((225,200), Image. ANTIALIAS)
img4 = ImageTk.PhotoImage(img)
img_label = Label(frameOvrigText, image=img4)
img_label.grid(row=0, column=0, sticky = NW)


#Delägareinfo

lblMedlemsnummer = Label(frameDelagare, text = "Medlemsnr.")
lblMedlemsnummer.grid(row = 1, column = 0, sticky=W, pady=(0,8))
txtMedlemsnummerDelagare = Text(frameDelagare, width = 5, height=0.1)
txtMedlemsnummerDelagare.grid(row = 1, column =1, sticky = W)
txtMedlemsnummerDelagare.config(state=DISABLED)

entSokMedlem = Entry(frameDelagare, width = 5)
entSokMedlem.grid(row = 1, column =1, sticky=E, padx=(40, 50))
btnSokMedlem = Button(frameDelagare, text = "Sök", command= lambda: hamtaDelagare(entSokMedlem.get()))
btnSokMedlem.grid(row =1, column = 1, sticky=E, padx=(0,10))

lblForetag = Label(frameDelagare, text = "Företag")
lblForetag.grid(row = 2, column = 0, sticky=W, pady=(0,8))
txtForetag = Text(frameDelagare, width = 25, height=0.1)
txtForetag.grid(row = 2, column =1, sticky = W)
txtForetag.config(state=DISABLED)

lblFornamn = Label(frameDelagare, text = "Förnamn")
lblFornamn.grid(row = 3, column = 0, sticky=W, pady=(0,8))
txtFornamn = Text(frameDelagare, width = 25, height=0.1)
txtFornamn.grid(row = 3, column =1, sticky = W)
txtFornamn.config(state=DISABLED)

lblEfternamn = Label(frameDelagare, text = "Efternamn")
lblEfternamn.grid(row = 4, column = 0, sticky=W, pady=(0,8))
txtEfternamn = Text(frameDelagare, width = 25, height=0.1)
txtEfternamn.grid(row = 4, column =1, sticky = W)
txtEfternamn.config(state=DISABLED)

lblAdress = Label(frameDelagare, text = "Adress")
lblAdress.grid(row = 5, column = 0, sticky=W, pady=(0,8))
txtAdress = Text(frameDelagare, width = 25, height=0.1)
txtAdress.grid(row = 5, column =1, sticky = W)
txtAdress.config(state=DISABLED)

lblPostnummer = Label(frameDelagare, text = "Postnummer")
lblPostnummer.grid(row = 6, column = 0, sticky=W, pady=(0,8))
txtPostnummer = Text(frameDelagare, width = 25, height=0.1)
txtPostnummer.grid(row = 6, column =1, sticky = W)
txtPostnummer.config(state=DISABLED)

lblPostadress = Label(frameDelagare, text = "Ort")
lblPostadress.grid(row = 7, column = 0, sticky=W, pady=(0,8))
txtPostadress = Text(frameDelagare, width = 25, height=0.1)
txtPostadress.grid(row = 7, column =1, sticky = W)
txtPostadress.config(state=DISABLED)

lblTelefon = Label(frameDelagare, text = "Telefon")
lblTelefon.grid(row = 8, column = 0, sticky=W, pady=(0,8))
txtTelefon = Text(frameDelagare, width = 25, height=0.1)
txtTelefon.grid(row = 8, column =1, sticky = W, padx=(0,4))
txtTelefon.config(state=DISABLED)

btnAndraDelagare = Button(frameDelagare, text ="Ändra", command = lambda: laggTillAndraDelagare("Ändra"))
btnAndraDelagare.grid(row=9, column=1, sticky=W, padx=(55,0), pady=(0,5))

btnTaBortDelagare = Button(frameDelagare, text="Ta bort delägare", command = lambda: taBortDelagare())
btnTaBortDelagare.grid(row=9, column =1, sticky=E, padx=(0,5), pady=(0,5))

#Maskininfo

lblMaskinnummermaskininfo = Label(frameMaskininfo, text= "Maskinnummer")
lblMaskinnummermaskininfo.grid(column = 0, row = 0, sticky = W, padx=(10,0), pady=(0,8))
entMaskinnummermaskininfo = Entry(frameMaskininfo, width = 5)
entMaskinnummermaskininfo.grid(column =1, row =0, sticky = W, padx=(10,0))
entMaskinnummermaskininfo.config(state=DISABLED)

lblMaskinbeteckning = Label(frameMaskininfo, text="Beteckning")
lblMaskinbeteckning.grid(column = 0, row=1, sticky = W, padx=(10,0), pady=(0,8))
entMaskinbeteckning = Entry(frameMaskininfo, width = 32)
entMaskinbeteckning.grid(column=1, row=1, sticky = W, padx=(10,0))
entMaskinbeteckning.config(state=DISABLED)

lblMaskinme_klass = Label(frameMaskininfo, text="ME-Klass")
lblMaskinme_klass.grid(column=0, row=2, sticky = W, padx=(10,0), pady=(0,8))
entMaskinme_klass = Entry(frameMaskininfo, width = 32)
entMaskinme_klass.grid(column=1, row=2, sticky = W, padx=(10,0))
entMaskinme_klass.config(state=DISABLED)

lblMaskinmotorfabrikat = Label(frameMaskininfo, text="Motorfabrikat")
lblMaskinmotorfabrikat.grid(column=0, row=3, sticky = W, padx=(10,0), pady=(0,8))
entMaskinmotorfabrikat = Entry(frameMaskininfo, width = 32)
entMaskinmotorfabrikat.grid(column=1, row=3, sticky=W, padx=(10,0))
entMaskinmotorfabrikat.config(state=DISABLED)

lblMaskinmotortyp = Label(frameMaskininfo, text="Motortyp")
lblMaskinmotortyp.grid(column=0, row=4, sticky = W, padx=(10,0), pady=(0,8))
entMaskinmotortyp=Entry(frameMaskininfo, width = 32)
entMaskinmotortyp.grid(column=1, row=4, sticky=W, padx=(10,0))
entMaskinmotortyp.config(state=DISABLED)

lblMaskinmotor = Label(frameMaskininfo, text="Motor")
lblMaskinmotor.grid(column=0, row=5, sticky = W, padx=(10,0), pady=(0,8))
entMaskinmotor = Entry(frameMaskininfo, width = 32)
entMaskinmotor.grid(column=1, row=5, sticky=W, padx=(10,0))
entMaskinmotor.config(state=DISABLED)

lblMaskinvaxellada = Label(frameMaskininfo, text="Växellåda")
lblMaskinvaxellada.grid(column=0, row=6, sticky = W, padx=(10,0), pady=(0,8))
entMaskinvaxellada=Entry(frameMaskininfo, width = 32)
entMaskinvaxellada.grid(column=1, row=6, sticky=W, padx=(10,0))
entMaskinvaxellada.config(state=DISABLED)

lblMaskinhydraulsystem = Label(frameMaskininfo, text="Hydraulsystem")
lblMaskinhydraulsystem.grid(column=0, row=7, sticky = W, padx=(10,0), pady=(0,8))
entMaskinhydraulsystem=Entry(frameMaskininfo, width = 32)
entMaskinhydraulsystem.grid(column=1, row=7, sticky=W, padx=(10,0))
entMaskinhydraulsystem.config(state=DISABLED)

lblMaskinkylvatska = Label(frameMaskininfo, text="Kylvätska")
lblMaskinkylvatska.grid(column=0, row=8, sticky = W, padx=(10,0), pady=(0,8))
entMaskinkylvatska=Entry(frameMaskininfo, width = 32)
entMaskinkylvatska.grid(column=1, row=8, sticky=W, padx=(10,0))
entMaskinkylvatska.config(state=DISABLED)

lblMaskinmotoreffekt = Label(frameMaskininfo, text="Motoreffekt/KW")
lblMaskinmotoreffekt.grid(column=0, row=9, sticky = W, padx=(10,0), pady=(0,8))
entMaskinmotoreffekt=Entry(frameMaskininfo, width = 32)
entMaskinmotoreffekt.grid(column=1, row=9, sticky=W, padx=(10,0))
entMaskinmotoreffekt.config(state=DISABLED)

lblMaskinmotorvarmare = Label(frameMaskininfo, text="Motorvärmare")
lblMaskinmotorvarmare.grid(column=0, row=10, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinmotorvarmare = ttk.Checkbutton(frameMaskininfo)
cbMaskinmotorvarmare.state(['!alternate', '!selected', 'disabled'])
cbMaskinmotorvarmare.grid(column = 1, row = 10, sticky = W, padx=(5,0))

lblMaskinkatalysator = Label(frameMaskininfo, text="Katalysator")
lblMaskinkatalysator.grid(column=0, row=11, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinkatalysator = ttk.Checkbutton(frameMaskininfo)
cbMaskinkatalysator.state(['!alternate', '!selected', 'disabled'])
cbMaskinkatalysator.grid(column = 1, row = 11, sticky = W, padx=(5,0))

lblMaskinpartikelfilter = Label(frameMaskininfo, text="Partikelfilter")
lblMaskinpartikelfilter.grid(column=0, row=12, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinpartikelfilter = ttk.Checkbutton(frameMaskininfo)
cbMaskinpartikelfilter.state(['!alternate', '!selected', 'disabled'])
cbMaskinpartikelfilter.grid(column = 1, row = 12, sticky = W, padx=(5,0))

lblMaskinvattenbaseradlack = Label(frameMaskininfo, text="Vattenbaserad lack")
lblMaskinvattenbaseradlack.grid(column=0, row=13, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinvattenbaseradlack = ttk.Checkbutton(frameMaskininfo)
cbMaskinvattenbaseradlack.state(['!alternate', '!selected', 'disabled'])
cbMaskinvattenbaseradlack.grid(column = 1, row = 13, sticky = W, padx=(5,0))

lblMaskinkylmedia = Label(frameMaskininfo, text="Kylmedia")
lblMaskinkylmedia.grid(column=0, row=14, sticky = W, padx=(10,0), pady=(0,8))
entMaskinkylmedia=Entry(frameMaskininfo, width = 32)
entMaskinkylmedia.grid(column=1, row=14, sticky=W, padx=(10,0))
entMaskinkylmedia.config(state=DISABLED)

lblMaskinbullernivautv = Label(frameMaskininfo, text="Bullernivå utvändigt")
lblMaskinbullernivautv.grid(column=0, row=15, sticky = W, padx=(10,0), pady=(0,8))
entMaskinbullernivautv=Entry(frameMaskininfo, width = 32)
entMaskinbullernivautv.grid(column=1, row=15, sticky=W, padx=(10,0))
entMaskinbullernivautv.config(state=DISABLED)

lblMaskinbullernivainv = Label(frameMaskininfo, text="Bullernivå invändigt")
lblMaskinbullernivainv.grid(column=0, row=16, sticky = W, padx=(10,0), pady=(0,8))
entMaskinbullernivainv=Entry(frameMaskininfo, width = 32)
entMaskinbullernivainv.grid(column=1, row=16, sticky=W, padx=(10,0))
entMaskinbullernivainv.config(state=DISABLED)

lblMaskinsmorjfett = Label(frameMaskininfo, text="Smörjfett")
lblMaskinsmorjfett.grid(column=0, row=17, sticky = W, padx=(10,0), pady=(0,8))
entMaskinsmorjfett=Entry(frameMaskininfo, width = 32)
entMaskinsmorjfett.grid(column=1, row=17, sticky=W, padx=(10,0))
entMaskinsmorjfett.config(state=DISABLED)

lblMaskinBatterityp = Label(frameMaskininfo, text="Batterityp")
lblMaskinBatterityp.grid(column=0, row=18, sticky = W, padx=(10,0), pady=(0,8))
entMaskinBatterityp=Entry(frameMaskininfo, width = 20)
entMaskinBatterityp.grid(column=1, row=18, sticky=W, padx=(10,0))
entMaskinBatterityp.config(state=DISABLED)

lblMaskinBatteriantal = Label(frameMaskininfo, text="Antal")
lblMaskinBatteriantal.grid(column=1, row=18, sticky=E, padx=(0,35))
entMaskinBatteriantal = Entry(frameMaskininfo, width=5)
entMaskinBatteriantal.grid(column=1, row=18, sticky=E)
entMaskinBatteriantal.config(state=DISABLED)

#checkbox
lblMaskinKollektivforsakring = Label(frameMaskininfo, text="Kollektiv försäkring")
lblMaskinKollektivforsakring.grid(column=0, row=19, sticky = W, padx=(10,0), pady=(0,8))
cbMaskinKollektivforsakring = ttk.Checkbutton(frameMaskininfo)
cbMaskinKollektivforsakring.state(['!alternate', '!selected', 'disabled'])
cbMaskinKollektivforsakring.grid(column = 1, row = 19, sticky = W, padx=(5,0))

lblMaskinperiod = Label(frameMaskininfo, text="Period")
lblMaskinperiod.grid(column=0, row=20, sticky = W, padx=(10,0), pady=(0,8))
deMaskinperiod1 = DateEntry(frameMaskininfo, values="Text", date_pattern="yyyy-mm-dd")
deMaskinperiod1.delete(0, 'end')
deMaskinperiod1.grid(column=1, row=20, sticky=W, padx=(10,0))


deMaskinperiod2 = DateEntry(frameMaskininfo, values="Text", date_pattern="yyyy-mm-dd")
deMaskinperiod2.delete(0, 'end')
deMaskinperiod2.grid(column=1, row=20, sticky=E)


lblMaskinarsbelopp = Label(frameMaskininfo, text="Årsbelopp")
lblMaskinarsbelopp.grid(column=0, row=21, sticky = W, padx=(10,0), pady=(0,8))
entMaskinarsbelopp=Entry(frameMaskininfo, width = 32)
entMaskinarsbelopp.grid(column=1, row=21, sticky=W, padx=(10,0))
entMaskinarsbelopp.config(state=DISABLED)

#Buttons

btnMaskinpresentation=Button(frameMaskininfo,text="Maskinpresentation", command = lambda: maskinpresentation(entMaskinnummermaskininfo()))
btnMaskinpresentation.grid(column=0, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnMiljodeklaration=Button(frameMaskininfo, text="Miljödeklaration", command = lambda: miljodeklaration(entMaskinnummermaskininfo.get()))
btnMiljodeklaration.grid(column=1, row=22, sticky=W, padx=(10,0), pady=(20,0))

btnHistorik=Button(frameMaskininfo, text="Historik", command = lambda: historikFonster(entMaskinnummermaskininfo.get()))
btnHistorik.grid(column=6, row=0, sticky=W, padx=(10,10))

btnLaggtillmaskin=Button(frameMaskininfo, text="Lägg till ny", command = lambda: nyMaskinFonster("Ny",entMaskinnummermaskininfo.get(), txtMedlemsnummerDelagare.get(1.0, END)))
btnLaggtillmaskin.grid(column=4, row=22, sticky=W, pady=(20,0))

btnAndramaskin=Button(frameMaskininfo, text="Ändra", command = lambda: nyMaskinFonster(entMaskinnummermaskininfo.get(),entMaskinnummermaskininfo.get(), txtMedlemsnummerDelagare.get(1.0, END)))
btnAndramaskin.grid(column=4, row=22,sticky=E, pady=(20,0))

btnBytmaskin=Button(frameMaskininfo, text="Byt maskin", command = lambda: nyMaskinFonster("Byt",entMaskinnummermaskininfo.get(), txtMedlemsnummerDelagare.get(1.0, END)))
btnBytmaskin.grid(column=5, row=22, padx=(0,60), pady=(20,0))

btnTabortmaskin=Button(frameMaskininfo, text="Ta bort maskin", command  = lambda: taBortMaskin(entMaskinnummermaskininfo.get()))
btnTabortmaskin.grid(column=5, row=22, sticky=E, pady=(20,0))



#--------------------

lblMaskinmiljostatus = Label(frameMaskininfo, text="Miljöstatus")
lblMaskinmiljostatus.grid(column=2, row=0, sticky = W, padx=(10,0))
entMaskinmiljostatus=Entry(frameMaskininfo, width = 32)
entMaskinmiljostatus.grid(column=3, row=0, sticky=W, padx=(10,0))
entMaskinmiljostatus.config(state=DISABLED)

lblMaskinarsmodell = Label(frameMaskininfo, text="Årsmodell")
lblMaskinarsmodell.grid(column=2, row=1, sticky = W, padx=(10,0))
entMaskinarsmodell=Entry(frameMaskininfo, width = 32)
entMaskinarsmodell.grid(column=3, row=1, sticky=W, padx=(10,0))
entMaskinarsmodell.config(state=DISABLED)

lblMaskinregistreringsnummer = Label(frameMaskininfo, text="Reg. nr/Ser. nr")
lblMaskinregistreringsnummer.grid(column=2, row=2, sticky = W, padx=(10,0))
entMaskinregistreringsnummer=Entry(frameMaskininfo, width = 32)
entMaskinregistreringsnummer.grid(column=3, row=2, sticky=W, padx=(10,0))
entMaskinregistreringsnummer.config(state=DISABLED)

lblMaskintyp = Label(frameMaskininfo, text="Maskintyp")
lblMaskintyp.grid(column=2, row=3, sticky = W, padx=(10,0))
entMaskintyp=Entry(frameMaskininfo, width = 32)
entMaskintyp.grid(column=3, row=3, sticky=W, padx=(10,0))
entMaskintyp.config(state=DISABLED)

lblMaskinmotoroljevolym  = Label(frameMaskininfo, text="Motorolja volym/liter")
lblMaskinmotoroljevolym.grid(column=2, row=5, sticky = W, padx=(10,0))
entMaskinmotoroljevolym=Entry(frameMaskininfo, width = 32)
entMaskinmotoroljevolym.grid(column=3, row=5, sticky=W, padx=(10,0))
entMaskinmotoroljevolym.config(state=DISABLED)

lblMaskinvaxelladevolym = Label(frameMaskininfo, text="Växellåda volym/liter")
lblMaskinvaxelladevolym.grid(column=2, row=6, sticky = W, padx=(10,0))
entMaskinvaxelladevolym=Entry(frameMaskininfo, width = 32)
entMaskinvaxelladevolym.grid(column=3, row=6, sticky=W, padx=(10,0))
entMaskinvaxelladevolym.config(state=DISABLED)

lblMaskinhydraulsystemvolym = Label(frameMaskininfo, text="Hydraul volym/liter")
lblMaskinhydraulsystemvolym.grid(column=2, row=7, sticky = W, padx=(10,0))
entMaskinhydraulsystemvolym=Entry(frameMaskininfo, width = 32)
entMaskinhydraulsystemvolym.grid(column=3, row=7, sticky=W, padx=(10,0))
entMaskinhydraulsystemvolym.config(state=DISABLED)

lblMaskinkylvatskavolym = Label(frameMaskininfo, text="Kylvätska volym/liter")
lblMaskinkylvatskavolym.grid(column=2, row=8, sticky = W, padx=(10,0))
entMaskinkylvatskavolym=Entry(frameMaskininfo, width = 32)
entMaskinkylvatskavolym.grid(column=3, row=8, sticky=W, padx=(10,0))
entMaskinkylvatskavolym.config(state=DISABLED)

#Textruta, fält för Övrig Text
lblOvrigtext = Label(frameMaskininfo, text="Övrig text")
lblOvrigtext.grid(column=2, row=9, sticky=W, padx=(10,0))
TxtOvrigtext = Text(frameMaskininfo, width = 20, height=4)
TxtOvrigtext.grid(row=10, column=2, columnspan=2, rowspan=3, sticky=NSEW, padx=(10,15))
TxtOvrigtext.config(state=DISABLED)

#Scrollbar
ScbTxtOvrigText = Scrollbar(frameMaskininfo, orient="vertical")
ScbTxtOvrigText.grid(row = 10, column = 3, sticky = N+S+E, rowspan = 3)
ScbTxtOvrigText.config(command =TxtOvrigtext.yview)

TxtOvrigtext.config(yscrollcommand=ScbTxtOvrigText.set)

#------------------------

lblMaskinbransle = Label(frameMaskininfo, text="Bränsle")
lblMaskinbransle.grid(column=4, row=0, sticky = W, padx=(10,0))
entMaskinbransle=Entry(frameMaskininfo, width = 32)
entMaskinbransle.grid(column=5, row=0, sticky=W, padx=(10,0))
entMaskinbransle.config(state=DISABLED)

lblMaskindackfabrikat = Label(frameMaskininfo, text="Däckfabrikat")
lblMaskindackfabrikat.grid(column=4, row=1, sticky = W, padx=(10,0))
entMaskindackfabrikat=Entry(frameMaskininfo, width = 32)
entMaskindackfabrikat.grid(column=5, row=1, sticky=W, padx=(10,0))
entMaskindackfabrikat.config(state=DISABLED)

lblMaskindimension = Label(frameMaskininfo, text="Dimension/typ")
lblMaskindimension.grid(column=4, row=2, sticky = W, padx=(10,0))
entMaskindimension=Entry(frameMaskininfo, width = 32)
entMaskindimension.grid(column=5, row=2, sticky=W, padx=(10,0))
entMaskindimension.config(state=DISABLED)

#Checkbox
lblMaskinregummerbara = Label(frameMaskininfo, text="Regummerbara")
lblMaskinregummerbara.grid(column=4, row=3, sticky = W, padx=(10,0))
cbMaskinregummerbara = ttk.Checkbutton(frameMaskininfo)
cbMaskinregummerbara.state(['!alternate', '!selected', 'disabled'])
cbMaskinregummerbara.grid(column = 5, row = 3, sticky = W, padx=(5,0))

#Checkbox
lblMaskinregummerade = Label(frameMaskininfo, text="Regummerade")
lblMaskinregummerade.grid(column=4, row=4, sticky = W, padx=(10,0))
cbMaskinregummerade = ttk.Checkbutton(frameMaskininfo)
cbMaskinregummerade.state(['!alternate', '!selected', 'disabled'])
cbMaskinregummerade.grid(column = 5, row = 4, sticky = W, padx=(5,0))

lblMaskingasolanlaggning = Label(frameMaskininfo, text="Gasolanläggning")
lblMaskingasolanlaggning.grid(column=4, row=5, sticky = W, padx=(10,0))
cbMaskingasolanlaggning = ttk.Checkbutton(frameMaskininfo)
cbMaskingasolanlaggning.state(['!alternate', '!selected', 'disabled'])
cbMaskingasolanlaggning.grid(column = 5, row = 5, sticky = W, padx=(5,0))

lblMaskinSaneringsvatska = Label(frameMaskininfo, text="Saneringsvätska")
lblMaskinSaneringsvatska.grid(column=4, row=6, sticky = W, padx=(10,0))
cbMaskinSaneringsvatska = ttk.Checkbutton(frameMaskininfo)
cbMaskinSaneringsvatska.state(['!alternate', '!selected', 'disabled'])
cbMaskinSaneringsvatska.grid(column = 5, row = 6, sticky = W, padx=(5,0))

#Checkbox
lblMaskininsattserlagd = Label(frameMaskininfo, text="Maskininsats erlagd")
lblMaskininsattserlagd.grid(column=4, row=7, sticky = W, padx=(10,0))
cbMaskininsatserlagd = ttk.Checkbutton(frameMaskininfo)
cbMaskininsatserlagd.state(['!alternate', '!selected', 'disabled'])
cbMaskininsatserlagd.grid(column = 5, row = 7, sticky = W, padx=(5,0))

lblMaskinforare = Label(frameMaskininfo, text="Förare")
lblMaskinforare.grid(column=4, row=8, sticky = W, padx=(10,0))
entMaskinforare=Entry(frameMaskininfo, width = 32)
entMaskinforare.grid(column=5, row=8, sticky=W, padx=(10,0))
entMaskinforare.config(state=DISABLED)

lblMaskinreferens = Label(frameMaskininfo, text="Referensjobb")
lblMaskinreferens.grid(column=4, row=9, sticky =W, padx=(10,0))
lbMaskinreferens=Listbox(frameMaskininfo, width = 20, height=5)
lbMaskinreferens.grid(column=4, row=10, sticky=NSEW, padx=(10,0), columnspan=2, rowspan=3)

#Scrollbar
ScbTxtMaskinreferens = Scrollbar(frameMaskininfo, orient="vertical")
ScbTxtMaskinreferens.grid(row = 10, column = 6, sticky = W+N+S, rowspan = 3)
ScbTxtMaskinreferens.config(command =LbMaskiner.yview)

lbMaskinreferens.config(yscrollcommand=ScbTxtMaskinreferens.set)

#Listbox
lblMaskintillbehor = Label(frameMaskininfo, text="Tillbehör")
lblMaskintillbehor.grid(column=4, row=14, sticky = W, padx=(10,0))
lbMaskintillbehor=Listbox(frameMaskininfo)
lbMaskintillbehor.grid(column=4, row=15, rowspan=6, columnspan=2,sticky=NSEW, padx=(10,0))

#Scrollbar
ScbLbMaskintillbehor = Scrollbar(frameMaskininfo, orient="vertical")
ScbLbMaskintillbehor.grid(row = 15, column = 6, sticky = N+W+S, rowspan = 6)
ScbLbMaskintillbehor.config(command =lbMaskintillbehor.yview)

lbMaskintillbehor.config(yscrollcommand=ScbLbMaskintillbehor.set)

#Förare
lblForare = Label(forare, text="Förare i systemet")
lblForare.grid(column=0, row=0, sticky=N, pady=(10,0), padx=(10,0))
lbForare = Listbox(forare, width=48, height=25, exportselection=0)
lbForare.grid(column=0, row=1, padx=(10, 0), pady=(10,0))
lbForare.bind('<<ListboxSelect>>', hamtaReferenser)

lblReferenser = Label(forare, text="Förarens referenser")
lblReferenser.grid(column=1, row=0, sticky=N, pady=(10,0))
lbReferenser = Listbox(forare, width=60, height=25)
lbReferenser.grid(column=1, row=1, padx=(10, 0), pady=(10,0))

entLaggTillForare = Entry(forare, width=48)
entLaggTillForare.grid(column=0, row=2, padx=(10,0), pady=(10,0), sticky =W)
btnLaggTillForare = Button(forare, text="Lägg till förare", command = lambda: laggTillForare(entLaggTillForare.get()))
btnLaggTillForare.grid(column=0, row=3, sticky=W, pady=(10,0), padx=(10,0))
btnTaBortForare = Button(forare, text="Ta bort förare", command = lambda: taBortForare())
btnTaBortForare.grid(column=0, row=3, sticky=E, pady=(10,0), padx=(0, 94))

entLaggTillReferens = Entry(forare, width=60)
entLaggTillReferens.grid(column=1, row=2, padx=(10,0), pady=(10,0), sticky = W)
btnLaggTillReferens = Button(forare, text="Lägg till referens", command=lambda: laggTillReferens(entLaggTillReferens.get()))
btnLaggTillReferens.grid(column=1, row=3, sticky=W, pady=(10,0), padx=(10,0))
btnTaBortReferens = Button(forare, text="Ta bort referens", command=lambda:taBortReferens())
btnTaBortReferens.grid(column=1, row=3, sticky=E, pady=(10,0), padx=(0,150))

lblForareDelagareMaskiner = Label(forare, text = "Maskiner")
lblForareDelagareMaskiner.grid(row=0, column=2, pady=(10,0), padx=(10,0))

LbForareDelagaresMaskiner = Listbox(forare, width = 60, height = 25, exportselection=0)
LbForareDelagaresMaskiner.grid(row = 1, column = 2, pady=(10,0), padx=(10,0), sticky=W)
LbForareDelagaresMaskiner.grid_rowconfigure(1, weight=1)
LbForareDelagaresMaskiner.grid_columnconfigure(0, weight=1)

btnKopplaMaskin = Button(forare, text ="Koppla förare till maskin", command=lambda: kopplaMaskin())
btnKopplaMaskin.grid(row=3, column=2, sticky=W, pady=(10,0), padx=(10,0))

btnKopplaBortMaskin = Button(forare, text="Koppla bort förare från maskin", command=lambda: kopplaBortMaskin())
btnKopplaBortMaskin.grid(row=1, column=3, sticky=NW, pady=(38,0), padx=(10,0))

lblKoppladMaskin = Label(forare, text ="Markerad förare är kopplad till maskin:")
lblKoppladMaskin.grid(row=0, column=3, pady=(10,0), padx=(10,0))
entKoppladMaskin = Entry(forare, width = 5)
entKoppladMaskin.grid(row=1, column=3, pady=(10,0), padx=(10,0), sticky=NW)

#Försäkring

forsakringBytFrame = Frame (forsakring)
forsakringNyPremieFrame = Frame(forsakring)

forsakringBytFrame.grid(column=0, row=0)
forsakringNyPremieFrame.grid(column=0, row=1, sticky=W, pady=(150,0), padx=(10,0))

lblNuvarandeForsakring = Label(forsakringBytFrame, text="Nuvarande försäkring: ")
lblNuvarandeForsakring.grid(column=0, row=0, sticky=W, padx=(10,0), pady=(10,0))

txtNuvarandeForsakring = Text(forsakringBytFrame, height=1, width = 32)
txtNuvarandeForsakring.grid(column=1, row=0, sticky=W, padx=(10,0), pady=(10,0))

btnBytforsakring = Button(forsakringBytFrame, text="Byt försäkring", command=lambda:bytForsakring())
btnBytforsakring.grid(column=2, row=0, padx=(10,0), pady=(10,0))

lblnyttStartDatum = Label(forsakringNyPremieFrame, text="Nytt startdatum")
lblnyttStartDatum.grid(column=0, row=0)

lblnyttSlutDatum = Label(forsakringNyPremieFrame, text="Nytt slutdatum")
lblnyttSlutDatum.grid(column=1, row=0)

denyttStartDatum = DateEntry(forsakringNyPremieFrame, values = "Text", date_pattern="yyyy-mm-dd" )
denyttStartDatum.delete(0, END)
denyttStartDatum.grid(column=0, row=1)

denyttSlutDatum = DateEntry(forsakringNyPremieFrame, values = "Text", date_pattern="yyyy-mm-dd" )
denyttSlutDatum.delete(0,END)
denyttSlutDatum.grid(column=1, row=1, padx=(3,0))

lblnyArsPremie = Label(forsakringNyPremieFrame, text="Nya årspremien.")
lblnyArsPremie.grid(column=0, row=2, pady=(10,0))

entnyArsPremie = Entry(forsakringNyPremieFrame, width=15, validate="key", validatecommand=(validera, "%P"))
entnyArsPremie.grid(column=0, row=3, pady=(10,10))

btnUppdateraForsakringsInformation = Button(forsakringNyPremieFrame, text="Uppdatera försäkringsinfot.", command=lambda:uppdateraForsakring())
btnUppdateraForsakringsInformation.grid(column=0, row=4, pady=(0,10), columnspan=2, sticky=W)

#Funktioner som körs på uppstart
hamtaForare()
fyllListboxDelagare()
hamtaMaskinerFranEntry()
hamtaForsakring()
hamtaForareMaskin()

# kör fönstret
root.mainloop()