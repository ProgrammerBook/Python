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

if cislo == 0:
    print("Číslo je 0")
elif cislo < 0:
    print("Číslo je záporné")
else:
    print("Číslo je nula")



# Rozlišení mezi různými typy čísel
x = 10

if isinstance(x, int):
    print("x je celé číslo")
elif isinstance(x, float):
    print("x je desetinné číslo")
else:
    print("x není číslo")



# Kontrola vstupu od uživatele
user_input = input("Zadej své jméno: ")

if user_input:
    print("Vítej,", user_input)
else:
    print("Nezadal jsi žádné jméno")

