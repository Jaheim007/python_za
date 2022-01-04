# def effect():
#     print("---------------------------\n  EFFECTUER UN LIVRAISON\n---------------------------\n ")
#     reponse_2 = "oui"
#     while reponse_2 != "non":
#         global commande
#         try:
#             email = input("Veuillez entrer l'email du client:\t ")
#             name_produit = input("Veuillez saisir le nom de produit:\t ")
#             val_produit = int(input("Veuillez saisir la quantité de produit:\t "))
#             if email in infos.values():
#                 quantite[name_produit] -= val_produit
#                 commande[name_produit] = val_produit
#                 historique[email] = commande
#                 for key,value in quantite.items():
#                     print(f'{key} : {value}')
#                 print("Votre commande a été effectuée")
#                 commande ={}
#             elif name_produit not in quantite:
#                 print("Cette adresse email n'existe pas, veuillez retournez a option 2")
#         except KeyError:
#             print("Ce produit n'existe pas ")
#         else:
#             pass
        
#         reponse_2 = input("Voulez-vous effectue d'autres livraisons (oui/non):\t ")