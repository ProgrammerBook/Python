#Přetipování umožňuje konverzi tohoto řetězce na požadovaný datový typ.
#Pomocí přetipování můžete konvertovat vstup do různých datových typů, například na celé číslo (Integer).

x = "1"
y =  2
x = int(x) # x  se zmení z datového typu string na intiger
z = x + y
print("Sčítání:", z)  # Výstup: 3

# str() - přetipování na string
# int() - přetipování na intiger
# bool() - přetipování na bolleans
# float() - přetipování na float

# Získání vstupu od uživatele jako desetinné číslo
float_input = float(input("Zadej desetinné číslo: "))
print("Zadali jste číslo:", float_input)
