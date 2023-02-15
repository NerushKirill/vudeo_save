import re
from datetime import datetime

from receiving import receving
from search_config import search_mse


def main_string(data):
    result_search = [*search_mse(data)]

    return result_search


def subdivision(train_1):
    # for subdivision table
    subdivision_name = str()
    _es_or_buro = re.findall('.{0,}№', train_1[0])[0]

    match _es_or_buro:
        case 'экспертном составе №':
            subdivision_name = 'экспертный состав'
        case 'бюро №':
            subdivision_name = 'бюро'
        case _:
            return 'error'

    _number_division = re.findall('\d{1,2}', train_1[0])[0]
    _room_number = re.findall('\d{1,3}', train_1[1])[0]  # сравнить с номером кабинета из subdivision.cabinet_mse

    return [subdivision_name, _number_division, _room_number]


def new_note(last_note_id, count_mse, train_1, train_3):
    # for note table
    note_id = last_note_id + 1
    iso_number = str(note_id) + '/ВН'
    count_record_day = count_mse
    date_mse = datetime.strptime(train_1[2].split(' ')[1], '%d.%m.%Y').strftime('%Y-%m-%d')

    _total_time = re.findall('[\d]{1,2}:[\d]{1,2}', train_1[3])
    time_start_mse_day = _total_time[0]  # сравнить время начала и конца
    time_end_mse_day = _total_time[1]  # сравнить время начала и конца

    current_date_note = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    # gave перебрать список for _ in 'train_3 = result_search[2]': if != Ю.Ю. Корниенко: return _
    gave = train_3  # проверить != Ю.Ю. Корниенко

    return [note_id, iso_number, count_record_day, date_mse,
            time_start_mse_day, time_end_mse_day, current_date_note, gave]


def new_mse(train_2):
    # for mse table
    all_mse_in_day = []

    for mse in train_2:
        _full_name = str(re.findall('[А-Яа-я]{1,} [А-Яа-я]{1,} [А-Яа-я]{1,}', mse[0])[0]).split(' ')
        s_name = _full_name[0]
        f_name = _full_name[1]
        m_name = _full_name[2]
        birthday = datetime.strptime(mse[1], '%d.%m.%Y').strftime('%Y-%m-%d')

        _total_time_mse = re.findall('[\d]{1,2}:[\d]{1,2}', mse[2])
        time_start_mse = _total_time_mse[0]
        time_end_mse = _total_time_mse[1]

        all_mse_in_day.append([s_name, f_name, m_name, birthday, time_start_mse, time_end_mse])

    return all_mse_in_day


def main_prog(note_number, data):
    result_search = main_string(data)
    search_all_mse = result_search[1]
    count_mse = len(search_all_mse)

    train_1 = re.split(',\n{0,1} {0,1}', result_search[0][0])
    train_2 = [re.split(',\n{0,1} {0,1}', mse) for mse in search_all_mse]
    train_3 = result_search[2][1]

    sub_d = subdivision(train_1)
    note = new_note(note_number, count_mse, train_1, train_3)
    all_mse = new_mse(train_2)

    return [sub_d, note, all_mse]


if __name__ == '__main__':
    path = "../2_program_storage/15-02-2023 (test_2.pdf)"
    file_name = "sheet_1_(test_2.pdf).png"
    data = receving(path, file_name)

    print(*main_prog(661, data), sep='\n')
