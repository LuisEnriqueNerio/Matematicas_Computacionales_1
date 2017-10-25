# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:59:31 2017

@author: Luis Nerio
"""
from copy import deepcopy
import random
import math

class grafo:
    def __init__(self):
        self.V =set() #un conjunto
        self.E = dict() #un mapeo de pesos a aritstas
        self.vecinos = dict() #un mapeo
        
    def agrega(self, v ):
        self.V.add(v)
        if not  v in self.vecinos: # vecindad de v
            self.vecinos[v]= set() #inicialmente no tiene nada
    def conecta(self, v , u , peso = 1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)] = self.E[(u,v)] = peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        
    def complemento(self):
        comp= grafo()
        for v in self.V:
            for w in self.V:
                if v != w  and (v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp
    
    def aristas(self):
        return self.E
    
    def vertices(self):
        return self.V
    
    def __str__(self):
        return "Aristas= " + str(self.E)+"\nVertices = " +str(self.V)
    
    def BFS_n(self, ni):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=fila()      ##fila con los nodos por visitar          
        Xvisitar.meter( ni )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados

    def DFS_n(self, ni):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=pila()      ##fila con los nodos por visitar          
        Xvisitar.meter( ni )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados
#    def BFS_N(self, ni):
#        visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
#        Xvisitar=fila()
#        Xvisitar.meter(  (ni,0)   )   
#        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
#            nodo = Xvisitar.obtener()
#            if nodo[0] not in visitados:
#                visitados[nodo[0]]=nodo[1]
#                for vecino in self.vecinos[nodo[0]]:
#                    #vecinos_d.append( (e,nodo[1]+1) )
#                    Xvisitar.meter((vecino,nodo[1]+1))
#                #for v in vecinos_d:
#                    #f.meter(v)
#        return visitados
 
    @property
    def diametro(self):
        maximo = 0
        for vertice in self.V:
            dic_bfs = BFS_N(self, vertice)
            if max(dic_bfs.values())>maximo:
                maximo = max(dic_bfs.values())
        return maximo
    
    @property
    def centrales(self):
        di_ma=dict()  #distancias maximas de cada vertice
        nodos_centrales=[]
        for v in self.V:
            diccionario = BFS_N(self, v)
            di_ma[v]= max(diccionario.values()  )
        radio = min(di_ma.values())
        for valor in di_ma:
            if di_ma[valor] == radio:
                nodos_centrales.append(valor)
        return nodos_centrales
    
    def dijkstra(self, actual):
        distancia = dict()
        previo = dict()
        vertices = self.V.copy()
        for v in vertices:
            distancia[v] = math.inf
            previo[v]="indefinido"
            
        distancia[actual]= 0
        
        while len(vertices)!= 0:
            minimo = math.inf
            for e in vertices:
                aux = distancia[e]
                if aux < minimo:
                    u = e
                    minimo=distancia[e]
            vertices.remove(u)
            
            for v in self.vecinos[u]:
                alternativa = distancia[u]+self.E[(u,v)]
                if alternativa < distancia[v]:
                    distancia[v]=alternativa
                    previo[v]=u   
        return (distancia,previo)    
    
    
    def kruskal(self):
        e = deepcopy(self.E)
        arbol = grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol
    
    def DFS(self,ni):
        visitados =[]
        f=pila()
        f.meter(ni)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados   
    

def BFS_N(g, ni):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=fila()
    Xvisitar.meter(  (ni,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados

def DFS_N(g, ni):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=pila()
    Xvisitar.meter(  (ni,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados


class pila(object):##quitas el mas nuevo STACK
    def __init__(self):
        self.a=[]
    
    def obtener(self):
        return self.a.pop()
    
    def meter(self, e):
        self.a.append(e)
        
    @property
    def longitud(self):
        return len(self.a)
    
    def __str__(self):
        return "<" + str(self.a)+ ">"
    
    



class fila(pila):##quitas el que ha estado mas tiempo QUEUE
    def obtener(self):
        return self.a.pop(0)

g= grafo()
g.conecta('a','b', 4)
g.conecta('a','c', 2)
g.conecta('a','d', 8)
g.conecta('a','e', 1)
g.conecta('b','c', 10)
g.conecta('b','d', 2)
g.conecta('b','e', 15)
g.conecta('c','e', 3)
g.conecta('c','d', 6)
g.conecta('d','e', 11)

print(g)
k = g.kruskal()

for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += g.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])] )
            
    c += g.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
    print('costo',c)
    
    
    
m = grafo()
m.conecta('Cola de Caballo', 'Faro de Comercio', 46)
m.conecta('Cola de Caballo', 'Chipinque', 69)
m.conecta('Cola de Caballo', 'Grutas de Garcia', 91)
m.conecta('Cola de Caballo', 'Fundidora', 47)
m.conecta('Cola de Caballo', 'Cadereyta', 63)
m.conecta('Cola de Caballo', 'Basilica', 48)
m.conecta('Cola de Caballo', 'Cerro de la Silla', 61)
m.conecta('Cola de Caballo', 'Cerro de las Mitras', 66)
m.conecta('Cola de Caballo', 'Estadio BBVA', 50)

m.conecta('Faro de Comercio','Chipinque', 30)
m.conecta('Faro de Comercio','Grutas de Garcia', 49)
m.conecta('Faro de Comercio','Fundidora', 7)
m.conecta('Faro de Comercio','Cadereyta', 38)
m.conecta('Faro de Comercio','Basilica', 5)
m.conecta('Faro de Comercio','Cerro de la Silla', 24)
m.conecta('Faro de Comercio','Cerro de las Mitras',23)
m.conecta('Faro de Comercio','Estadio BBVA', 13)

m.conecta('Chipinque','Grutas de Garcia',66 )
m.conecta('Chipinque','Fundidora', 30)
m.conecta('Chipinque','Cadereyta', 62)
m.conecta('Chipinque','Basilica', 28)
m.conecta('Chipinque','Cerro de la Silla', 48)
m.conecta('Chipinque','Cerro de las Mitras', 41)
m.conecta('Chipinque','Estadio BBVA', 37)

m.conecta('Grutas de Garcia','Fundidora', 51)
m.conecta('Grutas de Garcia','Cadereyta', 81)
m.conecta('Grutas de Garcia','Basilica',49 )
m.conecta('Grutas de Garcia','Cerro de la Silla', 68)
m.conecta('Grutas de Garcia','Cerro de las Mitras', 48)
m.conecta('Grutas de Garcia','Estadio BBVA', 56)

m.conecta('Fundidora','Cadereyta', 34)
m.conecta('Fundidora','Basilica',8 )
m.conecta('Fundidora','Cerro de la Silla', 22)
m.conecta('Fundidora','Cerro de las Mitras', 23)
m.conecta('Fundidora','Estadio BBVA', 8)

m.conecta('Cadereyta','Basilica', 38)
m.conecta('Cadereyta','Cerro de la Silla', 43)
m.conecta('Cadereyta','Cerro de las Mitras', 56)
m.conecta('Cadereyta','Estadio BBVA', 34)

m.conecta('Basilica','Cerro de la Silla', 26)
m.conecta('Basilica','Cerro de las Mitras', 25)
m.conecta('Basilica','Estadio BBVA', 15 )

m.conecta('Cerro de la Silla','Cerro de las Mitras', 45)
m.conecta('Cerro de la Silla','Estadio BBVA', 19)

m.conecta('Cerro de las Mitras','Estadio BBVA', 32)




k = m.kruskal()
for r in range(50):
    ni = random.choice(list(k.V))
    dfs =  k.DFS(ni)
    c = 0
    #print(dfs)
    #print(len(dfs))
    for f in range(len(dfs) -1):
            c += m.E[(dfs[f],dfs[f+1])]
            print(dfs[f], dfs[f+1], m.E[(dfs[f],dfs[f+1])] )
            
    c += m.E[(dfs[-1],dfs[0])]
    print(dfs[-1], dfs[0], m.E[(dfs[-1],dfs[0])])
    print('costo',c,'\n')
