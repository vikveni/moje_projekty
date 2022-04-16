from pprint import pprint
TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of a Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present. '''
]
oddelovac = "-" * 35
# Zadané proměné uživatel a heslo
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
# Vstupy
user_inp = input("User: ")
pass_inp = input("Password: ")

# Ověření uživatele
if users.get(user_inp) == pass_inp:
    print("Welcome to the app,", user_inp, ".")
    print("We have 3 texts to be analyzed.")
    print(oddelovac)
else:
    print("Wrong user or password")
    quit()

# výběr textu
choose_txt = input("Choose from 1-3 for analyzing the text: ")
if 1 <= choose_txt.isnumeric() <= 3:
    print(oddelovac)
else:
    print("Wrong number!")
    quit()

txt = TEXTS[int(choose_txt) - 1].split()

# Všechna slova
pocet_slov = []
pocet_slov_s_velkym = []
pocet_velkych_slov = []
pocet_malych_slov = []
cisla = []
soucet_cisel = 0
for slova in txt:
    ciste_slova = slova.strip(".,:!\"\'")
    pocet_slov.append(ciste_slova)
    # S počátečním velkým
    if slova.istitle():
        pocet_slov_s_velkym.append(slova)
    # Slova velkými písmeny
    if slova.isupper():
        pocet_velkych_slov.append(slova)
    # Slova s malym
    if slova.islower():
        pocet_malych_slov.append(slova)
    #  Cisla
    if slova.isnumeric():
        cisla.append(slova)
    # Sooucet cisel
    if slova.isnumeric():
        soucet_cisel += int(slova)
print(f"There are {len(pocet_slov)} words in the selected text.")
print(f"There are {len(pocet_slov_s_velkym)} titlacse words.")
print(f"There are {len(pocet_velkych_slov)} uppercase words.")
print(f"There are {len(pocet_malych_slov)} lowercase words.")
print(f"There are {len(cisla)} numeric strings")
print(f"The sum of all numbers {soucet_cisel}")

#
pocet_pismen = []
print(oddelovac)
print("LEN|", "OCCURENCES".center(20), "|NR.")
for vsechna_slova in txt:
    pocet_pismen.append(len(vsechna_slova))
#
kolikrat_slovo = {}
for pismena in pocet_pismen:
    if pismena not in kolikrat_slovo:
        kolikrat_slovo[pismena] = 1
    else:
        kolikrat_slovo[pismena] = kolikrat_slovo[pismena] + 1
# Seřazené klíče podle hodnot do proměné
nej_nej = []
for serazeno in sorted(kolikrat_slovo.keys()):
    nej_nej.append(kolikrat_slovo[serazeno])

hvezdicka = "*"

# Konečný výpis
for index, kolikrat in enumerate(nej_nej, 1):
    print(
          f"{index:<3}|{kolikrat * hvezdicka:^22}|{kolikrat}",
          sep="\n")
print("Thank you, for your time :-)")