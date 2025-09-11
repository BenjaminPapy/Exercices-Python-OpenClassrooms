#1
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

#2
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

#3
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

#4
salaire_annuel = float(input("Bonjour, veuillez rentrer votre salaire annuel : "))

#5
heures_travaillees = float(input("Veuillez également renseigner votre nombre d'heures travaillés par semaine : "))

#6
mensuel = salaire_mensuel(salaire_annuel)

hebdo = salaire_hebdomadaire(mensuel)

horaire = salaire_horaire(hebdo, heures_travaillees)

#7
print("Votre salaire horaire est de", round(horaire, 2), "euros")