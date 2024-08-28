# Třídy využíváme k tomu, abychom vytvořili vlastní knihovnu funkcí a objektů

# Třída se definuje pomocí klíčového slova `class`:
#---------------------------------------------
# class NazevTridy:
#     # Zde vytvoříme metody (funkce) a atributy (proměnné)
#---------------------------------------------

# Vytvoření instance třídy a volání metod:
# instance = NazevTridy()
# instance.nazevMetody(parametry)

# ---------------------------------------------
# Ukážeme si příklad, ve kterém vytvoříme kalkulačku pro sčítání a odčítání:

# Vytvoření třídy
class Kalkulacka:
    # Vytvoření metody pro sčítání
    def scitani(self, cislo1, cislo2):
        vysledek = cislo1 + cislo2
        return vysledek
    
    # Vytvoření metody pro odečítání
    def odecitani(self, cislo1, cislo2):
        vysledek = cislo1 - cislo2
        return vysledek

# Vytvoření instance třídy
kalkulacka = Kalkulacka()

x = 5
y = 6

# Vyvolání metody pro sčítání
vysledek1 = kalkulacka.scitani(x, y)

# Vyvolání metody pro odečítání
vysledek2 = kalkulacka.odecitani(x, y)
print("Kalkulačka")
print(" Sečtení čísel:", vysledek1)
print(" Odečtení čísel:", vysledek2)

# Dědičnost
# Mezi třídami můžeme dědit, například parametry, či metody

class DomaciMazlicek:
    # Pomocí metody __init__ můžeme inicializovat atributy
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def pohyb(self):
        print(f" {self.jmeno} se pohybuje.")

# Třída, která dědí z DomaciMazlicek
class Pes(DomaciMazlicek):
    def zvuk(self):
        print(f" {self.jmeno} štěká.")

# Použití dědičnosti
print("Domácí zvíře")
pes = Pes("Rex")
pes.pohyb()  # Výstup: Rex se pohybuje.
pes.zvuk()   # Výstup: Rex štěká.
