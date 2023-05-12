## QUESTION 7
def lire1_graphe(chemin_vers_fichier):
    ## lecture du fichier
    f = open(chemin_vers_fichier)
    ligne1 = f.readline()
    lignes_suivantes = f.readlines()
    f.close()
    
    ## construction de la liste des sommets
    LS = [int(val) for val in ligne1.strip().split(' ')]
    ## ordre du graphe
    n = len(LS)
    ## construction de la liste des arcs
    Laux = []
    for elt in lignes_suivantes:
        Laux.append(elt.strip().split('\t'))
    # construction de la liste LArcs
    LArcs = []
    for elt in Laux:
        a, b = elt
        LArcs.append((int(a), int(b)))
    ## taille du graphe
    m = len(LArcs)
    
    return n, m, LS, LArcs

def arcs_vers_mat1(n, LArcs):
    M = [[0] * n for i in range(n)]
    for arc in LArcs:
        M[arc[0]][arc[1]] = 1
    return M

def charger1_graphe(chemin_vers_fichier):
    n, m, LS, LArcs = lire1_graphe(chemin_vers_fichier) # <-- dépaquetage de tuple
    return arcs_vers_mat1(n, LArcs)

## QUESTION 14
def lire2_graphe(chemin_vers_fichier):
    with open(chemin_vers_fichier) as f:
        ligne1 = f.readline()
        lignes_suivantes = f.readlines()
    #
    LS = ligne1.strip().split(' ')
    LArcs = [elt.strip().split('\t') for elt in lignes_suivantes]
    #
    return LS, LArcs

def charger2_graphe(chemin_vers_fichier):
    LS, LArcs = lire2_graphe(chemin_vers_fichier)
    #
    DLadj = {}
    for s in LS:
        DLadj[s] = []
    for arc in LArcs:
        DLadj[arc[0]].append(arc[1])
    return DLadj

def numerotation_sommets(DLadj):
    DS, cpt = dict(), 0
    for s in DLadj.keys():
        DS[s] = cpt
        cpt += 1
    return DS

def DLadj_to_Madj(DS, DLadj):
    Madj = [[0] * len(DS) for i in range(len(DS))]
    for s, Ladj in DLadj.items():
        for v in Ladj:
            Madj[DS[s]][DS[v]] = 1
    return Madj

def Madj_to_DLadj(DS, Madj):
    # construction du dictionnaire réciproque DNS
    DNS = {}
    for sommet, numero in DS.items():
        DNS[numero] = sommet
    # on initialise le dictionnaire DLadj
    #         avec pour clés tous les noms de sommets, et valeurs associées des listes vides
    DLadj = {}
    for s in DS.keys():
        DLadj[s] = []
    
    # on parcourt la matrice d'adjacence, représentée en machine par un tableau à deux dimensions
    # comportant len(Madj) et len(Madj[0]) colonnes (en verité len(Madj) = len(Madj[0]) car la matrice est carrée)
    for i in range(len(Madj)):
        for j in range(len(Madj[0])):
            if Madj[i][j] == 1: ## s'il existe un arc du sommet numéroté i vers le sommet numéroté j
                u, v = DNS[i], DNS[j] ## on détermine le noms des sommets correspondants
                DLadj[u].append(v)    ## on ajoute l'arc au dictionnaire des listes d'adjacence
    return DLadj

