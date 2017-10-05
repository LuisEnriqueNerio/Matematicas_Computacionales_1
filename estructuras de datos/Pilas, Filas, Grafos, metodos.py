# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:43:12 2017

@author: Luis Nerio
"""

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
        return g.E
    
    def vertices(self):
        return g.V
    
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

g = grafo()
g.conecta('a','b', 1)
g.conecta('a','c', 1)
g.conecta('a','d', 1)
g.conecta('a','e', 1)
g.conecta('a','e', 1)
g.conecta('b','f', 1)
g.conecta('c','f', 1)
g.conecta('d','g', 1)
g.conecta('e','g', 1)
print("vecinos de a:  " + str(g.vecinos['a']))
print("vertices " + str(g.V))
print("Aristas ="+ str(g.E))
g2 = g.complemento()
print("Aristas ="+ str(g2.E))