class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
    def __repr__(self):
        return f"Nodo {self.valor}"
    
class ListaEnlazada:
    def __init__(self):
        self.head = None
        
    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo