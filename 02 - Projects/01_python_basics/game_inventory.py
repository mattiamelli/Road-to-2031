inventario = []
monete = 100
while True:
    schermata_iniziale = int(input(
    "1. Visualizza inventario:\n"
    "2. Compra oggetto:\n"
    "3. Vendi oggetto:\n"
    "4. Visualizza monete:\n"
    "5.Esci\n "
    "Segli un'opzione\n"
    ))
    if schermata_iniziale == 1:
        if not inventario:
            print("L'inventario è vuoto\n")
        else:
            print(f"{inventario}")
    elif schermata_iniziale == 2:
        acquisto = input(
        "Spada > 50 monete\n"
        "Scudo > 30 monete\n"
        "Pozione > 10 monete\n"
        "Scegli cosa comprare\n"
        )
        acquisto = acquisto.lower()
        inventario.append(acquisto)
        if acquisto == 'spada':
            if monete >= 50:
                monete -= 50
            else:
                print("L'acquisto non può essere effettuato, saldo insufficiente!")
        elif acquisto == 'scudo':
            if monete >= 30:
                 monete -= 30
            else:
                print("L'acquisto non può essere effettuato, saldo insufficiente!")
        elif acquisto == 'pozione':
            if monete >= 10:
                monete -= 10
            else:
                print("L'acquisto non può essere effettuato, saldo insufficiente!")
    elif schermata_iniziale == 3:
        vendita_oggetto = input("Scegli quale oggetto vuoi vendere:\n")
        vendita_oggetto = vendita_oggetto.lower()
        if vendita_oggetto in inventario:
            inventario.remove(vendita_oggetto)
            if vendita_oggetto == "spada":
                monete += 25
            elif vendita_oggetto == "scudo":
                monete += 15
            elif vendita_oggetto == "pozione":
                monete += 5
        else:
            print("L'oggetto non è presente nell'inventario!")
    elif schermata_iniziale == 4:
        print(f"Il tuo saldo ammonta a {monete}")
    elif schermata_iniziale == 5:
        print("Sei uscito dal gioco!")
        break
