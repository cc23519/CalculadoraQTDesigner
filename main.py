import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculadoraQT_ui import Ui_MainWindow

class Calculadora(QMainWindow):
    def __init__(self) -> None:
        super(Calculadora, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())
