import random
import math

def szamok():
    lotto=[]
    for i in range(1,6,1):
        szam:int =math.floor(random.random()*90+1)
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
    
    for i in range(0,5,1):
        szam:int = int(input("Kérek egy számot!: "))
        szelveny.append(szam)
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
    
    for i in range(0,5,1):
        szam:int = int(input("Kérek egy számot!: "))
        szelveny.append(szam)
    print(lista)
    print(szelveny)

    for a in range(0,len(lista),1):
        for i in range(0,len(lista),1):
            if szelveny[i] == lista[a]:
                talszam+=1
        i=0
    return talszam