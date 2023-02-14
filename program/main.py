"""
mkdir Files_set
convert all files from Files_set to png
for i in Files: receiving i

"""

import os
import datetime

from convert_pdf import converter_png
from receiving import receving
from searching import main_prog


#!!!!!!!!!!!from new day videosave

# current_date = datetime.datetime.today().strftime('mse for %d-%m-%Y')
current_date = datetime.datetime.today().strftime('%d-%m-%Y')

file_log = "../logs/config_log.txt"
start_count = 0

with open(file_log, "r", encoding='utf-8') as file:
    # noinspection PyRedeclaration
    start_count = int([i for i in file][-1][-1])

if start_count == 0:
    with open(file_log, 'a', encoding='utf-8') as file:
        file.write(f'\n{current_date}\nlaunch = 1')
    try:
        os.mkdir(f'..\\1_working_directory')
        os.mkdir(f'..\\2_programm_storage')
    except FileExistsError as e:
        print(e)
else:
    print('12345')

#
#
#
#
#

# for i in range(2):
#     data = receving(i)
#     print(main_prog(data))
