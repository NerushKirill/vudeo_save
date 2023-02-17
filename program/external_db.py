from mysql.connector import connect, Error

from config import host_db, user_db, password_db, database_name


request_1 = f"""
SELECT note_id FROM note ORDER BY note_id DESC LIMIT 1;
"""

# request_1 = f"""
# SELECT subdivision_id FROM subdivision WHERE es_or_buro = '{}' AND number_division = '{}'
# """

request_2 = f"""
INSERT INTO note (note_id, count_record_day, date_mse, time_start_mse_day, time_end_mse_day, current_date_note, gave)
VALUES (1, 2, '2023-01-01', '9:30', '12:00', '2023-02-10 12:15', 'И.О. Фамилия')
"""


def select_db(connection, request):
    with connection.cursor() as cursor:
        cursor.execute(request)
        result = cursor.fetchall()
        for row in result:
            return row


def inset_db(connection, request):
    with connection.cursor() as cursor:
        cursor.execute(request)
        connection.commit()


def main_cursor(command, request):
    try:
        with connect(
                host=host_db,
                user=user_db,
                password=password_db,
                database=database_name
        ) as connection:

            if command == select_db:
                return command(connection, request)
            elif command == inset_db:
                command(connection, request)
                print('complete')

    except Error as e:
        print(e)


def main():
    #запрос последней записи
    main_cursor(select_db, request_1)
    # main_cursor(inset_db, request_2)


if __name__ == '__main__':
    main()
