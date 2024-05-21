# Funkce jsou bloky kódu, které provádějí určité operace a mohou být znovupoužity.

#-----------------------------------------------------------------
# def add(Zde dáme parametry funkce):
#    Zde zadame kod který cheme mít ve funkci
#    return  To co dáme do return tak bude mít hdonotu ve funkce
# ----------------------------------------------------------------

# Jestli že máme ve funkci více return, a jedna z nich bude zaktivovaná tak se funkce ukončí a dašlí kody budou přeskočeny
# Vyvolání funkce
# add(zde dáme hodnoty pro paramtery) 

# Vytvoření funkce
def add(x, y):
  z = x + y
  return z   

cislo1 = 3
cislo2 = 4

# Vyvolání funkce
result = add(cislo1,cislo2)
# cislo1 a cislo2 ted budoud ve funkci zmeneni na x a y
# Je to pododbné jako překopírovvání porměnné
# x = cilo1 a y = cislo2
# V jakém pořadí porměnné napíšeme, tak takový parametr dostane hodnotu

# Výpis výsledku
print("Výsledek sčítání je:", result)  # Očekávaný výstup: 7



