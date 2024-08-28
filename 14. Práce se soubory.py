# Pomocí pythonu mužeme číst nebo vytvářet soubory

# -----------------------------------------------
   # with open("nazev_souboru","prace_se_souborem") as nazev_promenne

    # Moznosti pracovat se souborem:
        # r = přečtení souboru
        # w = vytvoření soubour

    # Funcke:
        # .read() = funkce na přeštení kodu
        # .write() = Z¨Do závorek dáme to co cheme vypsat do souboru
# ------------------------------------------------
#!!!! NEZAPOMĚN ŽE SOUBOR MUSÍ BÝT VE STEJNÉ SLOŽCE, JINKA MUSÍŠ ZKOPÍROVAT JEHO CESTU V ULOŽISTI NEBO NASTANE CHYBA!!!!


# Vytvoření a otevření souboru v režimu zápisu
with open("novy_soubor.txt", "w") as vy_soubor:
    # Zápis textu do souboru
    vy_soubor.write("Tohle je muj soubor vytvoření v pythonu")


# Otevřeme soubor pro čtení
with open("novy_soubor.txt", "r") as file:
    # Přečteme celý obsah souboru
    obsah = file.read()
    print("Obsah souboru je:")
    print(obsah)
