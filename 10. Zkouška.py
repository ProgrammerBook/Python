# V pythonu mužeme provádět zkoušky , díky kterým s emužeme vyhnout zastavení kodu kvůli erroru
# Zkoušku porvadíme pomocí 'try' a 'except'

#----------------------------------------------------------------------------------------------
#try:
#    zde dáme blok kodu pro zkoušku
#except Zde dáme typ erroru:
    # Jestliže se vyskytne v bloku kodu v try error, tak blok kodu přeskoči a sputstí se tento
#----------------------------------------------------------------------------------------------

x = "1"
y = 2


# Kod s chybou
try:
    z = x + y  #TypeError: chyba datového typu, nemužem sčíttat intiger a string
    print("Zde není žádná chyba, výsledke je", z)
    # Tento blok kodu neprobehne z duvodu erroru
except TypeError:
    print("V kodu nastala chyba")


# Kod bez chybi
try:
    z = int(x) + y  #Výstup: 3
    print("Zde není žádná chyba, výsledke je", z)
    # V kodu nenastala chby kod v pořádku porběne
except TypeError:
    print("V kodu nastala chyba")
    # Tento blok kodu neprobehe, jelikož nenastala chyba
