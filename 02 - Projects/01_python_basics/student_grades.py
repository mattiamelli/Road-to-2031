n_esami = int(input("Quanti esami vuoi inserire?"))
voti_tot={}
somma_voti=0
voto_max=0
voto_min=100
for i in range (n_esami):
    esame = input("Inserisci il nome dell'esame: ")
    voto = int(input("Inserisci il voto dell'esame: "))
    somma_voti+=voto
    voti_tot[esame] = voto
    if voto > voto_max:
        voto_max = voto
        esame_max = esame
    if voto < voto_min:
        voto_min = voto
        esame_min = esame
media = somma_voti / n_esami
if media >= 6:
    print(f"La tua media è: {media}")
    print("Il tuo rendimento è sufficiente! Congratulazioni")
else:
    print(f"La tua media è: {media}")
    print("Il tuo rendimento è insufficiente!")
for esame, voto in voti_tot.items():
    print(f"Esame: {esame}, Voto: {voto}")
print(f"Il voto massimo è {voto_max} nell'esame di {esame_max}")
print(f"Il voto minimo è {voto_min} nell'esame di {esame_min}")