class archivosExp:
    def __init__(self, archivos, pesos, tamanio):
        self._archivos = archivos
        self._tamanio = tamanio
        self._pesos = pesos

    def f(self,cromosoma):
        f = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                f = f + self._pesos[i]
        if f < self._tamanio:
            return f
        else:
            return 0
