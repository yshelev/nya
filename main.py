from PyQt5.QtWidgets import QApplication
import sys
from WindowsScripts.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())