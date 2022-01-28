import lecture 

def galeShapeleyEtu (pEtu, pSpe) :
    #tableau des etudiants pris
    estEnCouple = [False for i in range(len(pEtu))]
    places = [int(item[-1]) for item in pSpe]
    couples = [[False for i in range (len(pEtu))] for i in range(len(pSpe))]
    #tant qu'au moins un etudiant est libre
    while False in estEnCouple :
        etu = estEnCouple.index(False) #numero de l'etudiant
        pe = [int(item) for item in pEtu[etu][1:]] #liste des preferences ordonnee
        while not estEnCouple[etu] :
            spe = pe[0] #premiere preference (non refusee)
            #l'etudiant se propose au master
            if places[spe]>0 :
                places[spe]-=1
                estEnCouple[etu] = True
                couples[spe][etu] = True
            else :
                for e in [i for i in range(len(couples[spe])) if couples[spe][i] == True] :
                    if pSpe[spe].index(str(etu)) < pSpe[spe].index(str(e)) :
                        estEnCouple[e] = False
                        couples[spe][e] = False
                        estEnCouple[etu] = True
                        couples[spe][etu] = True
            pe = pe[1:]
    #
    for i in (range(len(couples))) :
        for j in range(len(couples[i])) :
            if couples[i][j] :
                print(pSpe[i][0]+', '+pEtu[j][0]+' sont en couples')
    return

galeShapeleyEtu(lecture.fileEtu("PrefEtu.txt"), lecture.fileSpe("PrefSpe.txt"))
