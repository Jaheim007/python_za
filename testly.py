import json

chemin = "commande.json"

nom_produit = input("veuillez ajouter un produit :\t")
qte = int(input("veuillez renseingner la quantite du produit :\t"))

dicty = {}
try:
    with open(chemin, "r") as f:
        test = json.load(f)

    dicty[nom_produit] = qte
    
    

    with open(chemin, "w") as f:
        json.dump(dicty,f)
except json.decoder.JSONDecodeError:
    print("ok")
    