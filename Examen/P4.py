import copy


class AN:
    def __init__(self, sc=None, dd=None):
        self.dd = dd
        self.sc = sc
        self.hc = {}

    def tres(self, val, future_dd_val):
        """
        ** 3 puntos **
        Inserta un nodo a la estructura. El nodo tiene valor val y su padre es future_dd_val.
        Verifica que el actual nodo sea el padre. Si lo es, lo agrega y retorna true. En caso contrario
        busca al padre en en sus hijos.
        """
        if self.sc == future_dd_val:
            self.hc[val] = AN(sc=val, dd=self)
            return True
        for c in self.hc.values():
            c.tres(val, future_dd_val)
        return False

    def nif(self, sc, cm_):
        """
        ** 4 puntos **
        Busca al path de un valor dado desde el nodo self. Solo entrega el path para el primer nodo que
        encuentra. Un out es una lista de objetos AN
        """
        if self.sc == sc:
            return cm_
        for c in self.hc.values():
            out = c.nif(sc, cm_ + [c.sc])
            if out is not None:
                return out
        return None

    def deno(self, cm_):
        """
        ** 4 puntos **
        Elimina el último nodo de la lista cm_. Se asume que cm_ es un camino que permite encontrar al
        nodo que se está buscando.
        El reocorre todos los elementos AN hasta terminar de buscar en la lista. Aqui se autoelimina
        el nodo de la lista
        """
        if len(cm_) == 0:
            aux = copy.copy(self.dd.hc[self.sc])
            del self.dd.hc[self.sc]
            return aux
        next = cm_.pop(0)
        return self.hc[next].deno(cm_)

    def tres_ned_cm(self, ned, cm_):
        """
        ** 3 puntos **
        Este método inserta un objeto AN dado el camino entregado en cm_
        """
        if len(cm_) == 0:
            self.hc[ned.sc] = ned
            return

        next = cm_.pop(0)
        self.hc[next].tres_ned_cm(ned, cm_)

    def inte(self, val_origen, val_destino):
        """
        ** 3 puntos **
        Este metodo intercambia dos nodos. Primero busca el camino para llegar a cada uno de ellos,
        luego se eliminan los dos nodos, y finalemente se insertan el nodo 1 en la antigua posicion del 2
        y el 2 en la antigua posicion del 1.
        """
        cm_1 = self.nif(val_origen, [])
        cm_2 = self.nif(val_destino, [])
        aux_1 = self.deno(copy.copy(cm_1))
        aux_2 = self.deno(copy.copy(cm_2))
        self.tres_ned_cm(aux_2, cm_1[:-1])
        self.tres_ned_cm(aux_1, cm_2[:-1])


if __name__ == "__main__":
    # ** 3 puntos por el main **
    # Se crea una estructura de arbol
    an = AN(4)
    an.tres(2, 4)
    an.tres(3, 4)
    an.tres(1, 2)
    an.tres(5, 2)
    an.tres(6, 3)
    an.tres(8, 2)
    an.tres(7, 3)
    an.tres(7, 6)
    # No ubica a este valor en niguna parte. Ver imagen 1
    an.tres(10, 11)
    # Se busca el camino hasta un nodo de valor 7. En este caso puede encontrar 2:
    # 3 -> 7
    # 3 -> 6 -> 7
    # Depende de cómo se haya guardado el diccionario.
    out = an.nif(7, [])
    print(out)

    # Aquí elimina el Elemento del path que haya encontrado. La imagen 2 muestra una
    # de las dos posibles configuraciones
    an.deno(out)

    # Crea una nueva estructura
    an_n = AN(15)
    cm_aux = [2, 5]
    # Agrega el elementp an_n a en el nodo 5 que es hijo del nodo 2. Ver imagen 3
    an.tres_ned_cm(an_n, cm_aux)
    # Intercambia los nodos de valores 2 y 6. Ver imagen 4
    an.inte(2, 6)

