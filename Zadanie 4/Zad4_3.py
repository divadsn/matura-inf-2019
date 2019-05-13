#!/usr/bin/env python3
from math import gcd as nwd

def nwd_ciagu(ciag):
    if len(ciag) == 2:
        return nwd(ciag[0], ciag[1])
    else:
        return nwd(ciag[0], nwd_ciagu(ciag[1:]))

plik = open("liczby.txt", "r")
liczby = []

for l in plik:
    liczby.append(int(l.rstrip()))

pierwsza_liczba = liczby[0]
dlugosc_ciagu = 0
wspolny_dzielnik = 1

for i in range(1, len(liczby)):
    d = 1 # długość fragmentu ciągu
    t = 1 # NWD z fragmentu ciągu

    for x in range(2, len(liczby) - i): # od drugiego elementu, ponieważ nwd_ciagu wymaga min. dwuelementowy ciag
        nwd_nowe = nwd_ciagu(liczby[i:i + x])
        if nwd_nowe > 1:
            t = nwd_nowe
            d = x
        else:
            break

    # sprawdź, czy nowy ciąg jest dłuższy od poprzedniego
    if d > dlugosc_ciagu:
        pierwsza_liczba = liczby[i]
        dlugosc_ciagu = d
        wspolny_dzielnik = t

print(f"Pierwsza liczba ciągu: {pierwsza_liczba}, długość ciągu: {dlugosc_ciagu}, NWD: {wspolny_dzielnik}")
