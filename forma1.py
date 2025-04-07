
"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""


print("A beolvasott fájlban összesen ____ versenyző szerepel.")
print("A legtöbb futamot nyert versenyző: ____")
print("A legtöbb futamot teljesített versenyző: ____")
print("Az átlagos futamszám: ____")

versenyzok = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
        next(forrasfajl)
        for sor in forrasfajl:
            adatok = sor.strip().split(';')
            nev = adatok[0]
            csapat = adatok[1]
            gyozelmek_szama = int(adatok[2])
            teljesitett_futamok_szama =  int(adatok[3])

            versenyzok.append([nev, csapat, gyozelmek_szama, teljesitett_futamok_szama])

print(f'{versenyzok=}')
#1
versenyzo_szam = len(versenyzok)
print(f'A beolvasott fájlban összesen {versenyzo_szam} versenyző szerepel.')
#2
zsivany = max(versenyzok, key=lambda x: x[2])
#zsivany = zsivany[1]
print(f'A legtöbb futamot nyert versenyző: {zsivany}')
#3
legtobb_futam = max(versenyzok, key=lambda x: x[3])
#legtobb_futam = legtobb_futam[3]
#for versenyzo in versenyzok:
    # if versenyzo[2] == 

print(f'A legtöbb futamot teljesített versenyző: {legtobb_futam}')
#4
atlag = sum([x[3] for x in versenyzok]) / len(versenyzok)
print(f'Az átlagos futamszám: {atlag}')


with open('./kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as celfajl:
    print(f'A beolvasott fájlban összesen {versenyzo_szam} versenyző szerepel.', file=celfajl)
    print(f'A legtöbb futamot nyert versenyző: {zsivany}', file=celfajl)
    print(f'A legtöbb futamot teljesített versenyző: {legtobb_futam}', file=celfajl)
    print(f'Az átlagos futamszám: {atlag}', file=celfajl)
    # celfajl.write(f'A legtöbb futamot nyert versenyző: {zsivany}')
    # celfajl.write(f'A legtöbb futamot teljesített versenyző: {legtobb_futam}')
    # celfajl.write(f'Az átlagos futamszám: {atlag}')
