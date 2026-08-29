psw = input("Inserisci la password di pyton")
while psw != "python123":
    print("La password è errata, riprova!")
    psw = input("Riprova")
else:
    print("Password corretta!")
