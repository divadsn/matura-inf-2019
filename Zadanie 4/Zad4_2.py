#!/usr/bin/env python3
from math import factorial as silnia

plik = open("liczby.txt", "r")

for l in plik:
    liczba = l.rstrip()
    suma = 0

    for cyfra in liczba:
        suma += silnia(int(cyfra))

    if suma == int(liczba):
        print(liczba)
