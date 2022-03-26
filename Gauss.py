import numpy as np # Importation de numpy
np.set_printoptions(precision=3, suppress=True) # Affichage des réels

def Echange(i, j, m):
    resultat = np.copy(m)
    resultat[i, :] = m[j, :]
    resultat[j, :] = m[i, :]
    return resultat
    
def CombinaisonLineaire(i, coeff, j, M):
    res = np.copy(M)
    res[i, :] = M[i, :] + M[j, :] * coeff
    return res

def ChoixPivot(j, M):
    for i in range(M.shape[0]):
        if M[i, j] != 0 and i >= j:
            return i
    return None
    
def Echelonne(A):
    """
    param A:np.array
        /matrice correspondant à un système linéaire
    return :np.array
        /système linéaire échelonné
        
        |x, y, Z=?|
        | , y, Z=?|
        | ,  , Z=?|
    """
    copy = np.copy(A)
    for i in range(len(A)-1):
        lignepivot = ChoixPivot(i, copy)
        Echange(i-1, lignepivot, copy)
        pivot = copy[i+1, i]
        for j in range(i+1, len(A)):
            coeff = copy[j, i]/ copy[i, i]
            copy = CombinaisonLineaire(j, -coeff, i , copy)
    return np.around(copy, 8)
    
def Gauss(A):
    """
    param A:np.array
        /matrice correspondant à un système linéaire
    return :np.array
        /solution du système linéaire
    """
    copy = np.copy(Echelonne(A))
    
    #reduction du système linéaire
    for i in range(len(copy)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if copy[j, i] != 0:
                coeff = -(copy[j, i]/(copy[i, i]))
                copy = CombinaisonLineaire(j, coeff, i, copy)
    """
    après cette partie de code:
        |x,  ,  =?|
        | , y,  =?|
        | ,  , Z=?|
    """
    #solution unique
    return np.array([copy[k, -1]/copy[k, k] for k in range(len(A))])
    #je ne sais pas trop si il fallait prendre en compte les cas de solution
    #tel que les solution infini ou les solution nulle. Du coup je ne les ai
    #pas traité
