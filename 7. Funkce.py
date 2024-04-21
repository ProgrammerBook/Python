# Funkce jsou bloky kódu, které provádějí určité operace a mohou být znovupoužity.

# Vytvoření funkce
def add(x, y):
    
    # Tato funkce sečte dvě čísla.
    
    # Args:
      #  x (int): První číslo.
      #  y (int): Druhé číslo.
        
    # Returns:
        #int: Součet dvou čísel.
    
    z = x + y
    return z   

    # díky funkci return se vyhodnotí funkce add
# Vyvolání funkce
number1 = 3
number2 = 4
result = add(3, 4)
# add() --> takhle vyvoláváme funkci a do závorke napíšeme hodnoty ketré cheme aby měli hodnotu ve funkci 

# Výpis výsledku
print("Výsledek sčítání je:", result)  # Očekávaný výstup: 7



