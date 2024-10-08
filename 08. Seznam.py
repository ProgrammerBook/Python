# Vytvoření seznamu
# Seznam je datová strukutra ve které můžeme všechny datové typy
# Pro vyvoření seznamu musíme za znemnékem rovnosti dát hranaté závroky, a každou hodnotu odělovat čárkou

# -------------------------------------------
# nazev_seznamu = ["zde", "budou", "hodnoty", "v", "senzamu"]
# -------------------------------------------


# Pozice 0  1  2  3  4
cisla = [1, 2, 5, 3, 4]

# Pozice     0       1       2  
zvirata = ["Pes", "Kočka","Panda"]

# Výpis celého seznamu
print("Obsah seznamu s čísli:", cisla) # Výstup: [1, 2, 5, 3, 4]
print("Obasch seznamu se zvířaty:", zvirata)

# Vypisování zvlášť hodnot z seznamu
print("První prvek seznamu s čísli:", cisla[0])  # Výstup: 1
print("Poslední prvek seznamu s čísli:", cisla[4])  # Výstup: 4

# Přidání prvku do seznamu
cisla.append(6)
print("Seznam s čísli po přidání prvku:", cisla) # Výstup: [1, 2, 5, 3, 4, 6]

# Odebrání prvku ze seznamu podle hodnoty

zvirata.remove("Pes")
print("Seznam se zvířatama po odebrání prvku:", zvirata) # Výstup: ["Kočka","Panda"]

# Nalezení maximální hodnoty v seznamu
print("Maximální hodnota seznamu s čísli:", max(cisla)) # Výstup: 6

# Nalezení minimální hodnoty v seznamu
print("Minimální hodnota seznamu s čísli:", min(cisla)) # Výstup: 1

# Seřazení seznamu
cisla.sort(reverse = False)
print("Seznam s čísli seřazený:", cisla) # Výstup: [1, 2, 3, 4, 5, 6]
# reverse --> díky funkci reverse se kod seřadí naopak, jestliže tak chceme napíšme míto False na True

# Zjištění délky seznamu
print("Délka seznamu s čísli:", len(cisla)) # Výstup: 6