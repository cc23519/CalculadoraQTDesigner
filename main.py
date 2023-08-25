#CALCULADORA BÁSICA FEITA EM QTDESIGNER E PYQT6
#Guilherme Pereira!

#Importando...
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculadoraQT_ui import Ui_MainWindow

#Classe Tela Calculadora
class Calculadora(QMainWindow):


    #Inicializador
    def __init__(self) -> None:
        super(Calculadora, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Botões - 20 BOTÕES (Contém 18 ainda)
        self.buttonMaiseMenos.clicked.connect(self.MostrarNumerosVisor("-"))
        self.buttonVirgula.clicked.connect(self.MostrarNumerosVisor(","))
        self.button1.clicked.connect(self.MostrarNumerosVisor("1"))
        self.button2.clicked.connect(self.MostrarNumerosVisor("2"))
        self.button3.clicked.connect(self.MostrarNumerosVisor("3"))
        self.button4.clicked.connect(self.MostrarNumerosVisor("4"))
        self.button5.clicked.connect(self.MostrarNumerosVisor("5"))
        self.button6.clicked.connect(self.MostrarNumerosVisor("6"))
        self.button7.clicked.connect(self.MostrarNumerosVisor("7"))
        self.button8.clicked.connect(self.MostrarNumerosVisor("8"))
        self.button9.clicked.connect(self.MostrarNumerosVisor("9"))
        self.button0.clicked.connect(self.MostrarNumerosVisor("0"))
        self.buttonDiv.clicked.connect(self.MostrarNumerosVisor("/"))
        self.buttonMai.clicked.connect(self.MostrarNumerosVisor("+"))
        self.buttonMen.clicked.connect(self.MostrarNumerosVisor("-"))
        self.buttonMulti.clicked.connect(self.MostrarNumerosVisor("*"))
        self.buttonIgual.clicked.connect(self.RealizarConta())
        self.buttonCE.clicked.connect(self.Limparvisor())
        #lembrete: adicionar os botões de x/1, x2.


    #Mostra caracteres clickados no visor
    def MostrarNumerosVisor(self, valor):
        self.texto = self.visor.text()
        self.novocarac = self.texto =+ valor
        self.visor.setText(self.novocarac)


    #Limpa o visor
    def Limparvisor(self):
        self.visor.clear()


    #Pega a string do visor e a interpreta como equação
    def RealizarConta(self):
        self.equacao = self.visor.text()
        try:
            resultado = eval(self.equacao)
            self.visor.setText(resultado)
        except Exception as e:
            self.visor.setText("Ocorreu um erro.")

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())
