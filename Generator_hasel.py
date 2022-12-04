import random

try:
    #Ilość wszystkich znaków
    print('Podaj ogólną ilość znaków:')
    ilosc_znakow = int(input())
    #Ilość wielkich liter
    print('Podaj ilość wielkich liter:')
    wielkie_litery = int(input())
    #Ilość liczb
    print('Podaj ilość liczb:')
    liczby = int(input())
    #Ilość symboli
    print('Podaj ilość symboli/znaki specjalne:')
    symbole = int(input())
except:
    print("Nie podano wartości")

#Sprawdzamy czy podano poprawne kryteria
sum = wielkie_litery + liczby + symbole
if sum >= ilosc_znakow:
    print('Podano za dużą ilość wielkich liter, liczb lub symboli. Suma ich nie powinna przekraczać ogólną ilość znaków.')

#Definiejemy listy liter i symboli
litery = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbole_lista = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+','|','[',']','{','}',';',':','/','?','.','<','>']

#Funkcje losowania
def Los_litere():
    los = litery[random.randint(0,len(litery)-1)]
    return los

def Los_wielkie():
    los = litery[random.randint(0,len(litery)-1)]
    return los.upper()

def Los_liczbe():
    los = random.randint(0,9)
    return los

def Los_symbole():
    los = symbole_lista[random.randint(0,len(symbole_lista)-1)]
    return los

#Tworzenie hasła
def Gen_haslo(il, wi, li, sy):
    haslo = []
    male_litery = il - wi - li - sy
    i = 1

    while i <= il:
        co_losuj = random.randint(0,3)
        if co_losuj == 0 and sy != 0:
            haslo.append(Los_symbole()) 
            sy = sy - 1
        elif co_losuj == 1 and wi != 0:
            haslo.append(Los_wielkie()) 
            wi = wi - 1
        elif co_losuj == 2 and li != 0:
            haslo.append(Los_liczbe())
            li = li - 1
        elif co_losuj == 3 and male_litery != 0:
            haslo.append(Los_litere())
            male_litery = male_litery - 1
        else:
            i = i - 1
        i = i + 1
    return haslo
#-------------------------output--------------------------
print('Twoje hasło to: ',*Gen_haslo(ilosc_znakow, wielkie_litery, liczby, symbole), sep='')
