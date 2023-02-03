import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from receiving import receving
from search_config import search_mse


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
    text = receving(0)
    search = search_mse(text)
    print(*search)
    application(text)


if __name__ == '__main__':
    main()
