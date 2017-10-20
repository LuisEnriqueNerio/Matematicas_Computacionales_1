# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:29:13 2017

@author: Luis Nerio
"""
import math

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
        #self.E[(v,u)] = peso
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



def dijkstra(g, actual):
    distancia = dict()
    previo = dict()
    vertices = g.V.copy()
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
        print(u)
        vertices.remove(u)
        
        for v in g.vecinos[u]:
            alternativa = distancia[u]+g.E[(u,v)]
            if alternativa < distancia[v]:
                distancia[v]=alternativa
                previo[v]=u
        print(distancia)
    return (distancia,previo)

g=grafo()
g.conecta('A','B',8)

g.conecta('A','C',2)

g.conecta('A','D',5)

g.conecta('B','F',13)

g.conecta('B','D',2)

g.conecta('C','D',2)

g.conecta('C','E',5)

g.conecta('D','F',6)

g.conecta('D','G',3)

g.conecta('D','E',1)

g.conecta('E','G',1)

g.conecta('G','H',6)

g.conecta('F','H',3)

g.conecta('F','G',2)