from re import split as re_split
from datetime import datetime

from receiving import receving
from search_config import search_mse


def program_main(n: int):
    data = receving(n)
    result_pars = [*search_mse(data)]

    for i in result_pars:
        print(i)

    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    print(current_date)
    return [result_pars, current_date]


if __name__ == '__main__':
    train = program_main(0)
    train_1 = re_split(',\n{0,1} {0,1}', train[0][0][0])

    iso_number = '661/ВН'
    es_or_buro = train_1[0].split(' ')[0]
    number_division = train_1[0].split(' ')[1]
    count_record_day = len(train[0][1])
    # date_mse =
    # time_start_mse_day =
    # time_end_mse_day =
    # current_date_note =
    # gave =

    # print('------------------')
    # print(train_1[1])
    # print(es_or_buro)
    # print(number_division)
    # print(count_record_day)

    # print(iso_number,
    #       count_record_day,
    #       date_mse,
    #       time_start_mse_day,
    #       time_end_mse_day,
    #       current_date_note,
    #       gave,
    #       )
