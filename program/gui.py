import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from receiving import receving


def application(text_f):
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('name_app')
    window.setGeometry(50, 100, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText(text_f)
    main_text.move(10, 10)
    main_text.adjustSize()

    # btn = QtWidgets.QPushButton(window)
    # btn.move(70, 150)
    # btn.setText('next')
    # btn.setFixedWidth(200)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    text = receving(0)
    print(text)
    application(text)
