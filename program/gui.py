import sys
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from receiving import receving


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


if __name__ == '__main__':

    for i in range(6):
        text = receving(i)

        # application(text)
        result1 = re.findall(r'составе №\d, кабинет №\d\d\d,\nза \d\d.\d\d.\d\d\d\d, время с \d\d:\d\d по \d\d:\d\d:',
                             rf'{text}')
        result1_1 = re.findall(r'бюро №\d, кабинет №\d\d\d,\nза \d\d.\d\d.\d\d\d\d, время с \d\d:\d\d по \d\d:\d\d:',
                               rf'{text}')

        result2 = re.findall(r'\d\).{0,}', rf'{text}')
        result3 = re.findall(r'\w\.\w\..{0,}', rf'{text}')
        print('------------', i)
        print(text)
        print(result1, result1_1)
        print(result2)
        print(result3)
        input()
