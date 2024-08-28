# Podmínky


#Podmínky v Pythonu umožňují provádět různé akce na základě splnění určitých kritérií. Klíčová slova if, elif a else se používají k definici podmínek.

# ----------------------------------------------------------------------
# if podmínka1:
    # provedený kód, pokud je podmínka1 splněna
# elif podmínka2:
    # provedený kód, pokud je podmínka2 splněna a podmínka1 není splněna
# else:
    # provedený kód, pokud žádná předchozí podmínka není splněna
# ----------------------------------------------------------------------


# Podmínky
    # == --> rovnost
    # < , > --> menší než, větší než
    # <= , >= --> menší nebo rovná se , větší nebo rovná se
    # podminka1 and podminka2 --> and --> jestliže podminka1 a podminka2 bude True provede se blok kodu, zdali obě nebo jedna bude False blok kodu neproběhne
    # podminka1 or podminka2 --> or --> musí být alespoň jedna podmínka True aby proběhl blok kodu
    # hodnota in seznam --> in --> zkontrluje zdali se hodnota nacházi v senzamu
    # isinstance (proměnná, datový typ) --> kontorulje datoví typ 

# Příklady

# Vyhodnocení znaku čísla
cislo = 15
print("Velikost čísla")
print(" Váše číslo =", cislo)

if cislo == 0:
    print(" Číslo je 0")
elif cislo < 0:
    print(" Číslo je větší než 0")
else:
    print(" Číslo je číslo je menší než 0")







# Kontrola datového typu
print("Kontrola datového typu")
x = 10
print(" Hodnota x =", x)

if isinstance(x, int):
    print(" Hodnota x je celé číslo")
elif isinstance(x, float):
    print(" Hodnota x je desetinné číslo")
else:
    print(" Hodnota x není číslo")



# Kontrola vstupu od uživatele
print("Kontrola zadané honodty")
prezdivka = input(" Zadej své jméno: ")

if prezdivka:
    print(" Vítej,", prezdivka)
else:
    print(" Nezadal jsi žádnou prezdivku")

