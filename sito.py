from flask import Flask
from random import choice

lista_fatti = [
    "La maggior parte delle persone che soffrono di dipendenza tecnologica sperimentano un forte stress quando si trovano al di fuori dell'area di copertura della rete o non possono utilizzare i loro dispositivi.",
    r"Secondo uno studio condotto nel 2018, più del 50% delle persone di età compresa tra i 18 e i 34 anni si considera dipendente dal proprio smartphone.",
    "Lo studio della dipendenza tecnologica è una delle aree più rilevanti della ricerca scientifica moderna.",
    r"Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro.",
    "Un modo per combattere la dipendenza tecnologica è cercare attività che portino piacere e migliorino l'umore.",
    "Elon Musk sostiene che i social network sono progettati per tenerci all'interno della piattaforma, in modo che trascorriamo il maggior tempo possibile a guardare contenuti.",
    "Elon Musk è anche favorevole alla regolamentazione dei social network e alla protezione dei dati personali degli utenti. Sostiene che i social network raccolgono un'enorme quantità di informazioni su di noi, che possono essere utilizzate per manipolare i nostri pensieri e comportamenti.",
    "I social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme."
]




app = Flask(__name__)

@app.route("/gen-pas")
def gen_pass():
    char = "+-/*!&$#?=@<>abcdefghilmopqrstuvwz1234567890"
    p= []
    p2 = ""
    for i in range(20): p.append(choice(char))
    for i in range(20): p2 += p[i]
    return f"<h3>{p2}<h3>   <br><a href='/'>Ritorna alla home.</a>"

@app.route("/")
def pag_principale():
    return "<h1>Titolo</h1><br> <a href='/fatto_casuale'>Scopri un fatto casuale!</a><br> <a href='/gen-pas'>Genera una password sicura!</a>"

@app.route("/fatto_casuale")
def fc():
    return f'<h3>{choice(lista_fatti)}</h3><br><a href="/">Ritorna alla home.</a>'

app.run(debug=True)
