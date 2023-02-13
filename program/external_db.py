from mysql.connector import connect, Error
from config import host_db, user_db, password_db, database_name
from searching import main


# train = main(0)
train = ['бюро', '1']

request_1 = f"""
SELECT * FROM subdivision WHERE es_or_buro = '{train[0]}' AND number_division = {train[1]}
"""

# request_1 = f"""
# INSERT INTO note (iso_number, count_record_day, date_mse, time_start_mse_day, time_end_mse_day, current_date_note, gave)
# VALUES ('661/ВН', 2, '2022-11-07', '09:35', '11:30', '2023-02-10 12.47','И.О. Фамилия')
# """

# request_2 = f"""
# INSERT INTO mse (id_es_buro, sub_note_id, s_name, f_name, m_name, birthday, time_start_mse, time_end_mse)
# VALUES (5, 3, 'Фамилия', 'Имя', 'Отчество', '1990-01-01', '10:00', '12:00');
# """
#
# equest_3 = """
# INSERT INTO mse (id_es_buro, sub_note_id, s_name, f_name, m_name, birthday, time_start_mse, time_end_mse)
# VALUES (5, 3, 'Фамилия', 'Имя', 'Отчество', '1990-01-01', '10:00', '12:00');
# """

try:
    with connect(
        host=host_db,
        user=user_db,
        password=password_db,
        database=database_name
    ) as connection:

        requests = [request_1,
                    ]

        with connection.cursor() as cursor:
            cursor.execute(request_1)
            _subdivision_id = cursor.fetchall()
            print(_subdivision_id[0][0])

        # with connection.cursor() as cursor:
        #     for request in requests:
        #         cursor.execute(request)
        #         connection.commit()

except Error as e:
    print(e)
