import os
import datetime

from convert_pdf import converter_png
from receiving import receving
from searching import main_prog
from external_db import select_db, inset_db, main_cursor


path_working = "../1_working_directory"
path_storage = "../2_program_storage"
path_output = "../3_output_program"

current_date = datetime.datetime.today().strftime('%d-%m-%Y')

file_log = "../logs/config_log.txt"
counter_log = "../logs/counter.txt"
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

        requests_first_start = f'''
        INSERT INTO note (note_id, count_record_day, date_mse, time_start_mse_day, time_end_mse_day, current_date_note, gave) 
        VALUES ({int(input("Введите последний номер МСЭ по журналу: "))},
                0,
                0,
                0,
                0,
                0,
                'Последний номер предыдущего журнала МСЭ')
        '''

        main_cursor(inset_db, requests_first_start)

    except FileExistsError as e:
        print(e)


list_file = os.listdir(path_working)

num = 0

storage_path = f'{path_storage}/{current_date}_{num}'
save_mse_path = f'save mse for {current_date}_{num}'

try:
    os.mkdir(storage_path)
    os.mkdir(f'{path_output}/{save_mse_path}')
except FileExistsError as e:
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    num += 1
    os.mkdir(storage_path)
    os.mkdir(f'{path_output}/{save_mse_path}')


if len(list_file) > 0:
    for file_name in list_file:
        try:
            converter_png(path_working, file_name, 300, storage_path)

            for sheet in os.listdir(storage_path):
                # TODO Сортировка служебных записок по подразделениям
                # TODO Очистка working_directory
                # TODO Добавить логи

                request_last_note_id = """
                SELECT note_id FROM note ORDER BY note_id DESC LIMIT 1;
                """
                last_note_id = main_cursor(select_db, request_last_note_id)[0]

                data = receving(storage_path, sheet)
                working_train = main_prog(last_note_id, data)

                # сопоставление номера кабинета из бд и working_train[0][2]

                request_room_number = f"""
                SELECT subdivision_id, cabinet_mse 
                FROM subdivision 
                WHERE es_or_buro = '{working_train[0][0]}' AND number_division = '{working_train[0][1]}';
                """

                subd_id_number = main_cursor(select_db, request_room_number)

                # if subd_id_number[1] == working_train[0][2]:
                    # print('number room - good')
                # else:
                    # print('number room - bad')

                # добавление записи в таблицу note
                request_add_note = f"""
                INSERT INTO note (note_id, count_record_day, date_mse, time_start_mse_day, time_end_mse_day, current_date_note, gave) 
                VALUES ({working_train[1][0]},
                        {working_train[1][1]},
                        '{working_train[1][2]}',
                        '{working_train[1][3]}',
                        '{working_train[1][4]}',
                        '{working_train[1][5]}',
                        '{working_train[1][6]}')
                """

                main_cursor(inset_db, request_add_note)

                mse_list = []

                # добавление записей в таблицу mse
                for mse in working_train[2]:

                    request_add_mse = f"""
                    INSERT INTO 
                    mse(id_es_buro, sub_note_id, s_name, f_name, m_name, birthday, time_start_mse, time_end_mse)
                    VALUES ({subd_id_number[0]}, 
                            {working_train[1][0]}, 
                            '{mse[0]}', 
                            '{mse[1]}', 
                            '{mse[2]}', 
                            '{mse[3]}', 
                            '{mse[4]}', 
                            '{mse[5]}');
                    """

                    main_cursor(inset_db, request_add_mse)

                    start_mse = '.'.join(mse[4].split(':'))
                    end_mse = '.'.join(mse[5].split(':'))
                    name_mse_dir = f'{mse[0]} {mse[1][0]}.{mse[2][0]}. ({start_mse}-{end_mse})'
                    mse_list.append(name_mse_dir)

                mse_list_str: str = ', '.join(mse_list)

                name_note_dir = ' '.join([f'({working_train[1][0]}-ВН)',
                                          str(working_train[0][0]),
                                          str(working_train[0][1]),
                                          f'({working_train[1][2]})',
                                          f'({mse_list_str})'
                                          ])

                os.mkdir(f'{path_output}/{save_mse_path}/{name_note_dir}')
                input('next_video')

        except FileExistsError as e:
            print(e)
            continue

else:
    print('Нет файлов для работы')
