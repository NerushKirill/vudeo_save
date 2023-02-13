import re
from datetime import datetime

from receiving import receving
from search_config import search_mse


def main_string(n: int):
    data = receving(n)
    result_search = [*search_mse(data)]

    return result_search


def subdivision(train_1):
    # for subdivision table
    _es_or_buro = train_1[0].split(' ')[0]
    _number_division = train_1[0].split(' ')[1][1:]
    _room_number = train_1[1].split(' ')[1][1:]  # сравнить с номером кабинета из subdivision.cabinet_mse

    return [_es_or_buro, _number_division, _room_number]


def new_note(len_res_search, train_1, train_3):
    # for note table
    note_id = 661
    iso_number = '661/ВН'
    count_record_day = len_res_search  # сравнить значение с len(train_2)
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
    _full_name = (re.findall('[А-Яа-я]{1,} [А-Яа-я]{1,} [А-Яа-я]{1,}', train_2[0])[0]).split(' ')
    s_name = _full_name[0]
    f_name = _full_name[1]
    m_name = _full_name[2]
    birthday = datetime.strptime(train_2[1], '%d.%m.%Y').strftime('%Y-%m-%d')

    _total_time_mse = re.findall('[\d]{1,2}:[\d]{1,2}', train_2[2])
    time_start_mse = _total_time_mse[0]
    time_end_mse = _total_time_mse[1]

    return [s_name, f_name, m_name, birthday, time_start_mse, time_end_mse]


def main():
    result_search = main_string(0)
    k = len(result_search[1])
    l = result_search[1]

    train_1 = re.split(',\n{0,1} {0,1}', result_search[0][0])
    train_3 = result_search[2][1]

    print(train_1)

    for i in l:
        train_2 = re.split(',\n{0,1} {0,1}', i)
        print(new_mse(train_2))

    print(train_3)


if __name__ == '__main__':
    main()
