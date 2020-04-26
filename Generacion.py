# Creado por Jesus Imitola
# GitHub User: jgimitola
# Fecha: del 19 de Abril de 2020 hasta el 22 de Abril de 2020.

import math


class Generacion:
    def __init__(self, anterior, elementos):
        self.anterior = anterior
        self.elementos = elementos

    def vivos(self):
        vivos = []
        for (key, value) in self.elementos.items():
            if value["vivo"]:
                vivos.append(key)
        return vivos

    def nacimientos(self):
        nacimientos = []
        for (key, value) in self.elementos.items():
            if (not value["vivo"]) and value["vecinos"] == 3:
                nacimientos.append(key)
        return nacimientos

    def muertes(self):
        muertes = []
        for (key, value) in self.elementos.items():
            if value["vivo"] and (value["vecinos"] <= 1 or value["vecinos"] >= 4):
                muertes.append(key)
        return muertes

    def siguiente(self):
        n = int(math.sqrt(len(self.elementos)))
        proxima = self.elementos.copy()
        nacimientos = self.nacimientos()
        muertes = self.muertes()
        for i in range(0, n):
            for j in range(0, n):
                vecis = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j), (i - 1, j - 1), (i + 1, j - 1),
                         (i - 1, j + 1),
                         (i + 1, j + 1)]

                if (i, j) in nacimientos:
                    proxima[(i, j)]["vivo"] = True
                    for vecino in vecis:
                        if (0 <= vecino[0] < n) and (0 <= vecino[1] < n):
                            proxima[vecino]["vecinos"] += 1
                elif (i, j) in muertes:
                    proxima[(i, j)]["vivo"] = False
                    for vecino in vecis:
                        if (0 <= vecino[0] < n) and (0 <= vecino[1] < n):
                            proxima[vecino]["vecinos"] -= 1
        return Generacion(self, proxima)
