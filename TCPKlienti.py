import socket 
import sys
import io
klientName='localhost'
klientPort=14000

klientSoketi=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
klientSoketi.connect((klientName,klientPort))
print("\nFIEK-TCP Klienti")
print("---------------------------------------------------------------------------------------------------------------------------")
print('\n\n  METODA                                 AKSIONI'
'\nMetoda IP              ->  Përcakton dhe kthen IP adresën e klientit.'
'\nMetoda NRPORTIT        ->  Përcakton dhe kthen portin e klientit.'
'\nMetoda NUMERO          ->  Gjen numrin e zanoreve dhe bashkëtingëlloreve ne tekst dhe kthen përgjigjen.'
'\nMetoda ANASJELLTAS     ->  Kthen fjalinë e shtypur ne tekst.'
'\nMetoda PALINDROM       ->  Kërkon nje fjali dhe tregon a eshte fjalia palindrome a jo.'
'\nMetoda KOHA            ->  Përcakton kohen aktuale ne server dhe e dërgon atë tek klienti si format te lexueshme për njerëzit.'
'\nMetoda LOJA            ->  Kthen 5 numra nga rangu [1,35].'
'\nMetoda GCF             ->  Gjënë faktorin më te madh te përbashkët në mes dy numra .'
'\nMetoda KONVERTO        ->  Kthen si rezultat konvertimin e opcioneve varësisht opcionit të zgjedhur. '
'                                           Lista e parametrave opcioni janë: cmNeInch, inchNeCm, kmNeMiles, mileNeKm')

print(
'\nMetoda MUAJI             ->  Kthen muajin perkates te atij numri')
print("---------------------------------------------------------------------------------------------------------------------------")


kerkesa=input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, MUAJI)?")
while True:

    klientSoketi.send(kerkesa.encode())
    informata=klientSoketi.recv(128).decode()
    print(informata)
    kerkesa=input("Operacioni (IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GCF, KONVERTO, MUAJI)?")
klientSoketi.close()
