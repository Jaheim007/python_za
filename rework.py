print("----------------------------------------------------\n Bienvenue dans mon programme de gestion des stocks".title()) 
menu = "----------------------------------------------------\n 1.Se Ravitailler \n 2.Ajouter Un Client \n 3.Effectuer Un Livraisons \n 4.Voir L'historique Des Livraisons \n 5.Afficher Le Stock \n 6.Editer Un Produit \n 7.Editer Un Cilent \n NB:Pour Sortir Du Programme Appuyez Sur La Touche  Enter"

quantite = {
     "pomme" : 10,
     "banane": 9,
     "raisins": 5, 
}

infos = {
    "Nan" : "nan@yahoo.com",
    "Jah" : "jah@mail.com",
    "@": "@"
}

commande={}
historique ={}

def se():
    print("--------------------\n   SE RAVITAILLER\n--------------------\n ")
    reponse = "oui"
   
    while reponse != "non":
        nom_produit = input("Veuillez entre le nom de produit:\t ")
        value_produit = int(input("Veuillez entre la quantite:\t "))
        
        if nom_produit in quantite:
                quantite[nom_produit] += value_produit
                print("Votre produit a été ajouté")
        
        elif nom_produit not in quantite:
                quantite[nom_produit] = value_produit
                print("Votre produit a été ajouté")
        else:
            pass
        
        for key,value in quantite.items():
            print(f'{key} : {value}')
        
        reponse = input("Voulez-vous ajouter d'autres produits (oui/non):\t ")
        
    
def ajout():
    print("--------------------\n AJOUTER UN CLIENT\n--------------------\n ")
    reponse_1= "oui"
    
    while reponse_1 != "non":
        nom_client = input("Veuillez le nom du client:\t")
        email_client = input("Veuillez l'email du client:\t")
        
        if nom_client in infos:
            print("Cet e-mail existe déjà!")
        
        else:
            infos[nom_client] = email_client
        
        for key,value in infos.items():
            print(f'{key} : {value}')
        
        reponse_1 = input("Voulez-vous ajouter d'autres clients (oui/non):\t ")

def effect():
    print("---------------------------\n  EFFECTUER UN LIVRAISON\n---------------------------\n ")
    reponse_2 = "oui"
    
    while reponse_2 != "non":
        global commande
        try:
            email = input("Veuillez entrer l'email du client:\t ")
            name_produit = input("Veuillez saisir le nom de produit:\t ")
            val_produit = int(input("Veuillez saisir la quantité de produit:\t "))
            
            if email in infos.values():
                quantite[name_produit] -= val_produit
                commande[name_produit] = val_produit
                historique[email] = commande
                
                for key,value in quantite.items():
                    print(f'{key} : {value}')
                print("Votre commande a été effectuée")
                commande ={}
            
            if name_produit not in quantite:
                print("Cette adresse email n'existe pas, veuillez retournez a option 2")
        
        except KeyError:
            print("Ce produit n'existe pas ")
        
        except ValueError: 
            print("Cet quantite n'existe pas.")
        
        else:
            pass
        
        reponse_2 = input("Voulez-vous effectue d'autres livraisons (oui/non):\t ")

def voir():
    print("------------------------------------\n  VOIR L'HISTORIQUE DES LIVRAISONS\n------------------------------------\n ")
    
    for e,v in historique.items():
        print(f'Client: \t {e}')
        
        for produit,quantite in v.items():
            print(f'{produit}:\t{quantite} \n')

        
def affic(): 
    print("--------------------\n AFFICHER LE STOCK\n--------------------\n ")
    
    for key,value in quantite.items():
        print(f'-----------------------------\nProduit:\t {key}\n\nDisponible:\t {value}\n-----------------------------\n')

def editp():
    print("--------------------\n EDITER UN PRODUIT\n--------------------\n ")
    reponse_4 = "oui"
    
    while reponse_4 != "non":
        produit_editer = input("Veuillez saisir le nom du produit:\t")
        quantite_editer = int(input("Veuillez saisir la quantite:\t"))
        
        try: 
            
            if produit_editer in quantite:
                new_produit = input("Veuillez saisir le nouveau produit:\t")
                quantite[new_produit] = quantite.pop(produit_editer)
            
            if quantite_editer in quantite.values():    
                new_quantite = input("Veuillez saisir la nouvelle quantité:\t")
                quantite[new_produit] = new_quantite
                quantite.update()
                
                for key,value in quantite.items():
                    print(f'------------\n Nouveau Produit:\t {key}\n Nouveau Quantite:\t {value}\n------------\n')
        
        except ValueError:
            print("Cette quantité n'existe pas")
        
        except KeyError:
            print("Ce produit n'existe pas")
        
        else: 
            pass
        
        reponse_4 = input("Voulez-vous éditer d'autres produits(oui/non):\t")    

def editc():
    print("--------------------\n EDITER UN CLIENT\n--------------------\n ")
    reponse_5 = "oui"
    
    while reponse_5 != "non":
        client_modifer = input("Veuillez saisir le nom du client:\t")
        
        if client_modifer in infos:
            new_name = input("Veuillez saisir le nouveau nom du client:\t")
            infos[new_name] = infos.pop(client_modifer)
            
            for key,value in infos.items():
                print(f'{key} : {value}')
        
        else:
            print("Ce client n'existe pas")
        
        reponse_5 = input("Voulez-vous editer une autre client(oui/non):\t")
        
def error():
    print("Veuillez saisir une autre options.")

chose_menu = {
    "1" : se,
    "2" : ajout,
    "3" : effect,
    "4" : voir, 
    "5" : affic, 
    "6" : editp, 
    "7" : editc, 
}
options = "-"

while options != "":
    print(menu)
    options = input("Veuillez choisir une option:\t ")
    chose_menu.get(options , error)()

