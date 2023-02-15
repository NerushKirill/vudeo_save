from pdf2image import convert_from_path


def converter_png(path_file, file_name, quality, out_path):
    images = convert_from_path(f'{path_file}/{file_name}', quality)
    for i, image in enumerate(images):
        image.save(f'{out_path}/sheet_{i}_({file_name}).png')


if __name__ == '__main__':
    path_file = "../1_working_directory"
    file_name = "test_1.pdf"
    quality = 300
    out_path = "../2_program_storage"
    converter_png(path_file, file_name, quality, out_path)
