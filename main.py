import feladatok
lotto=feladatok.szamok()
print()


atlaga:float=feladatok.atlag(lotto)
print(f"Átlag: {atlaga}")

otven:int=feladatok.nagyobb(lotto)
print(f"{otven}db van ötven felett")

legnagy:int=feladatok.legnagyobb(lotto)
print(f"{legnagy} a legnagyobb szám")

hanyas:int=feladatok.hanyadik(lotto)
print(f"A(z) {hanyas}. elem a legnagyobb")

legkis:int=feladatok.legkisebb(lotto)
print(f"{legkis} a legkisebb szám")

kul:int= legnagy-legkis
print(f"{kul} a legkisebb és legnagyobb különbsége")

szer:str=feladatok.szerepel(lotto)
print(szer)