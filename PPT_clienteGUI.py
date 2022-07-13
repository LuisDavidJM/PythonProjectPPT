import sys
import time
#GUI
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QDialog, QDialogButtonBox, QVBoxLayout
from PySide2.QtCore import QTimer
from PPTui import Ui_Form
#TCP
import socket

class QtWindow(QMainWindow):
    
    def __init__(self):
        super(QtWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Equipo 15")
        self.mensajeJuego("")
        
        self.salido = True
        self.usuario = 0
        self.win1 = 0
        self.lose1 = 0
        self.tie1 = 0
        self.win2 = 0
        self.lose2 = 0
        self.tie2 = 0
        self.win3 = 0
        self.lose3 = 0
        self.tie3 = 0

        self.show()

        time.sleep(1)
        self.ui.seleccion.activated.connect(self.seleccionJuego)
        self.ui.jugar.clicked.connect(self.botonJugar)
        self.ui.cerrar.clicked.connect(self.botonCerrar)

        self.ui.seleccion.setDisabled(True)
        self.ui.img1.setVisible(False)  
        self.ui.img2.setVisible(False)  
        self.ui.jugar.setDisabled(True)

        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Otro usuario salio")
        self.dialog.layout = QVBoxLayout()
        msg = QLabel("¿Esperar otro contrincante?")
        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.dialog.buttonBox = QDialogButtonBox(btn)
        self.dialog.buttonBox.accepted.connect(self.Recibir)
        self.dialog.buttonBox.rejected.connect(self.botonCerrar)
        self.dialog.layout.addWidget(msg)
        self.dialog.layout.addWidget(self.dialog.buttonBox)
        self.dialog.setLayout(self.dialog.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Recibir)
        self.timer.start()
        
    def Recibir(self):
        self.dialog.close()
        self.estado = True
        if self.estado:
            d = s.recv(40).decode("utf-8")
            if d == "Bienvenido al servidor":
                self.mensajeSistema("Bienvenido al servidor")
            elif d == "Esperando al otro jugador":
                self.mensajeSistema("Esperando al otro jugador")
            elif d == "Listo para jugar 1":
                self.mensajeSistema("Listo para jugar") 
                self.ui.seleccion.setEnabled(True)
                self.estado = False
                self.usuario = 1
                self.timer.stop()
            elif d == "Listo para jugar 2":
                self.mensajeSistema("Listo para jugar") 
                self.ui.seleccion.setEnabled(True)
                self.estado = False
                self.usuario = 2
                self.timer.stop()
            elif d == "El otro usuario se salio":
                if self.salido:
                    self.salido = False
                    self.win1 = 0
                    self.lose1 = 0
                    self.tie1 = 0
                    self.win2 = 0
                    self.lose2 = 0
                    self.tie2 = 0
                    self.ui.win1.setText(str(self.win1))
                    self.ui.lose1.setText(str(self.lose1))
                    self.ui.tie1.setText(str(self.tie1))
                    self.ui.win2.setText(str(self.win2))
                    self.ui.lose2.setText(str(self.lose2))
                    self.ui.tie2.setText(str(self.tie2))
                    self.dialog.activateWindow()
                    self.dialog.exec_()
                else:
                     ...
            if self.usuario == 1:
                if d == "Gana1":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("tijera.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("piedra.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("papel.png")
                    self.mensajeJuego("Ganaste")
                    self.win1 += 1
                    self.lose2 += 1
                    self.win3 += 1
                    self.ui.win1.setText(str(self.win1))
                    self.ui.lose2.setText(str(self.lose2))
                    self.ui.win3.setText(str(self.win3))
                    self.ui.img2.setVisible(True) #
                    self.ui.jugar.setDisabled(True)
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: green; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()
                elif d == "Pierde1":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("papel.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("tijera.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("piedra.png")
                    self.mensajeJuego("Perdiste")
                    self.lose1 += 1
                    self.win2 += 1
                    self.lose3 += 1
                    self.ui.lose1.setText(str(self.lose1))
                    self.ui.win2.setText(str(self.win2))
                    self.ui.lose3.setText(str(self.lose3))
                    self.ui.img2.setVisible(True) #
                    self.ui.jugar.setDisabled(True) 
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: red; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()
                elif d == "Empate":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("piedra.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("papel.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("tijera.png")
                    self.mensajeJuego("Empate")
                    self.tie1 += 1
                    self.tie2 += 1
                    self.tie3 += 1
                    self.ui.tie1.setText(str(self.tie1))
                    self.ui.tie2.setText(str(self.tie2))
                    self.ui.tie3.setText(str(self.tie3))
                    self.ui.img2.setVisible(True) #
                    self.ui.jugar.setDisabled(True)
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: blue; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()
            if self.usuario == 2:
                if d == "Gana1":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("papel.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("tijera.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("piedra.png")
                    self.mensajeJuego("Perdiste")
                    self.lose1 += 1
                    self.win2 += 1
                    self.lose3 += 1
                    self.ui.lose1.setText(str(self.lose1))
                    self.ui.win2.setText(str(self.win2))
                    self.ui.lose3.setText(str(self.lose3))
                    self.ui.img2.setVisible(True) #
                    self.ui.jugar.setDisabled(True)
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: red; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()
                elif d == "Pierde1":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("tijera.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("piedra.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("papel.png")
                    self.mensajeJuego("Ganaste")
                    self.win1 += 1
                    self.lose2 += 1
                    self.win3 += 1
                    self.ui.win1.setText(str(self.win1))
                    self.ui.lose2.setText(str(self.lose2))
                    self.ui.win3.setText(str(self.win3))
                    self.ui.img2.setVisible(True) #
                    self.ui.jugar.setDisabled(True)
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: green; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()
                elif d == "Empate":
                    if self.seleccionJuego() == 'Piedra':
                        self.imagen2("piedra.png")
                    elif self.seleccionJuego() == 'Papel':
                        self.imagen2("papel.png")
                    elif self.seleccionJuego() == 'Tijera':
                        self.imagen2("tijera.png")
                    self.mensajeJuego("Empate")
                    self.tie1 += 1
                    self.tie2 += 1
                    self.tie3 += 1
                    self.ui.tie1.setText(str(self.tie1))
                    self.ui.tie2.setText(str(self.tie2))
                    self.ui.tie3.setText(str(self.tie3))
                    self.ui.img2.setVisible(True)  #
                    self.ui.jugar.setDisabled(True)
                    self.ui.seleccion.setEnabled(True)
                    self.ui.msg1.setStyleSheet("background-color: blue; font: bold 20px;")
                    self.mensajeSistema("Elige otra vez")
                    self.estado = False
                    self.timer.stop()


    def mensajeJuego(self, Qmsg1):
        self.ui.msg1.setText(Qmsg1)

    def mensajeSistema(self,Qmsg2):
        self.ui.msg2.setText(Qmsg2)

    def imagen1(self, imag1):
        self.ui.img1.setPixmap(imag1)
    
    def imagen2(self, imag2):
        self.ui.img2.setPixmap(imag2)

    def botonJugar(self): #Accion al presionar boton jugar     
        opcion = self.seleccionJuego()
        if opcion == "Piedra":
            s.send(opcion.encode("utf-8"))
            self.timer.start()
            self.estado = True
            self.mensajeSistema("Esperando respuesta")
        elif opcion == "Papel":
            s.send(opcion.encode("utf-8"))
            self.timer.start()
            self.estado = True
            self.mensajeSistema("Esperando respuesta")
        elif opcion == "Tijera":
            s.send(opcion.encode("utf-8"))
            self.timer.start()
            self.estado = True
            self.mensajeSistema("Esperando respuesta")
        else:
            s.send("Nada".encode("utf-8"))
            self.timer.start()
            self.estado = True
            self.mensajeSistema("Esperando respuesta")

    def botonCerrar(self):
        s.send(f"Salir{self.usuario}".encode("utf-8")) #Accion al presionar boton cerrar
        print("Desconectado del servidor")
        s.close()
        sys.exit()

    def seleccionJuego(self):
        sel = self.ui.seleccion.currentText()
        if sel == 'Piedra':
            seleccion = "Piedra"
            self.imagen1("piedra.png")
        elif sel == 'Papel':
            seleccion = "Papel"
            self.imagen1("papel.png")
        elif sel == 'Tijera':
            seleccion = "Tijera"
            self.imagen1("tijera.png")
        else:
            seleccion = "Nada"
        self.ui.img1.setVisible(True) 
        self.ui.img2.setVisible(False)
        self.ui.msg1.setStyleSheet("background-color: white;") 
        self.mensajeJuego("")
        self.ui.jugar.setEnabled(True)
        self.salido = True
        return seleccion #Opcion del juago seleccionado

if __name__ == '__main__':
    s = socket.socket()
    server_host = 'localhost'
    server_port = 3015
    try:
        s.connect((server_host, server_port))
    except ConnectionRefusedError:
        print('El servicio no esta activo')
        print('Saliendo ...')
        sys.exit()   
    #GUI
    app = QApplication()
    window = QtWindow()
    sys.exit(app.exec_())
