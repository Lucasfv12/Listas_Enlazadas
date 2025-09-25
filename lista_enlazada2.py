class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
    def __repr__(self):
        return f"Nodo {self.valor}"
    
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)

nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

actual = nodo1
while actual is not None:
    print(actual)
    actual = actual.siguiente
    