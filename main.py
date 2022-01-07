#Exo 1
def extrait_ensemble_des_voyelles(mot):
    voyelles = ("a","e","i","o","u","y")
    conteneu =[]
    for i in mot:
        if i in voyelles:
            conteneu.append(i)
    return conteneu

#Exo 2
def transforme_lettres_numbres(mot):
    liste =["a", "b", "c", "d"]
    numero = []
    for i in mot:
        numero = liste.index(i)+1
        numero.append(str(numero))
    listjoin=".".join(numero)
    return listjoin

        
    