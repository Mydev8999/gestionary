import os
import shutil

chemin = "C:\\Users\\emilien\\OneDrive\\Bureau\\python codeur dojo\\dossier gestionaire"

os.chdir(chemin)


def menu():
                                                                                                                     
    print("\n1) créer dossier")
    print("2) renomer")
    print("3) supprimer dossier")
    print("4) créer fichier")
    print("5) supprimer fichier ")
    print("6) rentrer dans un dossier  ")
    print("7) retour parent (dossier précédant)")
    print("8) lire le contenu d'un fichier")
    a = input("votre choix: ")

    if a == "1":
        creer_dossier()
    elif a == "2":
        renomer()
    elif a == "3":
        suppr_dossier()
    elif a == "4":
        creer_fichier()
    elif a == "5":
        suppr_fichier()
    elif a == "6":
        rentrer_dossier()
    elif a == "7":
        retour_parent()
    elif a == "8":
        lire_fichier()

           

def afficher_dossier():
   liste_fichier = os.listdir(".")
   print(liste_fichier)



def creer_dossier():
    nomDossier = input("nom du dossier: ")
    os.mkdir("." + "\\" + nomDossier)

def suppr_dossier():
    nom_a_supprimé = input("entrée le nom du dossier a supprimé: ")
    chemin_total = "." + "\\" + nom_a_supprimé
    shutil.rmtree(chemin_total)

def creer_fichier():
    nom_fichier = input("nom du fichier: ")
    fichier_chemin = "." + "\\" + nom_fichier
    f = open(fichier_chemin, "w")
    f.close()
    

def suppr_fichier():
    fichier_nom = input("nom du fichier: ")
    chemin_fichier = "." + "\\" + fichier_nom
    os.remove(chemin_fichier)

def renomer():
    nom_ancien = input("nom du fichier/dossier à renomer: ")
    total_chemin = "." + "\\"  + nom_ancien
    nom_nouveau= input("nouveau nom: ")
    total_nouveau = "." + "\\" + nom_nouveau
    os.rename(total_chemin, total_nouveau)

def rentrer_dossier():
    name_repertory_enter = input("entrez le nom du dossier: ")
    os.chdir(name_repertory_enter)

def retour_parent():
    # Obtenir le chemin absolu du dossier parent
    chemin_parent = os.path.abspath('..')

    # Changer de répertoire pour le dossier parent
    os.chdir(chemin_parent)

def lire_fichier():
    nom_lire_fichier = input("entrez le nom du fichier à lire: ")
    
    with open(nom_lire_fichier) as fichier:
        print("\n")
        print("-------------------------------")
        print(fichier.read())
        print("-------------------------------\n")
        


    



    


while True:
    afficher_dossier()
    menu()








