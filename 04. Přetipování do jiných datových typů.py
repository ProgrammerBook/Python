# Přetipování umožňuje konverzi promenné na jiný požadovaný datový typ.
# Pomocí přetipování můžete konvertovat vstup do různých datových typů, například na celé číslo (Integer).

# ---------------------------------------------------
# str/int/float/bool(zde dáme proměnná kterou cheme přetipovat)
# ---------------------------------------------------

x = "1"
y =  2
x = int(x) # x  se změní z datového typu string na integer
z = x + y
print("Sčítání:", z)  # Výstup: 3

# str() - přetipování na string
# int() - přetipování na intiger
# bool() - přetipování na bolleans
# float() - přetipování na float

# Získání vstupu od uživatele jako desetinné číslo
vstup = float(input("Zadej desetinné číslo: "))
print("Zadali jste číslo:", vstup)
