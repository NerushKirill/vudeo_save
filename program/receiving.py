import cv2
import pytesseract


def receving(n: int) -> str:
    # Path tesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    file = f'../test_file/test_{n}.png'

    # Add picture
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Text frame
    config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata" -l rus --oem 1 --psm 3'
    text = pytesseract.image_to_string(img, config=config)
    return str(text)


if __name__ == '__main__':

    for i in range(6):
        pass

