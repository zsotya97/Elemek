import string 
#Osztály az adatok beolvasásához
class Adatok(object):
    def __init__(self, sor):
        split = sor.split(';')
        self.Ev=int(split[0])  if split[0]!="Ókor" else 0
        self.Nev=split[1]
        self.Vegyjel=split[2]
        self.Rendszam= int(split[3])
        self.Felfedezo=split[4]


#Beolvasás
with open("felfedezesek.csv","r") as Beolvas:
    fejlec= Beolvas.readline()
    lista = [Adatok(x.strip()) for x in Beolvas]


#3. feladat: 
print(f"3. feladat: Elemek száma: {len(lista)}")



#4. feladat: 
print(f"4. feladat: Felfedezések száma az ókorban: {sum(1 for x in lista if x.Ev==0)}")



#5. feladat: 
vegyjel = input("5. feladat: Kérek egy vegyjelet: ")
szam=0
while len(vegyjel)>2 or len(vegyjel)==0 or szam==0:
    for x in list(string.ascii_lowercase):
        for y in vegyjel:
            if x.lower()==y.lower():
               szam+=1
    if szam==0 or len(vegyjel)!=szam:
        vegyjel = input("5. feladat: Kérek egy vegyjelet: ")
        szam=0

#6. feladat
volt = False
kereses = Adatok
for x in lista:
    if x.Vegyjel.lower() == vegyjel.lower():
        volt =True
        kereses = x
        break
print("6. feladat: Keresés")
szoveg = f"""\tAz elem vegyjele: {kereses.Vegyjel}
\tAz elem neve: {kereses.Nev}
\tRendszám: {kereses.Rendszam}
\tFelfedezés éve: {kereses.Ev}
\tFelfedező: {kereses.Felfedezo}""" if volt is True else "\tNincs ilyen elem"
print(szoveg)


#7.feladat: 
leghosszabb = -1
for x in range(len(lista)-1):
    if lista[x].Ev!=0:
        if lista[x+1].Ev-lista[x].Ev>leghosszabb:leghosszabb = lista[x+1].Ev-lista[x].Ev
print(f"7. feladat: {leghosszabb} év volt a leghosszabb időszak két elem felfedezése között")


#8. feladat: 
print("8. feladat: Statisztika")
statisztika = {x.Ev for x in lista if x.Ev != 0}
for x in statisztika:
    szamlalas=0
    for y in lista:
        if(y.Ev==x):szamlalas+=1
    if szamlalas>3:
        print(f"\t{x}: {szamlalas}")
