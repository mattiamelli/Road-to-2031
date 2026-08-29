def operazione(n1, n2, segno):
    if segno == '+':
        ris = n1 + n2
        return ris
    elif segno == '-':
        ris = n1 - n2
        return ris 
    elif segno == '*':
            ris = n1 * n2
            return ris 
    elif segno == '/':
            ris = n1 / n2
            return ris 

def main():
    n1 = float(input("Inserire il primo numero:"))
    n2 = float(input("Inserire il secondo numero:"))
    segno =str(input("Inserire il segno dell'operazione:"))
    ris = operazione(n1, n2, segno)
    print(f"Il risultato finale è: {ris}")
main()