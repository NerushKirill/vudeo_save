from pdf2image import convert_from_path


file = '../test_file/train_set.pdf'


def converter_png():
    images = convert_from_path(file, 400)
    for i, image in enumerate(images):
        image.save(f'../test_file/test_{i}.png')


if __name__ == '__main__':
    converter_png()
