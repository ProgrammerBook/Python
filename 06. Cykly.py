# While cyklus provádí blok kódu opakovaně, dokud je podmínka pravdivá.

# -------------------------------------------------------------
# while pdomínka 
    # while bude porbíhat do té doby dokud nebude podínka False 
# --------------------------------------------------------------




print("Cyklus while:")

# Vytvoření proměnné řady
rada = 1

# While bude porbíhad do té doby, dokud nebude podmínka False
while rada < 6:
    print(" Na řadě je hráč s číselm:", rada)
    rada += 1


# For cyklus provádí blok kódu Po nějakou dobu
# -----------------------------------------------------------------------
# for i in range()
    # i --> v i se ukládá po kolíkáte (začíná od nuly) už porbíhá kod 
    # range(počet trvání cyklu) --> díky funkci range zadáme kolikrát bude cyklus for porbíhat
# ------------------------------------------------------------------------


print("Cyklus for:")
print(" Čísla od 0 do 5:")

# For proběhne 6 krát
for i in range(6):
    print(" Číslo na řadě:", i)
