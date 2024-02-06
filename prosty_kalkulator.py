#!/bin/env python3


# Autor: Małgorzata Staniszewska
# Wersja: 0.1
# Kontakt: mstaniszewska1@student.wsb-nlu.edu.pl

import sys

def kalkulator(liczba_1, operacja, liczba_2):
    if operacja == '+':
        wynik = liczba_1 + liczba_2
    elif operacja == '-':
        wynik = liczba_1 - liczba_2
    else:
        print("Nieobsługiwana operacja. Dozwolone operacje to: +, -")
        sys.exit(1)

    with open('/tmp/wynik.txt', 'w') as plik_wynikowy:
        plik_wynikowy.write(str(wynik))

if len(sys.argv) != 4:
    print("Użycie: calc.py <liczba_1> <operacja +-> <liczba_2>")
    sys.exit(1)

try:
    liczba_1 = float(sys.argv[1])
    operacja = sys.argv[2]
    liczba_2 = float(sys.argv[3])
except ValueError:
    print("Podane argumenty nie są liczbami.")
    sys.exit(1)

kalkulator(liczba_1, operacja, liczba_2)
print(f"Wynik został zapisany do pliku /tmp/wynik.txt.")

