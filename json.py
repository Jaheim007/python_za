import json  
menu = "Se ravitailler"

def se():
    print("Se Ravitailler1")
    nom_produit = input("Veuillez saisir le nom du produit:\t")
    value_quantite = int(input("Veuillez saisir la quantite du produit:\t"))
    dicty_quantite={}
    try:
        with open("commande.json ", "r") as f:
            json.load(f)
        if nom_produit in dicty_quantite:
                dicty_quantite[nom_produit] += value_quantite
                print("Votre produit à été mis a jour")
        elif nom_produit not in dicty_quantite:
                dicty_quantite[nom_produit]= value_quantite
                print("Votre produit à été ajouté ")

        with open("quantite.json", "w") as f:
            json.dump(dicty_quantite,f)
    
    except json.decoder.JSONDecodeError:
        print("ok")
def error():
    print("Veuillez saisir une autre option")

chose_menu = {
    "1": se
}
options ="oui"
while options == "oui":
    print(menu)
    options = input("Veuillez choisir une option:\t ")
    chose_menu.get(options , error)()