from pdf2image import convert_from_path


file = '../test_file/training.pdf'


def program():
    images = convert_from_path(file, 300)
    for i, image in enumerate(images):
        image.save(f'../test_file/test_{i}.png')


if __name__ == '__main__':
    program()
