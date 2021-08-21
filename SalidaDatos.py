import cv2 as cv
import os

class SalidaDatos():
    def __init__(self):
        self.captura = None
        self.ret = None
        self.camara = None

    def CargarDatos(self):
        dataRuta = 'Reconocimiento Facial (Basico)\Entrenamientos\Caras'
        self.listaData = os.listdir(dataRuta)

        self.entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
        self.entrenamientoEigenFaceRecognizer.read('Reconocimiento Facial (Basico)\Entrenamientos\EntrenamientoEigenFaceRecognizer.xml')

        self.ruidos = cv.CascadeClassifier('Reconocimiento Facial (Basico)\Entrenamientos\haarcascade_frontalface_default.xml')

    def Reconocimiento(self):
        self.camara = cv.VideoCapture(0)

        while True:
            self.ret,self.captura= self.camara.read()

            grises = cv.cvtColor(self.captura, cv.COLOR_BGR2GRAY)
            idcaptura = grises.copy()

            cara = self.ruidos.detectMultiScale(grises, 1.3, 5)

            for(x, y, e1, e2) in cara:
                    
                rostroCapturado = idcaptura[y:y + e2, x:x + e1]
                rostroCapturado = cv.resize(rostroCapturado, (160, 160), interpolation = cv.INTER_CUBIC)

                resultado = self.entrenamientoEigenFaceRecognizer.predict(rostroCapturado)
                cv.putText(self.captura, '{}'.format(resultado), (x,y-5), 1,1.3, (0,255,0),1,cv.LINE_AA)
                cv.rectangle(self.captura, (x,y), (x+e1, y+e2), (255,0,0), 2)

                if resultado[1]< 6000:
                    cv.putText(self.captura, '{}'.format(self.listaData[resultado[0]]), (x,y-20), 2,1.1,(0,255,0),1,cv.LINE_AA)
                    cv.rectangle(self.captura, (x,y), (x+e1,y+e2), (255,0,0),2)
                else:
                    cv.putText(self.captura,"No encontrado", (x,y-20), 2,0.7,(0,255,0),1,cv.LINE_AA)
                    cv.rectangle(self.captura, (x,y), (x+e1,y+e2), (255,0,0),2)


            cv.imshow('Resultado', self.captura)

            if cv.waitKey(1) == ord('s'):
                break

        self.camara.release()
        cv.destroyAllWindows()

