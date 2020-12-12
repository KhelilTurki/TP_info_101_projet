def generer_dico(nf):
    fichier = open(nf, "r")
    nblignes = fichier.readlines()
    dico=[]
    for i in range(len(nblignes)):
        dico.append(fichier.readline())
    print(dico)
    fichier.close()

#generer_dico('littre.txt')

def mot_jouable(mot, ll):
    lmot = list(mot)
    lmot2 = lmot
    check = False
    
    for i in range (0, len(ll)) :
        for j in range (0, len(lmot) - 1) :
            if (ll[i] == lmot[j]):
                lmot2.remove(lmot[j])
    
    if (lmot2[len(lmot2) - 1] in ll) :
        lmot2.remove(lmot2[len(lmot2) - 1])
        
    if ('*' in ll and len(lmot2) != 0) :
        lmot2.remove(lmot2[len(lmot2) - 1])

    if (len(lmot2) == 0) :
        check = True
    
    return check

def mots_jouables(motsfr, ll):
    liste = []
    for i in range (0, len(motsfr)):
        if (mot_jouable(motsfr[i], ll) == True) :
            liste.append(motsfr[i])

    return liste

#print(mots_jouables(["COURIR", "PIED", "DEPIT", "TAPIR", "MARCHER"], ["P", "I", "D", "E", "T", "A", "R"]))
