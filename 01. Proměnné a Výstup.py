# Výpis do příkazového řádku
# díky funkci print() mužeme vypisovta hodnoty v kulatých závorkách do příkazového řádku)

# ---------------------------------------------------------
# print(Hotnota kterou checeme vypsat do příkazového řádku)
# ---------------------------------------------------------

print("Hello world!") # Výstup Hello world!

# Vytvoření proměnných s různými datovými typy

# -----------------------------------
# název_proměnné = hodnota v promenné
# -----------------------------------

print(" ")

# Příklady proměnných
vek = 25         # typ int
jmeno = "Václav"   # typ str
je_muz = True    # typ bool
vyska = 175.5    # typ float

# Datové Typy
# -----------
#   Integers (celá čísla): Reprezentují celé číselné hodnoty, například věk.
#   Strings (řetězce): Reprezentují textové hodnoty, například jméno.
#   Booleans (logické hodnoty): Reprezentují logické hodnoty True (pravda) nebo False (nepravda).
#   Floats (desetinná čísla): Reprezentují desetinné číselné hodnoty, například výšku.


# Ukázka výpisu hodnot proměnných
print("Osobní údaje:")
print(" Věk:", vek)
print(" Jméno:", jmeno)
print(" Je muž:", je_muz)

# F-string
print(f" Výška: {vyska}")
#     ↑        ↑     ↑ 
#     |       Do složených závorek napíšeme proměnnou která poté bude pouze v printu přetipovaná na string
#     |
# píšeme f před uvozovky