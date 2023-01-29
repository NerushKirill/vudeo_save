import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
