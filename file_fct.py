def creer_file():
    return []

def ajouter(p,x):
    p.append(x)
    return p
 
def suivant(p):
    if not file_vide(p):
        return p.pop(0)
    else:
        return None
    
def file_vide(p):
    return len(p) == 0

def taille_file(p) :
    return len(p)
    
def premier(p) :
    if not file_vide(p):
        p[0]
    else:
        return None
