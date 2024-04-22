# Vytvoření seznamu
# pozice   0  1  2  3  4
cisla = [1, 2, 5, 3, 4]

# Výpis celého seznamu
print("Obsah seznamu:", cisla) # Výstup: [1, 2, 5, 3, 4]

# Vypisování zvlášť hodnot z seznamu
print("První prvek seznamu:", cisla[0])  # Výstup: 1
print("Poslední prvek seznamu:", cisla[4])  # Výstup: 5

# Přidání prvku do seznamu
cisla.append(6)
print("Seznam po přidání prvku:", cisla) # Výstup: [1, 2, 5, 3, 4, 6]

# Odebrání prvku ze seznamu podle hodnoty
zvirata = ["Pes", "Kočka","Panda"]
zvirata.remove("Pes")
print("Seznam po odebrání prvku:", zvirata) # Výstup: ["Kočka","Panda"]

# Vytvoření funkce pro nalezení maximální hodnoty v seznamu
print("Maximální hodnota seznamu:", max(cisla)) # Výstup: 6

# Vytvoření funkce pro nalezení minimální hodnoty v seznamu
print("Minimální hodnota seznamu:", min(cisla)) # Výstup: 1

# Vytvoření funkce pro řazení seznamu
cisla.sort(cisla)
print("Seznam seřazený:", cisla) # Výstup: [1, 2, 3, 4, 5, 6]

# Vytvoření funkce pro zjištění délky seznamu
print("Délka seznamu:", len(cisla)) # Výstup: 6