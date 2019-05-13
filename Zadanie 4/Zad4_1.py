#!/usr/bin/env python3

def jest_potega(n, podstawa):
    liczba = 1
    k = 0

    while n > liczba:
        liczba = podstawa ** k
        k += 1

    if liczba == n:
        return True
    else:
        return False

plik = open("liczby.txt", "r")
ilosc_liczb = 0

for l in plik:
    liczba = int(l.rstrip())
    if jest_potega(liczba, 3):
        ilosc_liczb += 1

print(ilosc_liczb)
