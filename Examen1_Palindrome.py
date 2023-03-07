class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prep = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendL(self,txt):
        txt = str(txt).replace(" ","").upper()
        for i in range(len(txt)):
            self._auxAppendL(txt[i])
    
    def isPalindrom(self):
        nodosIn = self.head
        nodosInOther = self.tail
        if self.length % 2 == 0:
            limit = (self.length/2) + 1
        else:
            limit = (self.length + 1)/2
        for i in range(int(limit)):
            if nodosIn.value == nodosInOther.value:
                nodosIn = nodosIn.next
                nodosInOther = nodosInOther.prep
            else:
                return False
        return True

    def printL(self):
        if self.head is not None:
            nodosIn = self.head
            while nodosIn:
                print(nodosIn.value)
                nodosIn = nodosIn.next 
        else:
            print("No hay nodos:printL")

    def printTailBackL(self):
        if self.tail is not None:
            nodosIn = self.tail
            while nodosIn:
                print(nodosIn.value)
                nodosIn = nodosIn.prep
        else:
            print("No hay nodos:printL")

    def _auxAppendL(self, value):
        if self.head is None:
            self.head = Nodo(value)
            self.tail = self.head
        else:
            self.tail.next = Nodo(value)
            self.tail.next.prep = self.tail
            self.tail = self.tail.next
        self.length+=1

""" 
appendL(*value)         => Añade el valor del parameto o parametros a la lista.
isPalindrom()           => Retorna un boleano, false en caso de que la instancia no sea un palindrome y true en caso contrario
printL()                => Imprime el valor de todos los elementos en la lista.
printTailBackL()        => Imprime el valor de todos los elementos de la lista de manera inversa.
_auxAppendL()           => Metodo privado que añade valores a la lista.
"""

my_linked_List = LinkedList()

my_linked_List.appendL(input(f"Ingresa una palabra: "))

if my_linked_List.isPalindrom():
    print("Es palindrome")
else:
    print("No es palindrome")   
