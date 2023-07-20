import sqlite3
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS solde(id INTEGER PRIMARY KEY AUTOINCREMENT ,solde BOOLEAN,unite TEXT)"
    )
cursor.execute(
    "CREATE TABLE IF NOT EXISTS depense(id INTEGER PRIMARY KEY AUTOINCREMENT ,depenses BOOLEAN,unite TEXT)"
    )
cursor.execute(
    "CREATE TABLE IF NOT EXISTS nouveau_solde(id INTEGER PRIMARY KEY AUTOINCREMENT , nouveausolde BOOLEAN,unite TEXT)"
    )
#ajouter un solde
def ajouter_solde():
    print("Ajouter votre solde svp!\n")
    solde = input("Ajouter votre solde\n")
    unite = "fcfa"
    sld = cursor.execute("INSERT INTO solde(solde,unite) VALUES (?, ?)", ((solde),(unite),)
                   )
    connection.commit()
    print("Solde ajoutee avec succe.",sld)
 #ajouter une depense   
def ajouter_depense():
    print("Ajouter vos depenses svp!\n")
    depenses = input("Ajouter vos depenses\n")
    unite = "fcfa"
    dpns = cursor.execute("INSERT INTO depense(depenses,unite) VALUES (?, ?)", ((depenses),(unite),)
                   )
    connection.commit()
    print("Depenses sont ajoute avec succe!.",dpns)
 #nouveau solde   
def nouveau_solde():
    unite = "fcfa"
    print("Votre nouveau solde est de:\n")
    nouveauSolde = input("votre nouveau solde est:\n")
   
    new = cursor.execute("INSERT INTO nouveau_solde(nouveausolde,unite) VALUES (?, ?)", ((nouveauSolde),(unite),)
                   )
    connection.commit()
    
    print("Voila l'etat actuel de votre budget \n",new)
    


def ajouter_action():
    action = " "
    print("--------------------------------------------------------------")
    print("                     Gestion de budget                        ")
    print("--------------------------------------------------------------")
    print("                     1)Ajouter votre solde svp!\n")
    print("                     2)Ajouter vos depenses svp!\n")
    print("                     3)Votre nouveau solde est de:\n")
    print("                     0)QUITTER\n")
    action = input("Quel service voulez-vous?\n")
    if action == "1":
        ajouter_solde()
        ajouter_action()
     
    elif action == "2":
        ajouter_depense()
        ajouter_action()
        
    elif action == "3":
        nouveau_solde()
        ajouter_action()
       
    elif action == "0":
        print("Merci!!!!!\nVous avez quitte l'application.")
        exit()
      
    else:
        print("Action non requise")

ajouter_action()