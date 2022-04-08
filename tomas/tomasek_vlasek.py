from pprint import pprint
print("Ahoj Tome, teda pokud nejsi Tom můžšes soubor ukončit!")

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
projekt = ["Youtubeři-1", "Influenceři-2", "Podcasteři-3"]
print(str(projekt).center(50))
projekt = ["Youtubeři", "Influenceři", "Podcasteři"]
projekt_spravne = True

while projekt_spravne:
    cislo = input("Co si myslíš, že to je?: ")
    if cislo.isnumeric() and int(cislo) == 3:
        print("Přesně tak je to podcast!" "Napadlo mě to, s tím, že máme o čem kecat, o životě prakticky ovšem ")
        print("a mohli bychom tu něco zanechat a zárověň něco i předat co na to říkáš.")
        print("Podle mě by to bylo super zajímávý, je to téma takový tabu, ale je sposuta lidi co si něčim")
        print("prošla a je nás málo v mladym věku co si něčím takovým prošli")
        break
    else:
        print("Ne to určitě ne, zkus to znova")
