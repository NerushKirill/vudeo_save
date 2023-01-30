from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="login",
        password="pass"
    ) as connection:

        create_db_query = "CREATE DATABASE IF NOT EXISTS online_movie_rating"

        with connection.cursor() as cursor:
            cursor.execute(create_db_query)

except Error as e:
    print(e)
