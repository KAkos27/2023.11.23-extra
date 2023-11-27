import random
import math

def szamok():
    lotto=[]

    szam:int =math.floor(random.random()*90+1)
    lotto.append(szam)

    while len(lotto) < 5:
        ismetles = False
        szam:int =math.floor(random.random()*90+1)
        for i in range(0,len(lotto),1):
            if szam == lotto[i]:
                ismetles = True
        if ismetles == False:
            lotto.append(szam)
        
    print(lotto)
    return lotto

def atlag(lista):
    osszeg:float=0
    szamlalo:float=0
    atlaga:float=0
    for i in range(0,len(lista),1):
        osszeg+=lista[i]
        szamlalo+=1
    atlaga=osszeg/szamlalo

    return atlaga

def nagyobb(lista):
    osszeg:int = 0
    for i in range(0,len(lista),1):
        if lista[i] > 50:
            osszeg+=1

    return osszeg

def legnagyobb(lista):
    max:int = 0
    for i in range(0,len(lista),1):
        if lista[i] > max:
            max=lista[i-1]

    return max

def hanyadik(lista):
    max:int = 0
    szamlalo:int = 0
    for i in range(0,len(lista),1):
        if lista[i] > max:
            max=lista[i]
            szamlalo=i+1
    return szamlalo

def legkisebb(lista):
    min:int = 91
    for i in range(0,len(lista),1):
        if lista[i] < min:
            min=lista[i]

    return min
    
def szerepel(lista):
    szam:int = int(input("Kérek egy számot!: "))
    szer:str = "Szerepel"
    nemszer:str = "Nem szerepel"
    for i in range(0,len(lista),1):
        if szam == lista[i]:
            return szer
    return nemszer
        
def talalat(lista):
    szelveny = []
    tal:str = "Van találat!"
    nemtal:str = "Nincs találat!"
    
    szam:int=int(input("Kérek egy számot!: "))
    szelveny.append(szam)

    while len(szelveny) < len(lista):
        ismetles = False
        szam:int=int(input("Kérek egy számot!: "))
        for i in range(0,len(szelveny),1):
            if szam == szelveny[i]:
                ismetles = True
        if ismetles == False:
            szelveny.append(szam)
        else:
            print("Hiba! Két különböző számot kell megadni!")

    print(lista)
    print(szelveny)

    for a in range(0,len(lista),1):
        for i in range(0,len(lista),1):
            if szelveny[i] == lista[a]:
                return tal
        i=0
    return nemtal

def hanytalalt(lista):
    szelveny = []
    talszam:int = 0
    
    szam:int=int(input("Kérek egy számot!: "))
    szelveny.append(szam)
    
    while len(szelveny) < len(lista):
        ismetles = False
        szam:int=int(input("Kérek egy számot!: "))
        for i in range(0,len(szelveny),1):
            if szam == szelveny[i]:
                ismetles = True
        if ismetles == False:
            szelveny.append(szam)
        else:
            print("Hiba! Két különböző számot kell megadni!")
    
    print(lista)
    print(szelveny)

    for a in range(0,len(lista),1):
        for i in range(0,len(lista),1):
            if szelveny[i] == lista[a]:
                talszam+=1
        i=0
    return talszam