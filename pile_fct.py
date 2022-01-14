def creer_pile(n):
    p=(n+1)*[None]
    p[0]=0
    return(p)

def empiler(p,x):
    n=p[0]
    assert n<len(p)-1, "La pile est pleine"
    n=n+1
    p[0]=n
    p[n]=x
    return(p)
 
def depiler(p):
    n=p[0]
    assert n>0, "La pile est vide"
    x=p[p[0]]
    p[n]=None    
    p[0]=n-1
    return(x)
    
def pile_vide(p):
    if p[0]==0 :
        return(True)
    else :
        return(False)

def taille_pile(p) :
    return(p[0])
    
def sommet_pile(p) :
    assert taille_pile(p)>0
    return(p[p[0]])

def inverser_pile(p) :
    p2=creer_pile(taille_pile(p))
    for i in range (taille_pile(p)):
        empiler(p2,depiler(p))
    return(p2)

def depiler_jusqua(p,x) :
    for i in range(taille_pile(p)) : 
        if p[p[0]]==x : 
            return(p)
        depiler(p)
    return("La lettre n'appartient pas à la liste")