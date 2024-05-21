# Třídy využíváme k tomu, abycho vytovřili takovou svojí knihovnu
# V třídě vytváříme pouze funkce
#---------------------------------------------
#class nazve_tridy:
    # zde vytvoříme funkce které chceme

# Vyvolání třídy
# nazev_tridy.nazev_funkce(parametry funkce)
#---------------------------------------------
# Ukážem si příklad , ve kterém vytvoříme karkulačku pro sčítání a odčítání

# Vytvořeni třídy
class karkulacka:
    # Vytovření funkce pro sčítání
    def scitani(cislo1,cislo2):
        vysledek = cislo1 + cislo2
        return vysledek
    
    # Vytvoření funkce pro odečítaní
    def odecitani(cislo1,cislo2):
        vysledek = cislo1 - cislo2
        return vysledek
    
x = int(input("Zadejte první číslo: "))
y = int(input("Zadejte druhé číslo: "))

# Vyvolání funkce pro sčítání
vysledek1 = karkulacka.scitani(x,y)

# Vyvolání funkce pro odečítání
vysledek2 = karkulacka.odecitani(x,y)

print("Sečtení čísel: ", vysledek1)
print("odečtení čísel: ", vysledek2)
    
    