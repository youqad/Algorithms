from collections import deque

class Noeud():
    def __init__(self, numero, voisins=[]):
        self.numero = numero
        self.voisins = set(voisins)
        
    def __str__(self):
        return self.numero
    
    def BFS(self):
        deja_vu = {i:False for i in self.adj.keys()}
        file = deque([self.numero])
        
        while file:
            v = file.pop()
            if deja_vu[v]:
                continue
            yield v
            deja_vu[v] = True
            
            file.extendleft([i for i in self.adj[v] if not deja_vu[i]])
        
    def DFS(self):
        deja_vu = {i:False for i in self.adj.keys()}
        pile = [self.numero]
    
        while pile:
            v = pile.pop()
            if deja_vu[v]:
                continue
            deja_vu[v] = True
            yield v
            
            pile.extend([i for i in self.adj[v] if not deja_vu[i]])
            
    def __iter__(self):
            yield from self.DFS()


class Noeud_Ordonne(Noeud):
    def __init__(self, numero, voisins=[]):
        self.numero = numero
        self.voisins = list(voisins)
    
        
        
class Graphe():
    def __init__(self, dic={}, taille=0):
        if not dic:
            self.adj = {Noeud(i) for i in range(taille)}
        else:
            self.adj = {Noeud(i,set(j)) for i,j in dic.items()}
        
    def __contains__(self, x):
        return x in self.adj
        
    def BFS(self, x=0):
        assert x in self
        deja_vu = {i:False for i in self.adj.keys()}
        file = deque([x])
        
        while file:
            v = file.pop()
            if deja_vu[v]:
                continue
            yield v
            deja_vu[v] = True
            
            file.extendleft([i for i in self.adj[v] if not deja_vu[i]])
        
    def DFS(self, x=0):
        assert x in self
        deja_vu = {i:False for i in self.adj.keys()}
        pile = [x]
    
        while pile:
            v = pile.pop()
            if deja_vu[v]:
                continue
            deja_vu[v] = True
            yield v
            
            pile.extend([i for i in self.adj[v] if not deja_vu[i]])
            
    def __iter__(self):
        if not self.adj:
            return ()
        else:
            yield from self.DFS(next(iter(self.adj)))
        
    def __str__(self):
        return str((len(self), self.adj))
    
    def __len__(self):
        return len(self.adj)
    
    
    
class Graphe_Ordonne(Graphe):
    def __init__(self, dic={}, taille=0):
        if not dic:
            self.adj = {i:[] for i in range(taille)}
        else:
            self.adj = {i:list(j) for i,j in dic.items()}
    
        
class Arbre(Noeud_Ordonne):
    def __init__(self, rac, *fils):
        Noeud_Ordonne.__init__(rac, fils)
    
    
        
            

G = Graphe({0:[1,2,3],1:[2,3],2:[],3:[0,1]})
G = Arbre(0, Arbre(1))

for i in G:
    print(i)

for i in G.BFS():
    print(i)
    
    