import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def application(text_f):
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('video_saver')
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


def main():
    application()


if __name__ == '__main__':
    main()
