import math
from math import ceil

strana = float(input('Zadej stranu čtverce v centimetrech: '))
cislo_je_spravne = strana > 0

# nacti hodnotu pi z knihovny math pythonu a zaokrouhli ji na dve desetinna mista
Pi = ceil(math.pi * 1000) / 1000.0

if cislo_je_spravne:
    print(f'Obvod čtverce se stranou {strana} je {4 * strana} cm')
    print(f'Obsah čtverce se stranou {strana} je {strana * strana} cm2')
    print(f'Obsah kruhu s poloměrem rovným obvodu strany tohoto čtverce je {strana * Pi} cm2')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky.')
print("Běž do háje")
