import copy
import numpy as np

class Individuo:
    def __init__(self,solucion):
        self._solucion = solucion
        self._fitness = 0

class DO:
    def __init__(self,
    cantidad_individuos,
    dimensiones,
    F,
    Cr,
    problema,
    generaciones):
        self._cantidad_individuos = cantidad_individuos
        self._dimensiones = dimensiones
        self._F = F
        self._Cr = Cr
        self._problema = problema
        self._generaciones = generaciones
        self._individuos = np.array([])

    def crearIndividuos(self):
        for i in range(self._cantidad_individuos):
            solucion = np.random.randint(2, size = self._dimensiones)
            individuo = Individuo(solucion)
            self._individuos = np.append(self._individuos, [individuo])

    def mejorIndividuo(self):
        for i in self._individuos:
            fitness = self._problema.f(i._solucion)
            if fitness < self._mejor._fitness:
                self._mejor = i

    def run(self):
        self.crearIndividuos()
        self._mejor = self._individuos[0]
        self.mejorIndividuo()
        
        generacion = 0
        while (generacion <= self._generaciones):
            for idx in range(len(self._individuos)):
                while(True):
                    r1 = np.random.randint(low=1,high=len(self._individuos))
                    if(r1 != idx):
                        break
                while(True):
                    r2 = np.random.randint(low=1,high=len(self._individuos))
                    if(r2 != r1 and r2 != idx):
                        break
                while(True):
                    r3 = np.random.randint(low=1,high=len(self._individuos))
                    if(r3 != r1 and r3 != r2 and r3 != idx):
                        break
                x1 = self._individuos[r1]
                x2 = self._individuos[r2]
                x3 = self._individuos[r3]
                #Generamos nuestro vector mutacion
                V = Individuo(x1._solucion + self._F*(x2._solucion - x3._solucion))
                #Redondeo para valores discretos de la seleccion
                V._solucion = V._solucion.astype(int)
                U = []
                J = np.random.randint(low=1,high=len(self._individuos))
                for jdx in range(len(self._individuos)):
                    rcj = np.random.randint(low=0,high=1)
                    if (rcj < self._Cr or jdx == J):
                        U.append(V)
                    else:
                        U.append(self._individuos[idx])
        
            for idx in range(len(self._individuos)):
                U[idx]._fitness = self._problema.f(U[idx]._solucion)
                if(U[idx]._fitness > self._individuos[idx]._fitness):
                    U[idx]._b = copy.deepcopy(self._individuos[idx]._solucion)
                    self._individuos[idx]._fitness = U[idx]._fitness
                    if U[idx]._fitness > self._mejor._fitness:
                        self._mejor = U[idx]
               
            if generacion % 100 == 0:
                print('Generación ', generacion, ':', self._mejor._solucion,' ',self._mejor._fitness)
            generacion += 1
        return self._mejor._solucion
