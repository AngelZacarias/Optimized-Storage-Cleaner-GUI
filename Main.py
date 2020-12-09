import os
import ArchivosExp
import AG
import DO
import PSO

def main():
    metodo = ''
    ruta = ""
    archivos = []
    pesos = []
    tamanioDeseado = 0
    
    #Obtenemos los parametros del problema
    print(":::::::: Optimizador de Limpiador de Archivos ::::::::")
    print('')
    ruta = input("Ingrese el directorio a analizar (C:\\Users\\user\\Desktop\\folder): ")
    if os.path.exists(ruta)==False:
        print("El directorio especificado no existe")
    else:
        print("Obteniendo información del directorio ",ruta," ...")
        #Obtenemos los archivos y los asignamos al problema
        tamanioActual = 0
        carpeta = os.listdir(ruta)
        for archivo in carpeta:
            rutaArchivo = ruta+'\\'+archivo
            t = int(os.path.getsize(rutaArchivo))
            archivos.append(archivo)
            pesos.append(t)
            tamanioActual += t
        print('')
        print("El directorio contiene ",len(archivos)," archivos")
        print("El directorio actual tiene archivos equivalentes a ",tamanioActual/1024/1024,"(MB)")
        
        print('')
        tamanioDeseado = float(input("Ingrese el tamanio que desea liberar (MB): "))
        tamanioDeseado=tamanioDeseado*1024*1024
        
        #Clase problema, archivos tiene los nombres de la ruta y pesos su tamaño
        directorio = ArchivosExp.archivosExp(archivos, pesos, tamanioDeseado)
        print('')
        print("Seleccione el metodo de resolución:")
        print("-Genetico")
        print("-Enjambre")
        print("-Diferencial")
        metodo=input("Ingrese el metodo a utilizar: ")
        
        #Ejecuta Algoritmo Evolutivo
        solucion = []
        if(metodo=='Genetico'):
            solucion = genetico(len(archivos),directorio)
        elif(metodo =='Diferencial'):
            solucion = diferencial(len(archivos),directorio)
        elif(metodo=='Enjambre'):
            solucion = enjambreParticulas(len(archivos),directorio)
        else:
            print('Metodo no soportado')
            
        #Mostramos el peso final alcanzado y que archivos eliminar
        tamanioAlcanzado = 0
        numSeleccionados = 0
        print('')
        print('::::::::::: Resultados :::::::::::')
        print("Debera eliminar los siguientes archivos:")
        print('')
        for idx in range(len(solucion)):
            if solucion[idx]:
                tamanioAlcanzado += pesos[idx]
                numSeleccionados += 1
                print(archivos[idx])
        print('')
        print("Total de archivos necesarios a eliminar: ", numSeleccionados)
        print("El tamaño actual es: ",round(tamanioActual/1024/1024,2))
        print("El tamaño total de los archivos seleccionados es: ", round(tamanioAlcanzado / 1024 / 1024, 2))
        print("Posible peso final: ",round((tamanioActual - tamanioAlcanzado)/1024/1024,2),'MB')

    
def genetico(numAlelos, directorio):
    # :::::::::::::::::::::: Algoritmo Genetico ::::::::::::::::::::::::::
    alelos = numAlelos
    individuos = 50
    tamano_gen = 1 #cada bit representa s
    generaciones = 2000
    factor_mutacion = 0.01
    ag = AG.AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, directorio)
    return ag.run()

def enjambreParticulas(numDimensiones, directorio):
    cantidad_individuos = numDimensiones
    dimensiones = numDimensiones
    ro = numDimensiones
    phi1_max=1.7
    phi2_max=2.0
    v_max=0.05
    generaciones=2000
    pso = PSO.PSO(cantidad_individuos, dimensiones, ro, phi1_max, phi2_max, v_max, directorio, generaciones)
    return pso.run()
    
def diferencial(numDimensiones, directorio):
    # :::::::::::::::::::::: Algoritmo Diferencial ::::::::::::::::::::::::::
    individuos = 50
    dimensiones = numDimensiones
    F = 0.5 #E[0.4,0.9]
    c = 0.85#E[0.1,1]
    generaciones = 2000
    ad = DO.DO(individuos, dimensiones, F, c, directorio,generaciones)
    return ad.run()

if __name__ == '__main__':
    main()
