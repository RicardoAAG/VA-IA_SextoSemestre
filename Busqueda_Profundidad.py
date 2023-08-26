#explicacion https://www.youtube.com/watch?v=2jkDHQl_T5k

# Profundidad
#Supongamos que se quiere planear un viaje entre 8 ciudades y se quiere encontrar el camino en el que se visiten
#la mayor cantidad de ciudades sin tener que recorrer el mismo camino 2 veces

import re 
patron=re.compile(r'\W')

def bus_profundidad(E,ni,V):
      nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 
      vi=nodos[ni]
      V=patron.split(V)
      v1=V[vi] #padre inicial
      Vp=[v1] #explorado
      Ep=[] #final
      w=v1 #padre actual
      padre={} #camino recorrido
      while True:
          while True:
              arista=[(w,x) for x in V if ((w,x) in E and x not in Vp)] #se buscan las aristas que salgan del nodo padre (w) siempre y cuando la arista exista y su destino no sea un nodo ya explorado
              if arista==[]: #si ninguna arista cumple esas condiciones se sale del while
                  break
              vk=arista[0] #se toma la primera de las aristas que cumplan esas condiciones
              Ep.append(vk)
              Vp.append(vk[1]) #y se agrega al final y despues se agrega el destino a los nodos explorados
              padre.update({vk[1]:w}) #se aztualiza el camino recorrido, agregando el nuevo tramo
              print(padre)
              w=vk[1] #el padre actual ahora es el destino
          if w==v1: #si se sale del while y el padre actual es el padre inicial entonces se termina
              print ("profundidad resuelto",Ep)
              break
          w=padre.get(w) #si se sale del while pero el padre actual no es el inicial, entonces ahora el padre actual es ahora igual al padre del padre actual (se regresa por el camino recorrido)
         
      return Ep

vi='a'
V=('a b c d e f g h')

E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 
bus_profundidad(E,vi,V)
