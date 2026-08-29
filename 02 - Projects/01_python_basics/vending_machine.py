print("Il prezzo dell'acqua è di 1$")
print("Il prezzo della coca cola è di 2$")
print("Il prezzo del panino è di 4$")
scelta = int(input("Seleziona il seguente numero per scegliere cosa acquistare: 1-acqua, 2-coca cola, 3 panino"))
soldi = int(input("Quanti soldi hai da spendere?"))
if soldi == 0: 
    print("Non hai abbastanza soldi.")
else:
    if scelta == 1 and soldi >=1:
        print("Hai abbastanza soldi poer acquistare l'acqua, attendi e ritira!")
    elif scelta ==2 and soldi >=2:
        print("Hai abbastanza soldi per acquistare la coca cola, attendi e ritira!")
    elif scelta ==3 and soldi >=4:
        print("Hai abbastanza soldi per acquistare il panino, attendi e ritira!")
    else:
        print("Non hai abbastanza soldi per acquistare questo prodotto.")
