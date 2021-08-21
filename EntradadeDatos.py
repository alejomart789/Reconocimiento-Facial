import cv2 as cv
import os
import imutils

# La capa de entrada es la primera parte de nuestra pequeña red neuronal que almacenara 
# todos los datos iniciales de Reconocimiento Facial

class Capa1Entrada():
    def __init__(self):
        pass

    # La funcion busca la ruta y verifica si existe la carpeta en la ruta exapta y si no existe la crea
    def CrearCarpeta(self,nombrePersona):
        self.nombreModelo = nombrePersona
        rutaCaras = 'C:/Users/A L E J A N D R O/Documents/Python/Reconocimiento Facial (Basico)/Entrenamientos/Caras'
        self.rutaCompleta = rutaCaras + '/' + self.nombreModelo # Guarda la ruta en una variable

        # Si no existe la carpeta con el nombre la crea
        if not os.path.exists(self.rutaCompleta):
            print(f'\nLa carpeta en la ruta {self.rutaCompleta} no existe...')
            os.makedirs(self.rutaCompleta)
            print(f'Se creo la carpeta {self.nombreModelo} en la ruta {self.rutaCompleta}')
    
    # Funcion donde se hara todo el proceso de caputa de la cara para guardarlos en las carpeta como imagenes
    def Captura(self):

        self.video = cv.VideoCapture(0) # Se define el numero de la camara o la ruta de imagen o video a capturar
        self.ruidos = cv.CascadeClassifier('Reconocimiento Facial (Basico)\Entrenamientos\haarcascade_frontalface_default.xml')

        id = 0
        while True:
            respuesta,captura = self.video.read() # Se lee la captura para verificar si funciona
            if respuesta == False:
                print(f'--Error al ejecutar el video: {respuesta}')
                break

            captura = imutils.resize(captura, width = 640) # Se cambia las dimensiones de la caputa - video para que no sea tan pesada la imagen

            print('Convirtiendo Captura a Escala de Grises...')
            grisCaptura = cv.cvtColor(captura, cv.COLOR_BGR2GRAY) # La captura - video se pasa a una version de grises para su mejor lectura
            idCaptura = captura.copy()

            caraDetectada = self.ruidos.detectMultiScale(grisCaptura, 1.3, 5)


            for(x, y, e1, e2) in caraDetectada:
                cv.rectangle(captura, (x, y), (x+e1, y+e2), (0, 255, 0), 2)

                rostroCapturado = idCaptura[y:y + e2, x:x + e1]
                rostroCapturado = cv.resize(rostroCapturado, (160, 160), interpolation = cv.INTER_CUBIC)
                cv.imwrite(self.rutaCompleta+'/imagen_{}.jpg'.format(id),rostroCapturado)
                id = id + 1

            cv.imshow('Resultado rostro', captura)

            if id == 501:
                print(f'\nSe Capturaron: {id} fotografias.')
                break
        
        self.video.release()
        cv.destroyAllWindows()
        print(f'Finalizando Caputa de rostro...')






