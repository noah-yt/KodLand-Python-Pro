meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "LMFAO": "sto morendo dal ridere",
            "TBH": "per dire la verità",
            "AFK": "mi allontano dalla tastiera",
            "OMG": "oh mio dio"
            }


while True:
    parola = input("Scrivi una parola che non capisci: ")
    parola = parola.upper()
    if parola in meme_dict.keys():
        print("il significato è:",meme_dict[parola])
    else:
        print("la parola non è presente nel dizionario, Boomer!")
