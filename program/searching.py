import re
from datetime import datetime

from receiving import receving
from search_config import search_mse


def program_main(n: int):
    data = receving(n)
    result_prog = [*search_mse(data)]

    # for debugging
    # for i in result_prog:
    #     print(i)

    return result_prog


if __name__ == '__main__':
    result_pars = program_main(0)
    train_1 = re.split(',\n{0,1} {0,1}', result_pars[0][0])
    train_2 = re.split(',\n{0,1} {0,1}', result_pars[1][0])
    train_3 = result_pars[2][1]

    # for subdivision table
    count_record_day = len(result_pars)  # сравнить значение с len(train_2)
    _es_or_buro = train_1[0].split(' ')[0]
    _number_division = train_1[0].split(' ')[1][1:]
    _room_number = train_1[1].split(' ')[1][1:]  # сравнить с номером кабинета из subdivision.cabinet_mse

    # for note table
    iso_number = '661/ВН'
    date_mse = datetime.strptime(train_1[2].split(' ')[1], '%d.%m.%Y').strftime('%Y-%m-%d')

    _total_time = re.findall('[\d]{1,2}:[\d]{1,2}', train_1[3])
    time_start_mse_day = _total_time[0]  # сравнить время начала и конца
    time_end_mse_day = _total_time[1]  # сравнить время начала и конца

    current_date_note = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    # gave перебрать список for _ in 'train_3 = result_pars[2]': if != Ю.Ю. Корниенко: return _
    gave = train_3  # проверить != Ю.Ю. Корниенко

    print(iso_number,
          count_record_day,
          _es_or_buro,
          _number_division,
          _room_number,
          date_mse,
          time_start_mse_day,
          time_end_mse_day,
          current_date_note,
          gave
          )

    print('------------------')

    # for mse table
    _full_name = (re.findall('[А-Яа-я]{1,} [А-Яа-я]{1,} [А-Яа-я]{1,}', train_2[0])[0]).split(' ')
    s_name = _full_name[0]
    f_name = _full_name[1]
    m_name = _full_name[2]
    birthday = datetime.strptime(train_2[1], '%d.%m.%Y').strftime('%Y-%m-%d')

    _total_time_mse = re.findall('[\d]{1,2}:[\d]{1,2}', train_2[2])
    time_start_mse = _total_time_mse[0]
    time_end_mse = _total_time_mse[1]

    print(s_name,
          f_name,
          m_name,
          birthday,
          time_start_mse,
          time_end_mse
          )
