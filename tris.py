#Gioco Tris in Python con AppJar, Funzioni, OOP e FIle
from datetime import date
import os
import shutil
from appJar import gui
import random
app=gui("Tris")
app.setResizable(False)
app.setSize(400,400)
app.setLocation(x=350,y=150)
app.setBg("lightblue")


#Classe Tris per pulsanti Tris
class Tris(object):
    def __init__(self,giocatore):
        self.giocatore=giocatore

#Classe punteggio per tenere conto dei punti
class Punteggio(object):
    def __init__(self,vit1,vit2,rounddafare,roundfatti):
        self.vit1=vit1
        self.vit2=vit2
        self.rounddafare=rounddafare
        self.roundfatti=roundfatti
        
    #Metodo Recosonto per resoconto punteggio
    def resoconto(self):
        global nome1
        global nome2
        global data
        app.removeAllWidgets()
        app.addLabel("s","Resoconto Partita",0,0,colspan=4)
        app.setLabelBg("s","orange")
        app.addLabel("rf","Round Giocati = "+(str(self.roundfatti))+"/"+str(self.rounddafare),1,0)
        app.addLabel("nomi","Giocatori = "+nome1+" e "+nome2,2,0)
        app.addLabel("v1","Partite Vinte da "+nome1+" = "+str(self.vit1),3,0)
        app.addLabel("v2","Partite Vinte da "+nome2+" = "+str(self.vit2),4,0)
        app.addLabel("v3","Partite Pari = "+str(self.roundfatti-(self.vit1+self.vit2)),5,0)

        mesi=["01:Gennaio","02:Febbraio","03:Marzo","04:Aprile","05:Maggio","06:Giugno","07:Luglio","08:Agosto","09:Settembre","10:Ottobre","11:Novembre","12:Dicembre"]
        today = str(date.today())
        mes=today.split("-")[1]
        i=0
        for i in range(len(mesi)):
            if (mesi[i].split(":")[0]) == mes:
                mese=mesi[i].split(":")[1]

        if today.split("-")[2][0]=="0":
            numero=today.split("-")[2][1]
        else:
            numero=today.split("-")[2]

        data=numero+" "+mese+" "+today.split("-")[0]
        app.addLabel("data","Data Partita = "+data,6,0)
        if punto.roundfatti < punto.rounddafare:
            app.addButtons(["Prossimo Round","Salva Dati Partita","Torna alla Home"],press,7,0)
        else:
            app.addButtons(["Salva Dati Partita","Torna alla Home"],press,7,0)

    #Metodo Salva per salvare il punteggio
    def salva(self):
        global nome1
        global nome2
        global data
        file=open("partite.txt","a")
        file.write("Round Giocati = "+(str(self.roundfatti))+"/"+str(self.rounddafare)+",Giocatori = "+nome1+" e "+nome2+","+"Partite Vinte da "+nome1+" = "+str(self.vit1)+","+"Partite Vinte da "+nome2+" = "+str(self.vit2)+","+"Partite Pari = "+str(self.roundfatti-(self.vit1+self.vit2))+","+"Data Partita = "+data+",\n")
        file.close()
        app.removeButton("Salva Dati Partita")
        app.removeButton("Torna alla Home")
        try:
            app.removeButton("Prossimo Round")
        except:
            pass
        app.addButton("Torna alla Home",press,8,0)
        app.addLabel("conferma","Dati salvati!",7,0)


#Funzione principale per Menu e smistamento Pulsanti
def menu(ppp):
    if ppp=="Crediti":
        a="""..."""
        app.infoBox("Crediti", a, parent=None)
    if ppp=="Contatti":
        a="""...
"""
        app.infoBox("Contatti", a, parent=None)
    if ppp=="Esci":
        app.stop()
    if ppp=="Torna alla Home":
        home()
    if ppp=="Come si Gioca":
        a="""A turno i giocatori scelgono una cella vuota che verrà riempita con il proprio colore. Vince il giocatore che riesce a disporre tre del proprio colore in linea retta orizzontale, verticale o diagonale. Se la griglia viene riempita senza che nessuno dei giocatori sia riuscito a completare una linea retta di tre colori, il gioco finisce in parità."""
        app.infoBox("Come si Gioca", a, parent=None)
    if ppp=="Svuota Salvataggi":
        file=open("partite.txt","w")
        file.close()
        menu("Partite Salvate")
    if ppp=="Partite Salvate" or ppp=="Indietro":
        app.removeAllWidgets()
        app.addLabel("s","Partite Salvate",0,0,colspan=4)
        app.setLabelBg("s","orange")
        app.startScrollPane("PANE")
        try:
            file=open("partite.txt","r")
            leggi=file.readlines()
            i=0
            for i in range(len(leggi)):
                app.addLabel(str(i),leggi[i].split(",")[5].split("=")[1],i+1,0)
                app.addNamedButton("Visualizza",str(i),mostra,i+1,1)
            file.close()
            if len(leggi)==0:
                app.addLabel("avviso","Non sono presenti partite salvate al momento")
        except:
            app.addLabel("avviso","Non sono presenti partite salvate al momento")
        app.stopScrollPane()
        app.addButton("Torna alla Home",press)

#Funzione per mostrare un punteggio salvato
def mostra(p):
    app.removeAllWidgets()
    app.addLabel("s","Partita",0,0,colspan=4)
    app.setLabelBg("s","orange")
    #try:
    file=open("partite.txt","r")
    leggi=file.readlines()
    i=0
    for i in range(len(leggi[int(p)].split(","))):
        app.addLabel(str(i),leggi[int(p)].split(",")[i],i+1,0)

    file.close()
    app.addNamedButton("Elimina",str(p),elimina)
    app.addButton("Indietro",menu)
    #except:
        #pass

#Funzione per eliminare un punteggio salvato
def elimina(pp):
    #try:
    file=open("partite.txt","r")
    t=file.readlines()
    leggi=t
    file.close()
    file=open("partite.txt","w")
    i=0
    for i in range(len(leggi)):
        if i!=int(pp):
            file.write(leggi[i])

    file.close()
    menu("Partite Salvate")
    #except:
        #pass
                
#Funzione per realizzare gli eventi alla vincita
def win(v):
    global pulsanti
    global nome1
    global nome2
    global punto

    punto.roundfatti=punto.roundfatti+1
    
    i=0
    for i in range(len(pulsanti)):
        if pulsanti[i].giocatore==0:
            app.disableButton(str(i))

    if v==1:
        app.setLabel("turno","VINCE "+nome1)
        app.setLabelBg("turno","lightgreen")
        punto.vit1=punto.vit1+1
    elif v==2:
        app.setLabel("turno","VINCE "+nome2)
        app.setLabelBg("turno","violet")
        punto.vit2=punto.vit2+1
    elif v==0:
        app.setLabel("turno","PARI")
        app.setLabelBg("turno","white")

    if punto.roundfatti < punto.rounddafare:
        app.addButton("Prossimo Round",press,6,0)
        app.addButton("Resoconto Partita",press,6,1)
        app.addButton("Torna alla Home",press,6,2)
    else:
        app.addButtons(["Resoconto Partita","Torna alla Home"],press,6,1)

#Funzione per stabilire la vittoria e per calcolare la mossa del Computer
def check(pp):
    global turno
    global nome1
    global nome2
    global pulsanti
    global mode

    if (turno%2==0):
        pulsanti[int(pp)].giocatore=1
        app.setButtonBg(pp, "lightgreen")
        app.disableButton(pp)
        
        turno=turno+1
        app.setLabel("turno","Turno di "+nome2)
        app.setLabelBg("turno","violet")
    else:
        pulsanti[int(pp)].giocatore=2
        app.setButtonBg(pp, "violet")
        app.disableButton(pp)
        turno=turno+1
        app.setLabel("turno","Turno di "+nome1)
        app.setLabelBg("turno","lightgreen")

    i=0
    for i in range(len(pulsanti)):
        if pulsanti[i].giocatore==0:
            #try:
            app.enableButton(str(i))
            #except:
                #pass

    #Controllo possibile vincità o parità
    vinci=0
    i=0
    for i in range(3):
        if (pulsanti[0+(i*3)].giocatore==pulsanti[1+(i*3)].giocatore) and (pulsanti[0+(i*3)].giocatore==pulsanti[2+(i*3)].giocatore):
            if pulsanti[0+(i*3)].giocatore!=0:
                vinci=pulsanti[0+(i*3)].giocatore
                win(vinci)
                

    if vinci==0:
        i=0
        for i in range(3):
            if (pulsanti[0+i].giocatore==pulsanti[3+i].giocatore) and (pulsanti[0+i].giocatore==pulsanti[6+i].giocatore):
                if pulsanti[0+i].giocatore!=0:
                    vinci=pulsanti[0+i].giocatore
                    win(vinci)


    if vinci==0:
        if (pulsanti[0].giocatore==pulsanti[4].giocatore) and (pulsanti[0].giocatore==pulsanti[8].giocatore):
            if pulsanti[0].giocatore!=0:
                vinci=pulsanti[0].giocatore
                win(vinci)
        elif (pulsanti[2].giocatore==pulsanti[4].giocatore) and (pulsanti[2].giocatore==pulsanti[6].giocatore):
            if pulsanti[2].giocatore!=0:
                vinci=pulsanti[2].giocatore
                win(vinci)

    if vinci==0:
        i=0
        controllo=0
        for i in range(len(pulsanti)):
            #print(pulsanti[i].giocatore)
            if pulsanti[i].giocatore==0:
                controllo=1
                break

        if controllo==0:
            vinci=3
            win(0)

    #Generazione mossa del Computer
    if vinci==0:
        if (mode=="Contro il Computer") and ((turno%2==0)==False):

            i=0
            for i in range(len(pulsanti)):
                if pulsanti[i].giocatore==0:
                    app.disableButton(str(i))
            
            scelta=-1
            cambio=0
            cont=0
            obbiettivo=4
            for cont in range(3):
                if cont>0:
                    obbiettivo=2
                if cont==1:
                    cambio=0
                else:
                    cambio=1
                i=0
                who=0
                if scelta==-1:
                    for i in range(3):
                        if (pulsanti[0+(i*3)].giocatore+pulsanti[1+(i*3)].giocatore+pulsanti[2+(i*3)].giocatore)==obbiettivo:
                            if pulsanti[0+(i*3)].giocatore==1:
                                who=1
                            elif pulsanti[1+(i*3)].giocatore==1:
                                who=1
                            elif pulsanti[2+(i*3)].giocatore==1:
                                who=1

                            if (who==1) or (cambio==1):
                                if pulsanti[0+(i*3)].giocatore==0:
                                    scelta=0+(i*3)
                                    break
                                elif pulsanti[1+(i*3)].giocatore==0:
                                    scelta=1+(i*3)
                                    break
                                elif pulsanti[2+(i*3)].giocatore==0:
                                    scelta=2+(i*3)
                                    break
                            
                        
                if scelta==-1:
                    i=0
                    who=0
                    for i in range(3):
                        if (pulsanti[0+i].giocatore+pulsanti[3+i].giocatore+pulsanti[6+i].giocatore)==obbiettivo:
                            if pulsanti[0+i].giocatore==1:
                                who=1
                            elif pulsanti[3+i].giocatore==1:
                                who=1
                            elif pulsanti[6+i].giocatore==1:
                                who=1

                            if (who==1) or (cambio==1):
                                if pulsanti[0+i].giocatore==0:
                                    scelta=0+i
                                    break
                                elif pulsanti[3+i].giocatore==0:
                                    scelta=3+i
                                    break
                                elif pulsanti[6+i].giocatore==0:
                                    scelta=6+1
                                    break

                if scelta==-1:
                    if (pulsanti[0].giocatore+pulsanti[4].giocatore+pulsanti[8].giocatore)==obbiettivo:
                        if pulsanti[0].giocatore==1:
                            who=1
                        elif pulsanti[4].giocatore==1:
                            who=1
                        elif pulsanti[8].giocatore==1:
                            who=1

                        if (who==1) or (cambio==1):
                            if pulsanti[0].giocatore==0:
                                scelta=0
                            elif pulsanti[4].giocatore==0:
                                scelta=4
                            elif pulsanti[8].giocatore==0:
                                scelta=8
                                
                    elif (pulsanti[2].giocatore+pulsanti[4].giocatore+pulsanti[6].giocatore)==obbiettivo:
                        if pulsanti[2].giocatore==1:
                            who=1
                        elif pulsanti[4].giocatore==1:
                            who=1
                        elif pulsanti[6].giocatore==1:
                            who=1

                        if (who==1) or (cambio==1):
                            if pulsanti[2].giocatore==0:
                                scelta=2
                            elif pulsanti[4].giocatore==0:
                                scelta=4
                            elif pulsanti[6].giocatore==0:
                                scelta=6
                    cambio=cambio+1


            if (scelta==-1) or (pulsanti[scelta].giocatore!=0):
                while True:
                    ran=random.randint(0,9)
                    try:
                        if pulsanti[ran].giocatore==0:
                            scelta=ran
                            break
                    except:
                        scelta=-1
            #print(scelta)
                
            #app.disableButton(str(scelta))
            #check(str(scelta))
            app.after(500, delay, scelta)
        
#Funzione utile a porre un delay nella mossa del Computer (Per renderlo più reale)
def delay(s):
    check(str(s))

#Funzione smistamento pulsanti secondari
def press(p):
    global turno
    global nome1
    global nome2
    global pulsanti
    global mode
    global punto
    if p=="Resoconto Partita":
        punto.resoconto()
    if p=="Salva Dati Partita":
        punto.salva()
    if p=="Torna alla Home":
        home()
    if p=="GIOCA" or p=="Prossimo Round":
        try:
            if app.getSpinBox("Round")=='':
                salvaround='1'
            else:
                salvaround=app.getSpinBox("Round")
            mode=app.getOptionBox("Modalità")
            if app.getEntry("Nome Giocatore 1")=="":
                nome1="Giocatore 1"
            else:
                nome1=app.getEntry("Nome Giocatore 1")
            if mode=="1vs1":
                if app.getEntry("Nome Giocatore 2")=="":
                    nome2="Giocatore 2"
                else:
                    nome2=app.getEntry("Nome Giocatore 2")
            else:
                nome2="Computer"
        except:
            pass

        turno=0
        app.removeAllWidgets()
        app.addLabel("s","Tris",0,0,colspan=4)
        app.setLabelBg("s","orange")
        app.addLabel("turno","Turno di "+nome1,1,0,colspan=4)
        app.setLabelBg("turno","lightgreen")

        i=0
        cont=0
        j=0
        pulsanti=[]
        for i in range(2,5):
            for j in range(3):
                app.addNamedButton("        ",str(cont),check,i,j)
                pulsanti.append(Tris(0))
                cont=cont+1

        try:
            test=punto.vit1
        except:
            punto=Punteggio(0,0,int(salvaround),0)
        app.addLabel("cont","Round "+(str(punto.roundfatti+1))+"/"+str(punto.rounddafare),7,1)


#Funzione per inizializzare i nomi dei giocatori all'inizio
def gio():
    try:
        try:
            app.removeLabel("Nome Giocatore 2")
            app.removeLabelEntry("Nome Giocatore 2")
        except:
            pass
        if (app.getOptionBox("Modalità")=="1vs1"):
            app.addLabelEntry("Nome Giocatore 2",6,3)
    except:
        pass

#Funzione che mostra la schermata principale
def home():
    global punto
    punto=0
    app.removeAllWidgets()
    app.addLabel("s","Tris",0,3,colspan=4)
    app.setLabelBg("s","orange")
    app.addLabel("w","Benvenuto al Gioco TRIS!",1,3)
    app.addLabel("w1","Inserisci i dati richiesti e clicca su GIOCA per iniziare",2,3)
    app.addLabelOptionBox("Modalità",["Contro il Computer","1vs1"],3,3)
    app.addLabelSpinBoxRange("Round",1,10,4,3)
    app.addLabelEntry("Nome Giocatore 1",5,3)
    app.addButton("GIOCA",press,7,3)

    app.setOptionBoxChangeFunction("Modalità",gio)

app.addMenuList("Home", ["Torna alla Home"], menu)
app.addMenuList("Classifica", ["Partite Salvate","-","Svuota Salvataggi"], menu)
app.addMenuList("Help",["Come si Gioca"], menu)
app.addMenuList("Crediti", ["Crediti","-","Contatti"], menu)
app.addMenuList("Esci", ["Esci"], menu)


home()
app.go()
