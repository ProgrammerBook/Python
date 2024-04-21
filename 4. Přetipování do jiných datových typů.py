#Přetipování umožňuje konverzi tohoto řetězce na požadovaný datový typ.
#Pomocí přetipování můžete konvertovat vstup do různých datových typů, například na desetinné číslo (float).
x = "1"
y =  2
x = int(x) # x  se zmení z datového typu string na intiger
z = x + y
print("Sčítání:", z)  # Očekávaný výstup: 3

# Získání vstupu od uživatele jako desetinné číslo
float_input = float(input("Zadej desetinné číslo: "))
print("Zadali jste číslo:", float_input)
