class Nodo_n:
    def __init__ (self, valor, hijos=[]):
        self.valor=valor
        self.hijos=hijos

def buscar(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscar_hijos(arbol.hijos,valor)

def buscar_hijos(lista,valor):
    if lista==[]:
        return False
    return buscar(lista[0],valor) or buscar_hijos(lista[1:],valor)

salida = []
with open('archivo.txt', 'r') as f:
    lineas = [linea.split() for linea in f]

for linea in lineas:
    print(linea)


a=Nodo_n(2500,[Nodo_n(50000),Nodo_n(250000),Nodo_n(2500000)])
buscar(a,2500)
