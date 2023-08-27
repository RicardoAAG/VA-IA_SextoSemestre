#explicacion: https://www.youtube.com/watch?v=KW5gvhOPdcA

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:36:40 2023

@author: super
"""

def prim(a,n,s):
    agregados=[] #lista con los nodos ya agregados
    suma=0 #suma total
    while(len(agregados)!=n): #se llena la lista con 0, indicando que ningun nodo ha sido agregado
        agregados.append(0) 
    agregados[s]=1 #se marca el nodo inicial como agregado
    final=[] #lista para almacenar el arbol final
    for i in range(0,n-2): #el for es para agregar aristas, es n-2 y no n-1 por hay un vertice 0 que no existe
        min=m
        for j in range(0,n): #este for revisa el nodo de salida y j representa ese nodo
            if(agregados[j]==1): #si el nodo de salida ya fue agregado entonces se revisan sus destinos
                for k in range(0,n): #este for revisa todos los nodos destino del nodo de salida j, llamados k
                    if(agregados[k]==0 and a[j][k]<min): #el if entra si el nodo destino no ha sido agregado y su distancia con el nodo de salida es menor al minimo
                        agregar_vertice=k #de ser el tomo dicho nodo de destino como candidato para ser agregado
                        e=[j,k] #se toma la arista para ser agregada
                        min=a[j][k] #y se actualiza la distancia minima a la distancia a la distancia de la arista, para poder usarla para comparar las siguientes aristas
        agregados[agregar_vertice]=1 #una vez que se hayan revisado todos los nodos se toma el mejor candidato y se marca como agregado
        final.append(e) #se agrega dicha arista a la lista final
        suma+=a[e[0]][e[1]] #y se suma su distancia a la suma final
        print(a[e[0]][e[1]])
        #como ya se agrego una arista se regresa al primer for y se busca la siguiente arista
    return [final,suma] #al final retorna las aristas finales y la suma de sus pesos


m=999
n=7

INICIO=1

#Vertice 0 no existe, pero es necesario para que inicie desde 1
w=[#0 1 2 3 4 5 6
   [m,m,m,m,m,m,m],#0
   [m,m,4,2,m,3,m],#1
   [m,4,m,m,5,m,m],#2
   [m,2,m,m,1,6,3],#3
   [m,m,5,1,m,m,6],#4
   [m,3,m,6,m,m,2],#5
   [m,m,m,3,6,2,m],#6
]


print(prim(w,n,INICIO))
