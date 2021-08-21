import cv2 as cv
import os
import numpy as np
from time import time

class Entrenamiento():
    def __init__(self):
        pass

    def DefinirRuta(self):
        self.carasRuta = 'Reconocimiento Facial (Basico)/Entrenamientos/Caras'
        self.listaCaras = os.listdir(self.carasRuta)

        print(f'Datos: {self.listaCaras}')

    def CrearEntreno(self):
        ids = []
        carasDatos = []

        id = 0
        tiempoInicial = time()

        for fila in self.listaCaras:
            rutaCompleta = self.carasRuta + '/' + fila
            print('Iniciando lectura...')

            for archivo in os.listdir(rutaCompleta):
                print('Imagenes:',fila + '/' + archivo)

                ids.append(id)
                carasDatos.append(cv.imread(rutaCompleta + '/' + archivo, 0))

            id = id + 1
            tiempoFinalLectura = time()
            tiempoTotalLectura = tiempoFinalLectura - tiempoInicial
            print('Tiempo de lectura: ',tiempoTotalLectura)

        entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
        print('\nIniciando entrenamiento.. Espere...')

        entrenamientoEigenFaceRecognizer.train(carasDatos, np.array(ids))

        tiempoFinalEntrenamiento = time()
        tiempoTotalEntrenamiento = tiempoFinalEntrenamiento - tiempoTotalLectura
        print('Tiempo entrenamiento total:',tiempoTotalEntrenamiento)

        entrenamientoEigenFaceRecognizer.write('Reconocimiento Facial (Basico)/Entrenamientos/EntrenamientoEigenFaceRecognizer.xml')
        print('Entrenamiento concluido')