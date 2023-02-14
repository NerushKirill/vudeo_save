import os
import datetime

from convert_pdf import converter_png
from receiving import receving
from searching import main_prog


#!!!!!!!!!!!from new day videosave
# current_date = datetime.datetime.today().strftime('mse for %d-%m-%Y')

# path_working = "..\\1_working_directory"
path_working = "../1_working_directory"
path_storage = "../2_program_storage"
path_output = "../3_output_program"

current_date = datetime.datetime.today().strftime('%d-%m-%Y')

file_log = "../logs/config_log.txt"
start_count = 0

with open(file_log, "r", encoding='utf-8') as f:
    # noinspection PyRedeclaration
    start_count = int([i for i in f][-1][-1])

if start_count == 0:
    with open(file_log, 'a', encoding='utf-8') as f:
        f.write(f'\n{current_date}\nlaunch = 1')
    try:
        os.mkdir(path_working)
        os.mkdir(path_storage)
        os.mkdir(path_output)
    except FileExistsError as e:
        print(e)


list_file = os.listdir(path_working)

if len(list_file) > 0:
    print('start __main__')
    for file_name in list_file:
        storage_path = f'{path_storage}/{current_date} ({file_name})'

        try:
            os.mkdir(storage_path)
            converter_png(path_working, file_name, 300, storage_path)
        except FileExistsError as e:
            print(e)
            continue

else:
    print('Нет файлов для работы')

#
#
#
#
#

# for i in range(2):
#     data = receving(i)
#     print(main_prog(data))
