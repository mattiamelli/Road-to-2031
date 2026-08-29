def calcolo_area(base, altezza):
    area = (base * altezza)
    return area

def main():
    base = float(input("Inserire la lunghezza della base:"))
    altezza = float(input("Inserire la lunghezza dell'altezza:"))
    area = calcolo_area(base, altezza)
    print(f"L'area del rettangolo corrisponde a : {area}")
main()


