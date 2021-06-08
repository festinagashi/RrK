import socket 
from _thread import *
import math 
import random  
import sys 
import datetime

serverName = 'localhost' 
severPort = 14000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    serverSocket.bind((serverName,severPort))
    
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()

serverSocket.listen(5)

print("----------------------------------------------------------------------------------")
print("\tFIEK-TCP Serveri")
print("----------------------------------------------------------------------------------")


def NUMERO(Teksti):
    
    zanoret =['A','E', 'I', 'O', 'U', 'Y', 'a', 'e','i', 'o','u','y']
    bashtingellore = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 
               'V', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'x', 'z']
    count = 0
    count2= 0

    for i in zanoret:
        for j in Teksti:
            if i==j:
                count2 = count2 + 1

    for i in bashtingellore:
        for j in Teksti:
            if i==j:
                count = count+1

    f = "Teksti i pranuar përmban "+ str(count2) +" zanore dhe "+ str(count) +" bashkëtingëllore"
    return f

def ANASJELLTAS(Teksti):
    fjaliaMbrapshte = (Teksti[::-1])
    return fjaliaMbrapshte

def PALINDROM(Teksti):
   
    return Teksti == Teksti[::-1]


def KOHA():
    from time import gmtime, strftime
    ktheKohen = strftime("%d.%m.%Y %I:%M:%S %p")
    return ktheKohen


def LOJA():
    Numrat = ""
    for i in range(0,5):
        NrRandom = random.randint(1,35)
        Numrat += str(NrRandom) + " "
    return Numrat


def KONVERTO(opcioni, Numri):
    if opcioni == "cmNeInch":
        Rezultati = Numri*0.393701
    elif opcioni == "inchNeCm":
        Rezultati = Numri*2.54
    elif opcioni == "kmNeMiles":
        Rezultati = Numri*0.62137
    elif opcioni == "mileNeKm":
        Rezultati = Numri/(0.62137)
    else:
        Rezultati= "Gabim! Opcionet janë: cmNeInch, inchNeCm, kmNeMiles, mileNeKm!"
    return Rezultati


def GCF(numri1,numri2):

    try:                        
        nr1 = int(numri1)
        nr2 = int(numri2)
        faktori =  math.gcd(nr1, nr2) 
        return faktori
    except:
        nr1 = str(numri1)
        nr2 = str(numri2)
        gabimi = 'Ju lutem shtypni vlera integer!'
        return gabimi


#----------------------METODAT SHTESE------------------

def MUAJI(numri):
    if(numri == 1):
        r = "Janari"
    elif(numri == 2):
        r= "Shkurt"
    elif(numri == 3):
        r= "Marsi"
    elif(numri == 4):
        r= "Prill"
    elif(numri == 5):
        r = "Maj"
    elif(numri == 6):
        r = "Qershor"
    elif(numri==7):
        r = "Korrik"
    elif(numri==8):
        r = "Gusht"
    elif(numri==9):
        r  = "Shtator"
    elif(numri==10):
        r = "Tetor"
    elif(numri==11):
        r = "Nentor"
    elif(numri==12):
        r = "Dhjetor"
    else: 
        r = "Nuk ka muaj te tille"
    return r


def ShumeKlient(lidhja):
    while True:
        try:
            informata = lidhja.recv(128).decode()
        except socket.error:
            print("Ndonje problem ka ndodhur!")
            break
        arr = str(informata).rsplit(" ")
        rendi = ""
        gjVargu = len(arr)
        for fjala in range(1, gjVargu):
            rendi += arr[fjala]
            if(fjala != gjVargu):
                rendi += " "
        if not informata:
            break
        elif(arr[0]=="IP"):
            informata = "IP Adresa e klientit është : " + str(address[0])
        elif(arr[0]=="NRPORTIT"):
            informata = "Klienti është duke përdorur portin " + str(address[1])
        elif(arr[0]=="NUMERO"):
            informata = NUMERO(rendi)

        elif(arr[0]=="ANASJELLTAS"):
           informata = ANASJELLTAS(rendi)
        elif(arr[0]=="KOHA"):
            informata = KOHA()

        elif(arr[0]=="LOJA"):
            informata = "5 numra te rastësishëm nga rangu [1,35] janë: " + LOJA()

        elif(arr[0]=="KONVERTO"):
            try:
                numri = float(arr[2])
            except socket.error:
                return "Gabim!"
            informata = str(KONVERTO(arr[1], numri))
        elif(arr[0]=="PALINDROM"):
           if (PALINDROM(arr[1]) == True):
            informata = "Teksti i dhënë është palindrome"
           else:  
            informata = "Teksti i dhënë nuk është palindrom"
        elif(arr[0] == 'GCF'):
            nr1 = arr[1] 
            nr2 = arr[2] 
            informata = 'Faktori me i madhe i perbashket eshte: ' + str(GCF(nr1,nr2))

        elif(arr[0]=="MUAJI"):
            rendi = int(arr[1])
            informata = str(MUAJI(rendi))
 
        else:
          informata="Serveri nuk ka përgjigjje për këtë kërkesë, ajo ose nuk është një nga opcionet ose nuk e keni shënuar mirë."
        lidhja.send(informata.encode())
    lidhja.close()   
  

i = 1
while(i==1):
        lidhja, address = serverSocket.accept()
        print("Serveri është lidhur me klientin me IP Adresë %s, në portin %s" % address)
        start_new_thread(ShumeKlient,(lidhja,))
serverSocket.close()



