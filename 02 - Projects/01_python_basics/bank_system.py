def bank_system(saldo, transazioni):
    while True:
        c_s = int(input(
        '1. Visualizza saldo\n' 
        '2. Deposita denaro\n' 
        '3. Preleva denaro\n'
        '4. Visualizza transazioni:\n' 
        '5. Esci\n' 
        "Segli un'opzione"
        ))
        nuovo = 0
        if c_s == 1:
            print(f"Il tuo saldo ammonta a {saldo}")
        elif c_s == 2:
            aggiunta = float(input("Digitare la somma da depositare:"))
            nuovo = saldo + aggiunta
            saldo+=aggiunta
            print(f"Il tuo saldo ora ammonta a {nuovo}")
            transazioni.append(f"Deposito: {aggiunta}")
        elif c_s == 3:
            prelievo = float(input("Digitare la somma da prelevare"))
            while prelievo > saldo:
                prelievo = float(input("I soldi che vuoi prelevare sono maggiori del saldo, preleva una cifra inferiore! REinserisci quanto vuoi prelevare:"))
            else:
                nuovo = saldo - prelievo
                saldo-=prelievo
                print(f"Il tuo saldo ora ammonta a {nuovo}")
                transazioni.append(f"Prelievo: {prelievo}")
        elif c_s == 4:
            for transazione in transazioni:
                print(transazione)
        elif c_s == 5:
            print("Hai eseguito il log out dal tuo account")
            break

def main():
    saldo = 1000
    transazioni = []
    ris = bank_system(saldo, transazioni)
main()
