from tkinter import * 


from EntradadeDatos import Capa1Entrada
from Entrenamiento import Entrenamiento
from SalidaDatos import SalidaDatos


entradaDatos = Capa1Entrada()
entrenamientoDatos = Entrenamiento()
reconocimiento = SalidaDatos()

def PantallaNombre():

    def AccionInciar():
        nombre = entradaTexto.get()
        print(nombre)

        if nombre == '':
            print('-- Error, tiene que ingresar un nombre, el campo no puede estar vacio.')
            labelInfo= Label(ventanaEmergente, text ='Error, Campo Vacio.', bg = '#000335', fg = 'Red', width = 1000, font = ('Verdana', 12))
            labelInfo.place(x= 200, y= 125, anchor = 'center')
        else:
            entradaDatos.CrearCarpeta(nombre)
            entradaDatos.Captura()
        
    ventanaEmergente = Tk()
    ventanaEmergente.title('NOMBRE DE NUEVO USUARIO - RECONOCIMIENTO FACIAL')
    ventanaEmergente.iconbitmap('Reconocimiento Facial (Basico)/Recursos/reconocimiento-facial.ico')
    ventanaEmergente.config(bg = '#000335')
    
    ancho_ventana = 400
    alto_ventana = 150

    x_ventana = ventanaEmergente.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventanaEmergente.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana - 30)
    ventanaEmergente.geometry(posicion)

    labelInicio = Label(ventanaEmergente, text ='Ingresar nombre del nuevo usuario', bg = '#000335', fg = '#00D709', width = 1000, font = ('Verdana', 12))
    labelInicio.place(x= 200, y=25, anchor = 'center')

    entradaTexto = Entry(ventanaEmergente)
    entradaTexto.place(x = 200, y = 60, anchor = 'center', width = 150, height = 20)
    
    botonIniciar = Button(ventanaEmergente, text = 'Iniciar', command = AccionInciar)
    botonIniciar.place(x = 200, y = 100, anchor = 'center', width = 100, height = 20)


    ventanaEmergente.mainloop()

def AccionEntrenar():
    print('Se iniciara a hacer el entrenamiento...')
    entrenamientoDatos.DefinirRuta()
    entrenamientoDatos.CrearEntreno()
def AccionReconocer():
    print('Iniciando Reconocimiento...')
    reconocimiento.CargarDatos()
    reconocimiento.Reconocimiento()





ventanaRaiz = Tk()
ventanaRaiz.title("RECONOCIMIENTO FACIAL - Alejandro Martínez")
ventanaRaiz.iconbitmap('Reconocimiento Facial (Basico)/Recursos/reconocimiento-facial.ico')
ventanaRaiz.config(bg = '#000335')

ancho_ventana = 800
alto_ventana = 200

x_ventana = ventanaRaiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventanaRaiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana - 30)
ventanaRaiz.geometry(posicion)

ventanaRaiz.resizable(0,0)

labelInicio = Label(ventanaRaiz, text ='RECONOCIMIENTO FACIAL - Alejandro Martínez', bg = '#000335', fg = '#00D709', width = 800, font = ('Verdana',24))
labelInicio.place(x= 400, y=25, anchor = 'center')

botonAgregar = Button(ventanaRaiz, text = 'Ingresar nuevo usuario', command = PantallaNombre)
botonAgregar.place(x= 450 , y = 85, width= 150, height=30)

botonEntrenar = Button(ventanaRaiz, text = 'Entrenar', command = AccionEntrenar)
botonEntrenar.place(x= 300, y = 85, width=100, height=30)

botonIniciarReconocimiento = Button(ventanaRaiz, text = 'Iniciar', command = AccionReconocer)
botonIniciarReconocimiento.place(x= 150, y = 85, width=100, height=30)









ventanaRaiz.mainloop()
