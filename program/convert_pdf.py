from pdf2image import convert_from_path


# file = '../test_file/tests/test_1.pdf'
file = '../test_file/tests/test_1.pdf'


def converter_png():
    images = convert_from_path(file, 300)
    for i, image in enumerate(images):
        image.save(f'../test_file/test_{i}.png')


if __name__ == '__main__':
    converter_png()
