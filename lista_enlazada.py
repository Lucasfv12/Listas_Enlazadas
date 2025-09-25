class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
    def __repr__(self):
        return f"Nodo {self.valor}"
        
nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo3 = Nodo(30)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3


print(nodo1.siguiente)
print(nodo2.siguiente)

actual = nodo1
while actual is not None:
    print(actual)
    actual = actual.siguiente