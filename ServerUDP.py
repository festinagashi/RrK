import socket
import sys
from _thread import *
import random
import datetime

serverName = 'localhost' 
severPort = 14000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    serverSocket.bind((serverName,severPort))
    
except socket.error:
    print("Nuk u arrit lidhja me serverin")
    sys.exit()

print("FIEK-UDP Serveri")
print("----------------------------------------------------------------------------------")

def IP():
    return str(adresaKlientit[0])

def NUMRIIPORTIT():
    return str(adresaKlientit[1])


def NUMERO(teksti):
    
    zanoret =['A','E', 'I', 'O', 'U', 'Y', 'a', 'e','i', 'o','u','y']
    bashtingellore = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 
               'V', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q','r', 's', 't', 'v', 'x', 'z']
    count = 0
    count2= 0
    
    for i in zanoret:
        for j in teksti:
            if i==j:
                count2 = count2 + 1
    for i in bashtingellore:
        for j in teksti:
            if i==j:
                count = count+1

    f = "Teksti i pranuar përmban "+ str(count2) +" zanore dhe "+ str(count) +" bashkëtingëllore"
    return f

def ANASJELLTAS(teksti):
    fjaliaMbrapshte = (teksti[::-1])
    return fjaliaMbrapshte

def PALINDROM(teksti):
   
    return teksti == teksti[::-1]


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

def GCF(x, y):
  
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
              
    return int(gcd)

#-------------------- METODAT SHTESE-----------------------------------
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


    
def ShumeKlient(kerkesa, address):
    try: 
       informata = kerkesa.decode() 
    except socket.error:
        print("Ka ndonje problem")   

    arr = str(informata).rsplit(" ")
    rendi = ""
    gjVargu = len(arr)

    for fjala in range(1, gjVargu):
        rendi += arr[fjala]
        if(fjala != gjVargu):
            rendi += " "
    if not informata:
        return
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
            informata = "5 numra te rastësishëm nga 35 janë: " + LOJA()

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
    elif(arr[0]=="GCF"):
        a = int(rendi[1])
        b = int(rendi[2])
        informata = str(GCF(a,b))

    elif(arr[0]=="MUAJI"):
            rendi = int(arr[1])
            informata = str(MUAJI(rendi))


    else:
        informata="Serveri nuk ka përgjigjje për këtë kërkesë, ajo ose nuk është një nga opcionet ose nuk e keni shënuar mirë."
    serverSocket.sendto(informata.encode(),address)


while True:

        informata, address=serverSocket.recvfrom(128)
        print('Serveri është lidhur me klientin me Ip Adresë ' + address[0] + ', në portin : ' + str(address[1]))
        start_new_thread(ShumeKlient,(informata, address,))

serverSocket.close()