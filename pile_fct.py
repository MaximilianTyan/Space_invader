def creer_pile(n):
    return list(range(n))

def empiler(p,x):
    p.append(x)
    return(p)
 
def depiler(p):
    if not pile_vide(p):
        p.pop(-1)
        return p
    else:
        return p
    
def pile_vide(p):
    return len(p) == 0

def taille_pile(p):
    return len(p)
    
def sommet_pile(p) :
    if not pile_vide(p):
        return p[-1]
    else:
        return None
