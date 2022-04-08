
print("Ahoj Tomáši (to oslovení je schválně!), teda pokud nejsi Tom můžšes soubor ukončit!")

jmeno = input("Zadej jméno: ")
prijmeni = input("Zadej přijmení: ")

if jmeno == "Tomáš" and prijmeni == "Vlášek":
    print("Vítám tě Tome, rád bych ti představil můj nápad :-) ")
else:
    print("Ty nejsi ten koho hledám!!!!!!!!!!! Pakuj se odsud pryč a nebo jen neumíš správně napsat jak se "
          "jmenuješ?")
    quit()

jkj = input("Jak se máš?: ")
dobry = ["Dobře", "Jde to", "Normálka", "Normoš", "Dobrý"]
if jkj in dobry:
    print("To rád slyším")
else:
    print("Tak třeba to bude lepší :-(")
nazev_projektu = "Nesmrtelný kluci"
guess_count = 0
guess_limit = 2
out_of_guesses = False
guess = input("Jak si myslíš, že se projekt bude jmenovat? Btw. máš 3 pokusů xD: ")

while guess != nazev_projektu and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Jak si myslíš, že se projekt bude jmenovat?: ")
        guess_count += 1
        guess_limit
    else:
        out_of_guesses = True

if out_of_guesses:
    print(nazev_projektu, "co si o to myslíš? Jo ty ještě nevíš, co to bude vlastně...")
else:
    print("Správně!")
projekt = ["Youtubeři", "Influenceři", "Podcasteři"]
print(str(projekt).center(50))
cislo_sluzby = int(input("Zadej číslo, podle kterého si mysliš, že to je: "))
guess_count_2 = 0
guess_limit_2 = 2
out_of_guesses_2 = False
projekt = ["Youtubeři", "Influenceři", "Podcasteři"]
projekt_spravne = projekt[-1]
while cislo_sluzby != projekt_spravne and not out_of_guesses:
    if guess_count_2 < guess_limit_2:
            cislo_sluzby = int(input("Hádej dál...:"))
            guess_count_2 += 1
    else:
            out_of_guesses_2 = True

if out_of_guesses_2:
    print("Správně je to podcast!", "Napadlo mě to, s tím, že máme o čem kecat, o životě prakticky ovšem "
                                    "a mohli bychom tu něco zanechat a zárověň něco i předat co na to říkáš")
else:
    print("Přesně tak je to podcast!" "Napadlo mě to, s tím, že máme o čem kecat, o životě prakticky ovšem "
                                    "a mohli bychom tu něco zanechat a zárověň něco i předat co na to říkáš")
print("Dík dalo mi to práci jako svině....")


