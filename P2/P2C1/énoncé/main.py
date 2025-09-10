#1
nombre1 = input("Fournissez un premier nombre: ")
nombre2 = input("Fournissez un second nombre: ")

#2
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur les nombres doivent être entiers")
#3
    raise SystemExit("Fin du programme")

#4
nombre1 = int(nombre1)
nombre2 = int(nombre2)

#5
operation = input("Entrez l'opérateur souhaitée '+', '-', '*' ou '/' : ")

#6
if operation not in ["+", "-", "*", "/"]:
    print("L'operateur choisis n'existe pas")
    raise SystemExit("Fin du programme")

#7,8,9,10
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 == 0:
        print("Vous ne pouvez pas diviser un chiffre/nombre par 0")
        raise SystemExit("Fin du programme")
    
    resultat = round(nombre1 / nombre2, 2)

print(f"Le resultat du calcul est : {resultat} :)")
