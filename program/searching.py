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


if __name__ == '__main__':
    program_main(0)
