# Creado por Jesus Imitola
# GitHub User: jgimitola
# Fecha: del 19 de Abril de 2020 hasta el 22 de Abril de 2020.

import numpy
from Generacion import Generacion


class Game:
    def __init__(self, n, N, elementos={}):
        if elementos == {}:
            for i in range(n):
                for j in range(n):
                    elementos[(i, j)] = {
                        "vivo": False,
                        "vecinos": 0
                    }

            # Posicionamos las N0 celulas iniciales aleatoriamente.
            puestos = 0
            while puestos < N:
                x = int(numpy.random.uniform(0, n))
                y = int(numpy.random.uniform(0, n))
                if not elementos[(x, y)]["vivo"]:
                    elementos[(x, y)]["vivo"] = True
                    vecis = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y - 1),
                             (x - 1, y + 1),
                             (x + 1, y + 1)]
                    for vec in vecis:
                        if vec in elementos:
                            elementos[vec]["vecinos"] += 1
                    puestos += 1

        self.inicio = Generacion(None, elementos)

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if len(self.actual.vivos()) > 0:
            self.actual = self.actual.siguiente()
            return self.actual
        else:
            raise StopIteration
