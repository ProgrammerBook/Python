# Vytvoření seznamu
# pozice   0  1  2  3  4
my_list = [1, 2, 3, 4, 5]

# Výpis celého seznamu
print("Obsah seznamu:", my_list)

# Vypisování zvlášť hodnot z seznamu
print("První prvek seznamu:", my_list[0])  # Očekávaný výstup: 1
print("Poslední prvek seznamu:", my_list[-1])  # Očekávaný výstup: 5

# Přidání prvku do seznamu
my_list.append(6)
print("Seznam po přidání prvku:", my_list)

# Odebrání prvku ze seznamu podle hodnoty
my_list.remove(3)
print("Seznam po odebrání prvku:", my_list)

# Indexování seznamu
print("První prvek seznamu:", my_list[0])  # Očekávaný výstup: [1, 2, 4]
print("Posledního prvku seznamu:", my_list[4])  # Očekávaný výstup: [4, 6]
