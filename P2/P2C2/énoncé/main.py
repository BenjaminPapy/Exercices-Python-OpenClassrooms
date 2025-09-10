#1, 2
nombres = input("Veuillez saisir une liste de plusieurs nombres entier séparés(ex: 1 2 3 4 ...): ")

#3
reponse = nombres.split()

#4
liste_entiers = [int(val) for val in reponse]
    
#5
resultat = 0
for nbr in liste_entiers:
    resultat += nbr
 
print(f"La somme de votre liste est : {resultat}")

#6
moyenne = resultat / len(liste_entiers)

print(f"La moyenne de cette liste est : {moyenne}")

#7
superieur_moyenne = 0

for nbr in liste_entiers:
    if nbr > moyenne:
        superieur_moyenne = superieur_moyenne + 1

print(superieur_moyenne)