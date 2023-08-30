#CALCULADORA BÁSICA FEITA EM QTDESIGNER E PYQT6
#Guilherme Pereira!

#Importando...
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from calculadoraQT_ui import Ui_MainWindow

#Classe Tela Calculadora
class Calculadora(QMainWindow):
    #Inicializador
    def __init__(self) -> None:
        super(Calculadora, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        #Botões - 20 BOTÕES (Contém 18 ainda)
class Calculadora(QMainWindow):
    def __init__(self):
        super(Calculadora, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar os botões aos métodos corretamente
        self.ui.buttonMaiseMenos.clicked.connect(lambda: self.MostrarNumerosVisor("-"))
        self.ui.buttonVirgula.clicked.connect(lambda: self.MostrarNumerosVisor(","))
        self.ui.button1.clicked.connect(lambda: self.MostrarNumerosVisor("1"))
        self.ui.button2.clicked.connect(lambda: self.MostrarNumerosVisor("2"))
        self.ui.button3.clicked.connect(lambda: self.MostrarNumerosVisor("3"))
        self.ui.button4.clicked.connect(lambda: self.MostrarNumerosVisor("4"))
        self.ui.button5.clicked.connect(lambda: self.MostrarNumerosVisor("5"))
        self.ui.button6.clicked.connect(lambda: self.MostrarNumerosVisor("6"))
        self.ui.button7.clicked.connect(lambda: self.MostrarNumerosVisor("7"))
        self.ui.button8.clicked.connect(lambda: self.MostrarNumerosVisor("8"))
        self.ui.button9.clicked.connect(lambda: self.MostrarNumerosVisor("9"))
        self.ui.button0.clicked.connect(lambda: self.MostrarNumerosVisor("0"))
        self.ui.buttonDiv.clicked.connect(lambda: self.MostrarNumerosVisor("/"))
        self.ui.buttonMai.clicked.connect(lambda: self.MostrarNumerosVisor("+"))
        self.ui.buttonMen.clicked.connect(lambda: self.MostrarNumerosVisor("-"))
        self.ui.buttonMulti.clicked.connect(lambda: self.MostrarNumerosVisor("*"))
        self.ui.buttonIgual.clicked.connect(self.RealizarConta)
        self.ui.buttonCE.clicked.connect(self.Limparvisor)

    def MostrarNumerosVisor(self, valor):
        texto = self.ui.visor.text()
        novo_carac = texto + valor
        self.ui.visor.setText(novo_carac)

    def Limparvisor(self):
        self.ui.visor.clear()

    def RealizarConta(self):
        equacao = self.ui.visor.text()
        try:
            resultado = eval(equacao)
            self.ui.visor.setText(str(resultado))
        except Exception as e:
            self.ui.visor.setText("Ocorreu um erro.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec())
        #lembrete: adicionar os botões de x/1, x2.
