# Creado por Jesus Imitola
# GitHub User: jgimitola
# Fecha: del 19 de Abril de 2020 hasta el 22 de Abril de 2020.

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
        n = len(self.elementos)
        proxima = self.elementos.copy()
        nacimientos = self.nacimientos()
        muertes = self.muertes()
        for i in range(n):
            for j in range(n):
                vecis = [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j), (i - 1, j - 1), (i + 1, j - 1),
                         (i - 1, j + 1),
                         (i + 1, j + 1)]

                if (i, j) in nacimientos:
                    proxima[(i, j)]["vivo"] = True
                    for vec in vecis:
                        if vec in proxima:
                            proxima[vec]["vecinos"] += 1

                elif (i, j) in muertes:
                    proxima[(i, j)]["vivo"] = False
                    for vec in vecis:
                        if vec in proxima:
                            proxima[vec]["vecinos"] -= 1
        return Generacion(self, proxima)
