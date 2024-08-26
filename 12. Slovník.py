# Slovník je datová struktura , ve které se nachází klíče
# Do každého klíče mužeme dávat jakoukoliv hodntou s ruznými datovími typy
# Slovník vyrtváříme pomocí {}, klíče jsou vetšinou vytvořeny v datovém typu string/intiger
# PRo založení dalšího kliče používáme čárku

# -------------------------------------------------
# nazev_slovniku = {
    # nazve_klice: hodnota_klice,
# }
# -------------------------------------------------

# Založení slovníku
klient = {
    "jméno": "Pavel",
    "přijmení": "Novák",
    "věk": 25,
}

# Výpis slovníku
print("Jméno klienta: ", klient["jméno"]) # Výpis: ... Pavel

# Smazání v slovníku 
klient.pop("přijmení") # Smaže se ze slovníku

# Přidání do slovníky
# nazev_slovniku[nazev_klice] = hodnta_klice
klient["přijmení"] = "Novotný"
print("Přijmení klienta: ", klient["přijmení"]) # Výpis: ... Novotný


# Změna hodnty v klíči
klient["věk"] = 26
print("Věk klienta: ", klient["věk"]) # Výpis: ... 26




