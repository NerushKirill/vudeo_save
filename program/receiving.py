import cv2
import pytesseract

from config import path_pytesseract


def receving(file_path, file_name):
    # Path tesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    file = f'{file_path}/{file_name}'

    # Add picture
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Text frame
    config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" -l rus --oem 1 --psm 3'
    text = pytesseract.image_to_string(img, config=config)
    return str(text)


if __name__ == '__main__':
    path = "../2_program_storage/16-02-2023 (new_test.pdf)"
    file_name = "sheet_0_(new_test.pdf).png"
    data = receving(path, file_name)
    print(data)
