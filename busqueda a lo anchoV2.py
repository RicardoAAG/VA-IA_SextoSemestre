import re 
patron=re.compile(r'\W')

def bus_anchura(E,ni,V):
    nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    vi=nodos[ni]
    V=patron.split(V)

    v1=V[vi]
    Vp=[v1] #Explorados

    Ep=[] #Final
    S = [v1] #Nivel de busqueda
    while True:
        bandera = True
        V_S=[] #Descubiertos en el nivel de busqueda actual
        for x in S: #se inicia la busqueda en cada nodo del nivel de busqueda actual
            Vdiff = [z for z in V if z not in Vp] #se crea la lista de nodos no exploradoos, quitandole los ya explorados
            print(Vdiff)
            for y in Vdiff: #revisa cada nodo no explorado
                if ((x,y) in E): #revisa si la combinacion entre el nodo del que se esta buscando (x) y el nodo no descubierto (y) existe
                    vk=(x,y)                    
                    Ep.append(vk)
                    Vp.append(y)
                    V_S.append(y) #si ese es el caso los junta, los agrega al arbol final, agrega ese nodo como nodo explorado y lo agrega como nodo descubierto
                
                    bandera = False
        if bandera==True: #se entra a este if si no se logran encontrar aristas nuevas
            print("Anchura resuelto",Ep)
            return Ep
        S = V_S #el nivel de busqueda actual ahora son los nodos descubiertos     
        
vi='a'
V=('a b c d e f g h')

E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')}

bus_anchura(E,vi,V)